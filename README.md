# Moodle Unit Tests

A framework for unit testing Moodle plugins.

## Getting Started

This program requires Docker and Docker Compose to be installed and running on your system. To install Docker and Docker Compose please follow the [official documentation](https://docs.docker.com/engine/install/). 

### Prerequisites

1. **Docker**: Ensure Docker is installed and the Docker Daemon is running. You can download it here: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) or install it via your package manager on Linux.
2. **Docker Compose**: Included by default in Docker Desktop on Windows. For Linux, you may need to install Docker Compose separately.
3. **Compatibility**: Supports Docker versions 20.10+ and Docker Compose versions 1.29+.
4. 

### Initializing a Moodle instance

After cloning the repository 

### IF LINUX: Do some permission stuff for the MariaDB container

After running the moodle containers for the first time the mariadb container will fail to start properly. Fix this with the following commands and start the containers again. For details: <https://github.com/bitnami/containers/issues/23841>

```bash
useradd -u 1001 mariadb-bitnami
chown -R mariadb-bitnami:mariadb-bitnami ./docker/server/.moodle/mariadb
```

## Troubleshooting

If you encounter any issues:

* **Windows**: Ensure Docker Desktop is running and WSL 2 is enabled (if using WSL).
* **Linux**: Verify Docker and Docker Compose permissions. You may need to add your user to the `docker` group to run Docker without `sudo`:

  ```bash
  sudo usermod -aG docker $USER
  ```


---
