import os
import subprocess

from constants import *
from utils import is_docker_compose_running


def launch_docker_compose() -> None:
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

def stop_docker_compose() -> None:
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
                "stop",
            ],
            check=True,
        )
    else:
        print("Moodle is not running")