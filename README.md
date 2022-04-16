<div align="center">
   <a href="https://github.com/alura-challenges/challenge-back-end">
    <img  src="https://raw.githubusercontent.com/luigiMinardi/alurachallenge-backend/7a2de4fd13d827d8b5bbde9a77d5a42e380cc25f/.github/challenges-logo.svg" alt="Alura Challenges" width="160px">
  </a>
</div>
<p align="center">
  <a href="#installing">Installing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#running-tests">Testing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#documantation-of-the-api">Documantation</a>
</p>
<div align="center">
  <a href="https://github.com/alura-challenges/challenge-back-end">
    <img alt="Alura Challenge Github" src="https://img.shields.io/badge/Alura-Challenge-%2300C86F">
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://www.django-rest-framework.org/#requirements">
    <img alt="PyPI - Django Version" src="https://img.shields.io/pypi/djversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://github.com/luigiMinardi/alurachallenge-backend/blob/main/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/badge/license-MIT-%2300C86F">
  </a>
  <a href="https://pypi.org/project/djangorestframework/">
    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/djangorestframework">
  </a>
</div>

# Installing

* First things first, clone the repository:

  ```bash
  git clone https://github.com/luigiMinardi/alurachallenge-backend-2
  ```

* Then create a [Virtual Enviroment](https://outline.com/HaJ3zA) for you:

  ```bash
  python -m venv .venv
  ```
  
* Activate Your `venv`:

  Mac/Linux:
  ```bash
  source .venv/bin/activate 
  ```
  Windows:
  ```cmd
  .venv\Scripts\activate.bat
  ```

* Install all the requirements:

  ```bash
  pip install -r requirements.txt
  ```

* Make the Migrations:

  ```bash
  python manage.py makemigrations
  ```

* Run the DataBase Migration:

  ```bash
  python manage.py migrate
  ```

* Create a Super User:
  ```bash
  python manage.py createsuperuser
  ```

* Run your server:

  ```bash
  python manage.py runserver
  ```

Now you are ready to use it.


# Running Tests

For run our automated tests do:

```bash
python manage.py test
```

# Documantation of the API

<div align="center">

## --- WIP ---
</div>