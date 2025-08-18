from __future__ import annotations

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

DEFAULT_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DEFAULT_LOG_DIR = os.getenv("LOG_DIR", "logs")
DEFAULT_LOG_FILE = os.getenv("LOG_FILE", "app.log")
DEFAULT_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", 5 * 1024 * 1024))  # 5 MB
DEFAULT_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", 5))

_CONFIGURED = False


def _level_from_str(level_str: str) -> int:
    """Convierte 'INFO' → logging.INFO, con fallback a INFO."""
    return getattr(logging, level_str.upper(), logging.INFO)


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def configure_logging(
    level: str | int = DEFAULT_LEVEL,
    log_dir: str | Path = DEFAULT_LOG_DIR,
    log_file: str = DEFAULT_LOG_FILE,
    max_bytes: int = DEFAULT_MAX_BYTES,
    backup_count: int = DEFAULT_BACKUP_COUNT,
) -> None:
    """Configura el logging global de la app (idempotente)."""
    global _CONFIGURED
    if _CONFIGURED:
        return

    level_num = _level_from_str(level) if isinstance(level, str) else level

    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    root = logging.getLogger()
    root.setLevel(level_num)
    root.handlers.clear()

    console = logging.StreamHandler()
    console.setLevel(level_num)
    console.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
    root.addHandler(console)

    log_dir = Path(log_dir)
    _ensure_dir(log_dir)
    file_path = log_dir / log_file

    file_handler = RotatingFileHandler(
        filename=file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level_num)
    file_handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
    root.addHandler(file_handler)

    for noisy in ("urllib3", "botocore", "matplotlib"):
        logging.getLogger(noisy).setLevel(max(level_num, logging.WARNING))

    _CONFIGURED = True


def get_logger(name: str | None = None) -> logging.Logger:
    """Devuelve un logger ya configurado. Configura si nadie lo hizo aún."""
    if not _CONFIGURED:
        configure_logging()
    return logging.getLogger(name if name else __name__)
