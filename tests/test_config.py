from pathlib import Path

from housing import config


def test_project_root():
    expected = Path(__file__).resolve().parents[1]

    assert config.PROJECT_ROOT == expected


def test_data_directories():
    assert config.DATA_DIR == config.PROJECT_ROOT / "data"
    assert config.RAW_DATA_DIR == config.DATA_DIR / "raw"
    assert config.PROCESSED_DATA_DIR == config.DATA_DIR / "processed"


def test_default_database_settings(monkeypatch):
    monkeypatch.delenv("DB_HOST", raising=False)
    monkeypatch.delenv("DB_PORT", raising=False)
    monkeypatch.delenv("DB_NAME", raising=False)
    monkeypatch.delenv("DB_USER", raising=False)
    monkeypatch.delenv("DB_PASSWORD", raising=False)

    # Reload config so it reads the modified environment.
    import importlib
    importlib.reload(config)

    assert config.DB_HOST == "localhost"
    assert config.DB_PORT == 5432
    assert config.DB_NAME == "uk_housing_intelligence"
    assert config.DB_USER == "housing_user"
    assert config.DB_PASSWORD == "dev_password"


def test_database_settings_from_environment(monkeypatch):
    monkeypatch.setenv("DB_HOST", "test-host")
    monkeypatch.setenv("DB_PORT", "5433")
    monkeypatch.setenv("DB_NAME", "test_database")
    monkeypatch.setenv("DB_USER", "test_user")
    monkeypatch.setenv("DB_PASSWORD", "test_password")

    import importlib
    importlib.reload(config)

    assert config.DB_HOST == "test-host"
    assert config.DB_PORT == 5433
    assert config.DB_NAME == "test_database"
    assert config.DB_USER == "test_user"
    assert config.DB_PASSWORD == "test_password"

