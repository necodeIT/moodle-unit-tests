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


**NOTICE:** Currently the cli tool only works inside the moodle-unit-tests folder


### Initializing and running Moodle

Before running a Docker instance select the version with


**NOTICE:** This method is not fully implemented, use the second one for now


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


**NOTICE**: If the mariadb container is not starting properly: Do some permission stuff for the MariaDB container

After running the moodle containers for the first time the mariadb container will fail to start properly. Fix this with the following commands and start the containers again. For details: <https://github.com/bitnami/containers/issues/23841>

```javascript
useradd -u 1001 mariadb-bitnami
chown -R mariadb-bitnami:mariadb-bitnami ./docker/server/.moodle/mariadb
```

### Using a database baseline

Once Moodle is up and running you can populate the database with data that is necessary for your tests (f.e. adding users or creating courses). To save the current state of the database as a baseline use this command:

```bash
mut baseline create
```

The saved database state will be restored before every test. The baseline can also be manually restored with:

```bash
mut baseline restore
```

### Creating and running Unittests

To create a Python unit test run:

```bash
mut test create <test_name> 
```

When creating a new test a new directory will be created in the `tests/TESTNAME`. In this directory there is a structured Python file where you can start writing your unit tests.  

To run a test use:

```bash
mut test run <test_name>
```

The results are saved in a markdown

## Troubleshooting

If you encounter any issues:

* **Windows**: Ensure Docker Desktop is running and WSL 2 is enabled (if using WSL).
* **Linux**: Verify Docker and Docker Compose permissions. You may need to add your user to the `docker` group to run Docker without `sudo`:

  ```bash
  sudo usermod -aG docker $USER
  ```
