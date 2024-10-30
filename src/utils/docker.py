import subprocess
import docker

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

def get_service_ip(service_name) -> str | None:
    client = docker.from_env()  # Connects to the Docker daemon
    try:
        # Find the container by service name
        container = client.containers.get(service_name)
        # Assuming the service is on a custom network, fetch the IP address
        ip_address = container.attrs['NetworkSettings']['Networks']['server_default']['IPAddress']
        return ip_address
    except docker.errors.NotFound:
        print(f"Service '{service_name}' not found.")
    except KeyError:
        print(f"Service '{service_name}' is not on the specified network or lacks an IP.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
