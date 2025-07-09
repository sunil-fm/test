# configs/config.py

from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[],
    environments=True,
    envvar_prefix="APP",
)

# Provide default values
settings.set("app_name", "MyApp")
settings.set(
    "logging", {"log_level": "DEBUG", "log_format": "%(levelname)s:%(message)s"}
)
