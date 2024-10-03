# Project Evergreen

Project Evergreen is a group project for the class CSE312: Web Applications at the University at Buffalo in the Fall 2024 semester. This project is intended to become the web application for the UB IEEE student chapter automated greenhouse chapter. 

## Managing the Environment

The development environment is being managed using [Poetry](https://python-poetry.org/). Please make sure that you have Poetry installed:
```shell
pip install poetry
```

The virtual environment can be created locally by using the `poetry install` command. The environment can then be activated using the `poetry shell` command. This venv can then be deactivated by using the `exit` command. 

New package dependencies for the project can be added using the `poetry add <package-name-from-pip>` command. 
