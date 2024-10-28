import os

# MariaDB Constants
MARIADB_IMAGE = "docker.io/bitnami/mariadb:11.4"
MARIADB_ALLOW_EMPTY_PASSWORD = "yes"  # Only for development, use cautiously
MARIADB_USER = "bn_moodle"
MARIADB_DATABASE = "bitnami_moodle"
MARIADB_CHARACTER_SET = "utf8mb4"
MARIADB_COLLATE = "utf8mb4_unicode_ci"
MARIADB_VOLUME_PATH = ".moodle/mariadb"
MARIADB_HOST = "mariadb"
MARIADB_PORT = 3306  # Default port for MariaDB
MARIADB_CONTAINER_NAME = "server-mariadb-1"

# Moodle Constants
MOODLE_IMAGE = "docker.io/bitnami/moodle:${MOODLE_VERSION}"
MOODLE_HTTP_PORT = "${HTTP_PORT}"  # Defined in .env file
MOODLE_HTTPS_PORT = "${HTTPS_PORT}"  # Defined in .env file
MOODLE_DATABASE_HOST = MARIADB_HOST  # Reuse MariaDB host
MOODLE_DATABASE_PORT_NUMBER = MARIADB_PORT
MOODLE_DATABASE_USER = MARIADB_USER
MOODLE_DATABASE_NAME = MARIADB_DATABASE
MOODLE_ALLOW_EMPTY_PASSWORD = MARIADB_ALLOW_EMPTY_PASSWORD
MOODLE_VOLUME_PATH = ".moodle/moodle"
MOODLE_DATA_PATH = ".moodle/moodledata"
MOODLE_CONTAINER_NAME = "server-moodle-1"
MOODLE_HOST = "moodle"

DOCKER_DIR = "docker"
ENV_PATH = os.path.join(DOCKER_DIR, ".env")
SERVER_DIR = os.path.join(DOCKER_DIR, "server")
TESTS_DIR = os.path.join(DOCKER_DIR, "tests")
SQL_BASELINE_DUMP_DIR = os.path.join(SERVER_DIR, "sql_dump")

