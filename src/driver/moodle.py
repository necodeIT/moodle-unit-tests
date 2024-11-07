import os
import subprocess

from constants import *
from utils import is_docker_compose_running

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
    #is moodle running?
    if is_docker_compose_running(os.path.join(SERVER_DIR, "docker-compose.yaml"), ENV_PATH):
        #stop moodle
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
    else:
        print("Moodle is not running")