import os

from dotenv import load_dotenv


def load_settings() -> dict[str, str]:
    load_dotenv()

    ENVS = {"ICEBERG_CHART_URL": "icebergcharts.com", "DATABASE_URL": "POSTGRESQL"}

    for env_name in ENVS.keys():
        loaded_value = os.getenv(env_name)
        if loaded_value:
            ENVS[env_name] = loaded_value

    return ENVS
