from orator import DatabaseManager, Model, Schema
from dotenv import load_dotenv
import os

def load_env_var():
    load_dotenv()
    env_var = {
        "DB_ENDPOINT": os.environ.get("DB_ENDPOINT"),
        "DB_USERNAME": os.environ.get("DB_USERNAME"),
        "DB_PASSWORD": os.environ.get("DB_PASSWORD"),
        "DB_NAME": os.environ.get("DB_NAME"),
        "DB_PORT": int(os.environ.get("DB_PORT")),
        "DB_SSL_CA": os.environ.get("DB_SSL_CA")
    }

    return env_var
ENV_VAR = load_env_var()

DATABASES = {
    "mysql": {
        "driver": "mysql",
        "host": ENV_VAR["DB_ENDPOINT"],
        "database": ENV_VAR["DB_NAME"],
        "user": ENV_VAR["DB_USERNAME"],
        "password": ENV_VAR["DB_PASSWORD"],
        "port": ENV_VAR["DB_PORT"],
        "prefix": "",
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
