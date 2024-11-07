import os
import subprocess
from constants import *

def sql_dump_baseline() -> None:
    path = os.path.join(SQL_BASELINE_DUMP_DIR, "baseline.sql")

    command = [
    'docker-compose', '-f', 'docker/server/docker-compose.yaml',
    '--env-file', 'docker/.env', 'exec', MARIADB_HOST,
    '/opt/bitnami/mariadb/bin/mariadb-dump', '-u', MARIADB_USER,
    MARIADB_DATABASE
    ]

    # Execute the command and redirect the output to a file
    with open(path, 'w') as outfile:
        subprocess.run(command, stdout=outfile, stderr=subprocess.PIPE)


def sql_restore_baseline() -> None:
    path = os.path.join(SQL_BASELINE_DUMP_DIR, "baseline.sql")
    if not os.path.exists(path):
        print("Baseline SQL dump not found.")
        return
    
    print("Restoring database from baseline dump...")
    
    try:
        restore_command = (
            f"docker exec -i {MARIADB_CONTAINER_NAME} "
            f"/opt/bitnami/mariadb/bin/mariadb -u {MARIADB_USER} {MOODLE_DATABASE_NAME} < {SQL_BASELINE_DUMP_DIR}/baseline.sql"
        )
        subprocess.run(restore_command, shell=True, check=True)
        
        print("Database restore completed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during database restore: {e}")
