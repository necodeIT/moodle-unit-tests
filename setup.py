from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]
    
setup(
    name="moodle-unit-tests",  # Name of the package
    version="0.1.0",  # Version
    packages=find_packages(),  # Automatically find packages
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "mut=moodle_unit_tests.main:main",  # CLI command = module:function
        ],
    },
    author="Simon Wewalka",
    author_email="swewalka@pm.me",
    description="A simple CLI tool to test Moodle services and plugins",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/necodeIT/moodle-unit-tests/",  # Update with your repo
    python_requires=">=3.12",
)
