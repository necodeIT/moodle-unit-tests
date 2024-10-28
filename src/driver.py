from typing import List
import os
import subprocess

import click
from constants import *


class Config:
    http_port: int
    https_port: int
    version: str

    def __init__(
        self,
        version: str,
        http_port: int = 80,
        https_port: int = 443,
    ) -> None:
        self.version = version
        self.http_port = http_port
        self.https_port = https_port

    def __str__(self) -> str:
        return f"MOODLE_VERSION={self.version}\nHTTP_PORT={self.http_port}\nHTTPS_PORT={self.https_port}"

    @staticmethod
    def from_env(lines: list[str]) -> "Config":
        version = lines[0].split("=")[1].strip()
        http_port = int(lines[1].split("=")[1].strip())
        https_port = int(lines[2].split("=")[1].strip())
        return Config(version, http_port, https_port)


def launch_moodle() -> None:
    subprocess.run(
        [
            "docker-compose",
            "-f",
            os.path.join(SERVER_DIR, "docker-compose.yaml"),
            "--env-file",
            ENV_PATH,
            "up",
            "-d",
        ],
        check=True,
    )

def stop_moodle() -> None:
    subprocess.run(
        [
            "docker-compose",
            "-f",
            os.path.join(SERVER_DIR, "docker-compose.yaml"),
            "--env-file",
            ENV_PATH,
            "down",
        ],
        check=True,
    )

    click.echo("Moodle stopped.")


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

    click.echo(f"Baseline dump created at {path}.")


def load_config() -> Config:
    with open(ENV_PATH, "r") as f:
        lines = f.readlines()
        return Config.from_env(lines)


def save_config(config: Config) -> None:
    with open(ENV_PATH, "w") as f:
        f.write(str(config))
