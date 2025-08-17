from src.core.settings import settings


def test_env_is_valid():
    assert settings.env in {"dev", "prod"}


def test_yaml_loaded_and_minimal_keys_exist():
    assert settings.get("app") is not None
    assert isinstance(settings.app_port, int)
    assert isinstance(settings.app_debug, bool)


def test_db_url_is_string_or_none():
    db = settings.db_url
    assert db is None or isinstance(db, str)


def test_paths_block_is_dict():
    paths = settings.data_paths
    assert isinstance(paths, dict)
