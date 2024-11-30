## Prerequisites


1. **Docker and Docker Compose**: Ensure Docker is installed and the Docker Daemon is running. You can download it here: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) or install it via your package manager on Linux. You can find further information on the [official documentation](https://docs.docker.com/engine/install/).
2. **Python:** A version >=3.12 is required for this project
3. **pip:** [installation docs](https://pip.pypa.io/en/stable/installation/)

## Installation Linux


1. Clone the repository into a folder of your choice

```bash
git clone https://github.com/necodeIT/moodle-unit-tests.git && cd moodle-unit-tests
```


2. Build the Python package with: 

```bash
pip install -e .
```

## Usage

After successfully building the project the cli tool is now installed on your system. You can run it with the command `mut`.


:::warning
Currently the cli tool only works inside the moodle-unit-tests folder

:::

### Initializing and running a Docker instance

Before running a Docker instance select the version with


:::info
This method is not fully implemented, use the second one for now

:::

```bash
mut moodle init
```

or specify it directly in the command 

```bash
mut moodle init <version>
```

Once the version has been set you can start the Moodle instance with

```bash
mut moodle run
```

\

:::warning
**IF LINUX:** Do some permission stuff for the MariaDB container

After running the moodle containers for the first time the mariadb container will fail to start properly. Fix this with the following commands and start the containers again. For details: <https://github.com/bitnami/containers/issues/23841>

```javascript
useradd -u 1001 mariadb-bitnami
chown -R mariadb-bitnami:mariadb-bitnami ./docker/server/.moodle/mariadb
```

:::

\
## Troubleshooting

If you encounter any issues:

* **Windows**: Ensure Docker Desktop is running and WSL 2 is enabled (if using WSL).
* **Linux**: Verify Docker and Docker Compose permissions. You may need to add your user to the `docker` group to run Docker without `sudo`:

  ```bash
  sudo usermod -aG docker $USER
  ```


---

\
\
