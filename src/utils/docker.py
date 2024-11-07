import subprocess
import docker
import os

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


def stop_container(container_name: str):
    """Stop a running Docker container."""
    try:
        subprocess.run(["docker", "stop", container_name], check=True)
        print(f"Container '{container_name}' stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to stop container '{container_name}': {e}")


def backup_moodle(container_name: str, backup_path: str):
    """
    Back up Moodle data by copying from the container volume to a specified path.
    
    Args:
        container_name (str): Name of the Moodle container.
        backup_path (str): Path on the host to store the backup.
    """
    try:
        os.makedirs(backup_path, exist_ok=True)
        subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{backup_path}:/backups",
            "--volumes-from", container_name,
            "busybox", "cp", "-a", "/bitnami/moodle", "/backups/moodle"
        ], check=True)
        subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{backup_path}:/backups",
            "--volumes-from", container_name,
            "busybox", "cp", "-a", "/bitnami/moodledata", "/backups/moodledata"
        ], check=True)
        print("Backup completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to backup Moodle: {e}")

def backup_mariadb(container_name: str, backup_path: str):
    """
    Back up MariaDB data by copying from the container volume to a specified path.
    
    Args:
        container_name (str): Name of the MariaDB container.
        backup_path (str): Path on the host to store the backup.
    """
    try:
        os.makedirs(backup_path, exist_ok=True)
        subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{backup_path}:/backups",
            "--volumes-from", container_name,
            "busybox", "cp", "-a", "/bitnami/mariadb", "/backups/mariadb"
        ], check=True)
        print("Backup completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to backup MariaDB: {e}")


def restore_mariadb(container_name: str, backup_path: str):
    """
    Directly copy the backup data to the original MariaDB container volume.
    
    Args:
        container_name (str): Name of the running MariaDB container.
        backup_path (str): Path on the host where the backup is stored.
    """
    # Stop the container to avoid data inconsistency during restore
    stop_container(container_name)
    
    # Copy backup data into the container's volume
    try:
        subprocess.run([
            "docker", "cp", f"{backup_path}/mariadb", f"{container_name}:/bitnami/mariadb"
        ], check=True)
        print("MariaDB data restored from backup.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restore MariaDB data: {e}")

def restore_moodle(container_name: str, backup_path: str):
    """
    Directly copy the backup data to the original Moodle container volumes.
    
    Args:
        container_name (str): Name of the running Moodle container.
        backup_path (str): Path on the host where the backup is stored.
    """
    # Stop the container to avoid data inconsistency during restore
    stop_container(container_name)
    
    # Copy backup data into the container's volumes
    try:
        subprocess.run([
            "docker", "cp", f"{backup_path}/moodle", f"{container_name}:/bitnami/moodle"
        ], check=True)
        subprocess.run([
            "docker", "cp", f"{backup_path}/moodledata", f"{container_name}:/bitnami/moodledata"
        ], check=True)
        print("Moodle data restored from backup.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restore Moodle data: {e}")
