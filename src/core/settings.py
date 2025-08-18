from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "config"

load_dotenv(dotenv_path=ROOT_DIR / ".env", override=False)


# --- Helpers ---
def _expand_env(value: Any) -> Any:
    """Expande ${VAR} en strings usando el entorno."""
    if isinstance(value, str):
        return os.path.expandvars(value)
    if isinstance(value, dict):
        return {k: _expand_env(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_env(v) for v in value]
    return value


def _coerce_bool(val: Any) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        return val.strip().lower() in {"1", "true", "yes", "on"}
    return bool(val)


def _deep_get(d: dict[str, Any], path: str, default: Any = None) -> Any:
    """Obtiene una clave anidada del dict usando 'a.b.c'. Devuelve default si no existe."""
    cur: Any = d
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def _read_yaml(p: Path) -> dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"El YAML debe tener un objeto dict en la raíz: {p}")
    return _expand_env(data)


# --- Settings ---
class Settings:
    """
    Config central del proyecto.
    - Lee config/{APP_ENV}.yaml
    - Expande ${VAR} usando .env / entorno
    - Permite overrides por variables de entorno (ej: DB_URL, SECRET_KEY)
    """

    def __init__(self, env: str, cfg: dict[str, Any]):
        self.env = env
        self._cfg = cfg

    def get(self, path: str, default: Any = None) -> Any:
        return _deep_get(self._cfg, path, default)

    @property
    def db_url(self) -> str | None:
        return os.getenv("DB_URL") or self.get("database.url")

    @property
    def secret_key(self) -> str | None:
        return os.getenv("SECRET_KEY")

    @property
    def app_debug(self) -> bool:
        return _coerce_bool(self.get("app.debug", False))

    @property
    def app_port(self) -> int:
        return int(self.get("app.port", 8501))

    @property
    def allowed_hosts(self) -> list[str]:
        val = os.getenv("ALLOWED_HOSTS")
        if val:
            return [h.strip() for h in val.split(",")]
        return list(self.get("app.allowed_hosts", []))

    @property
    def data_paths(self) -> dict[str, str]:
        return dict(self.get("paths", {}))

    @property
    def experimental_enabled(self) -> bool:
        return _coerce_bool(
            os.getenv("ENABLE_EXPERIMENTAL") or self.get("features.enable_experimental", False)
        )


def load_settings() -> Settings:
    env = os.getenv("APP_ENV", "dev").lower()
    if env not in {"dev", "prod"}:
        print(f"[settings] APP_ENV='{env}' no reconocido. Usando 'dev'.", file=sys.stderr)
        env = "dev"

    cfg_path = CONFIG_DIR / f"{env}.yaml"
    if not cfg_path.exists():
        raise FileNotFoundError(f"No se encontró {cfg_path}. Creá config/{env}.yaml")

    cfg = _read_yaml(cfg_path)
    return Settings(env, cfg)


settings = load_settings()
