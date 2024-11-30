import os
import subprocess

from moodle_unit_tests.constants import *
from moodle_unit_tests.utils import stop_container, start_container
from moodle_unit_tests.driver.config import load_config

def sql_dump_baseline() -> None:
    conf = load_config()
    mdl_version = conf.version.replace(".", "_")
    path = os.path.join(SQL_BASELINE_DUMP_DIR, f"baseline_{mdl_version}.sql")

    command = [
        'docker', 'exec', '-i',
        MARIADB_CONTAINER_NAME,
        '/opt/bitnami/mariadb/bin/mariadb-dump',
        '-u', MARIADB_USER,
        MARIADB_DATABASE
    ]

    stop_container(MOODLE_CONTAINER_NAME)

    # Execute the command and redirect the output to a file
    with open(path, 'w') as outfile:
        subprocess.run(command, stdout=outfile, stderr=subprocess.PIPE)

    print(f"Baseline SQL dump created at {path}")

    start_container(MOODLE_CONTAINER_NAME)


def sql_restore_baseline() -> None:
    conf = load_config()
    mdl_version = conf.version
    path = os.path.join(SQL_BASELINE_DUMP_DIR, f"baseline_{mdl_version.replace(".", "_")}.sql")
    if not os.path.exists(path):
        print(f"Baseline SQL dump for Moodle version {mdl_version} not found.")
        return
    
    stop_container(MOODLE_CONTAINER_NAME)
    
    print("Restoring database from baseline dump...")
    
    try:
        restore_command = (
            f"docker exec -i {MARIADB_CONTAINER_NAME} "
            f"/opt/bitnami/mariadb/bin/mariadb -u {MARIADB_USER} {MOODLE_DATABASE_NAME} < {path}"
        )
        subprocess.run(restore_command, shell=True, check=True)
        
        print("Database restore completed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during database restore: {e}")

    start_container(MOODLE_CONTAINER_NAME)
