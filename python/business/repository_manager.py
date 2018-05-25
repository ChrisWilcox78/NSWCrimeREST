from os import environ

from persistence_mongo import repository as mongo_repo
from persistence_mysql import repository as mysql_repo

DEFAULT_REPO_TYPE = "MONGO"


def get_configured_repo():
    if (environ.get("CRIMES_REPO_TYPE", DEFAULT_REPO_TYPE) == "MONGO"):
        return mongo_repo
    return mysql_repo
