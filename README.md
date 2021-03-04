# Python Sample App

This is a sample app to show how easy it is to get a Python application up and running.

# Prerequisites

- Python 3 is needed for this project. Python 2 is still installed by default on some sytems so
you should ensure you have Python3 installed. Check like this:

  ```
  which python3
  ```

- Pyenv will be used to manage the correct version. Pyenv is similar to rbenv and can be found
[here](https://github.com/pyenv/pyenv). To install on OS X:

  ```
  brew update
  brew install pyenv
  ```

  This project was built using Python 3.9.1. We will install and manage this with pyenv:

  ```
  pyenv install 3.9.1
  ```

  This version is referenced in the `.python-version` file so it should be used automatically.

- [Poetry](https://python-poetry.org/) is used as a dependency and package manager. This tool will
also manage our Python virtual environment to keep our dependencies contained. To install:

  ```
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  ```

  This should add poetry to your PATH but if not, follow the instructions found in command line upon installation


# Installation

Dependencies are specified within `pyproject.toml` file. To install, we use Poetry like this:

  ```
  poetry install
  ```

This will install all dependencies into a virtual environment managed by Poetry. We can enter this environment and execute commands within like this:

  ```
  poetry shell
  ```

# Developing

This app is utilizing [Flask](https://flask.palletsprojects.com/en/1.1.x/), a popular micro-web framework built in Python.

The app is configured with environment variables found in the `.env` file and we can start the server after installation like this:

  ```
  flask run
  ```

This will start the server at `http://localhost:5000`. If you navigate there, you should see the text "Hello World".

The code to do generate this view is in the hello module in `hello.py`.

This module defines a Flask blueprint at a root path

  ```
  from flask import Blueprint


  hello_bp = Blueprint('hello', __name__, url_prefix='/')
  ```

And then we use this blueprint to define our views:

  ```
  @hello_bp.route('/')
  def index() -> str:
    return "Hello World"
  ```

Blueprints are added to the main app in our root `__init__.py`.

# Linting

We are using [Flake8](https://flake8.pycqa.org/en/latest/) as our code linting. It is
installed with our main install as a dev dependency. To run it:

  ```
  flake8
  ```

Linting errors look like the following:

  ```
  ./python_sample_app/hello.py:9:25: W292 no newline at end of file
  ```

# Type Checking

Although Python is dynamically typed, it does support type hints, which is helpful for
enforcing proper interfaces. The type checker `mypy` is installed as a dev dependency
in Poetry. To run:

  ```
  mypy python_sample_app/
  ```

This will report any issues like this:

  ```
  python_sample_app/hello.py:9: error: Incompatible return value type (got "str", expected "int")
  ```

# Testing

There are two libraries that we are using to assist with testing. The first is `pytest`.
From the main project directory, we can run:

  ```
  pytest
  ```

This will run all tests defined in the `tests/` directory.

We can also analyze our code coverage using `coverage`:

  ```
  coverage run -m pytest
  ```

This will run `pytest` and create a coverage report which can be viewed like:

  ```
  coverage report
  ```
