# PYTHON - DJANGO Full Stack Guide

## Installation

- Install python 3.7
- Install pip latest `python -m pip install --upgrade pip`

---

## Virtual Environments

Using VENV (Windows)

- Create new environment `$ python -m venv [project_env]`
- Activate environment `$ project_env\Scripts\activate.bat`
- Validate checking installed packages `$ pip list`
- Save current dependencies version to file `$ pip freeze`
- Deactivate environment `$ deactivate`
- Delete environment `$ rmdir project_env /s`
- Install dependencies from file `$ pip install -r [requirements_file.txt]`
- Create virtual environment with access to system dependencies (globally installed) `$ python -m venv venv --system-site-packages`
- List packages installed only in environment `$ pip list --local`

Using VENV (Linux/Mac)

- Create new environment `$ python -m venv project_env`
- Activate environment `$ source project_env/bin/activate`
- Check python environment version `$ which python`
- Validate installed packages `$ pip list`
- Install packages `$ pip install [package]`
- Save current dependencies version to file `$ pip freeze > requirements.txt`
- Install dependencies from file `$ pip install -r [requirements_file.txt]`
- Deactivate environment `$ deactivate`
- Delete environment `$ rm -rf project_env`

### \* Never commit the virtual environment folder, only the dependencies versions file

---

## Django

List installed packages

`$ pip list`

Install environments manager

`$ pip3 install pipenv`

Create environments

`$ sudo -H pip install -U pipenv`

Create Django project

`$ django-admin startproject pollster`

Run dev server

`$ python manage.py runserver [port]`

Run migrations

`$ python manage.py migrate`

Create a new app

`$ python manage.py startapp polls`

Run interactive Shell

`$ python manage.py shell`

Add super user

`$ python manage.py createsuperuser`

---

### Attention

In case the code editor does not detect packages, open the code editor settings and set the python interpreter to the one in the environment previously created

First, select the File (Code on macOS) > Preferences > Settings menu command (Ctrl+,) to open your Settings, select Workspace

Then do any of the following steps:

1. Create or modify an entry for python.pythonPath with the full path to the Python executable (if you edit settings.json directly, add the line below as the setting):

For example:

- Windows:

`"python.pythonPath": "c:/python36/python.exe",`

- macOS/Linux:

`"python.pythonPath": "/home/python36/python",`

1. You can also use python.pythonPath to point to a virtual environment, for example:

- Windows:

`"python.pythonPath": "c:/dev/ala/venv/Scripts/python.exe",`

- macOS/Linux:

`"python.pythonPath": "/home/abc/dev/ala/venv/bin/python",`

You can use an environment variable in the path setting using the syntax \${env:VARIABLE}. For example, if you've created a variable named PYTHON_INSTALL_LOC with a path to an interpreter, you can then use the following setting value:

`"python.pythonPath": "${env:PYTHON_INSTALL_LOC}",`

#### \*Always make sure no line break is added to the .json file

```json
{
  "python.pythonPath": "~\\Documents\\SoftwareProjcts\\Python-Django\\Python-Django\\venv\\Scripts\\python.exe"
}
```

#### External references

- [Environments in VSCode]('https://code.visualstudio.com/docs/python/environments')

---

# Introduction to Python

Welcome to Stack Builders' introduction to Python. After this training you will be able to start coding with Python.

This course is for version 3 of the Python programming language. It’s recommended to use the latest available.

## Resources

- The Scientist & the Engineer ([keynote video](https://www.youtube.com/watch?v=862xL6jm_PQ))
- [Python style guide](http://google.github.io/styleguide/pyguide.html)
- [Clean code with Python](https://github.com/zedr/clean-code-python)
- [Type Annotations with Python](https://www.stackbuilders.com/tutorials/python/using-types-in-python-with-mypy/)
- [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)

## Syllabus

All threads can be executed in parallel (pun intended).

| [Thread 1](threads/1.md) | [Thread 2](threads/2.md)   | [Thread 3](threads/3.md) |
| ------------------------ | -------------------------- | ------------------------ |
| Background               | Basics and primitive types | Software Design          |
| Setup                    | Known structures           | Functional Programming   |
| Python for the web       | Being pythonic             | Packaging and OOS        |
| Toolkit                  | Testing                    | Paralellism              |

[START!](threads/1.md)
