import subprocess

def is_docker_compose_running(file_path, env_path) -> bool:
    try:
        # Run `docker-compose ps` to list services and their status
        result = subprocess.run(
            ["docker-compose","-f", file_path, "--env-file",env_path, "ps"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # If there’s output, the service is running
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        # If the command fails, assume the service is not running
        return False
