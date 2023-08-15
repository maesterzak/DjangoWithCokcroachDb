# CockroachDB With Django Template

This project provides a simple and ready-to-use Django template with pre-configured settings for integrating CockroachDB into your Django projects.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction


Jumpstart your Django project with a hassle-free integration of CockroachDB as the database backend. This template leverages essential packages such as django-cockroachdb, dj_database_url, python-dotenv, and psycopg2-binary to streamline your development process.



## Installation

Follow these steps to clone and set up the project:

* Clone the repository
```bash
git clone https://github.com/maesterzak/DjangoWithCokcroachDb.git

```
* Navigate to the project directory:
```bash
cd DjangoWithCokcroachDb
```
* Create a virtual environment for the project:
```bash
python -m venv venv
```

* Activate the virtual environment
```bash
./venv/scripts/activate
```

* Install the required packages
```bash
pip install -r requirements.txt
```
* Create a .env file in the project root and add the following environment variables along with your specific values. Sample is shown below:
```bash
SECRET_KEY = 'django-insecure-cqt2xivnlsaw16#13^gm+hmametr4)@he3c%szn2*$+051ud#d'

DATABASE_URL = "postgresql://abubakar:DeSHPI662SggOf7cUxcLtA@glum-dxggy-9683.8nj.cockroachlabs.cloud:26257/defaultdb?sslmode=require"
```
* Apply migrations to the database:
```bash
$ python manage.py makemigrations
```
* Migrate the database
```bash
$ python manage.py migrate
```

Feel free to create an issue on github if you run into any problems


## Usage
Once the installation steps are complete, you can start building your Django application on top of the pre-configured CockroachDB setup. Leverage the power of CockroachDB's scalability and reliability for your project's database needs.

## Contributing
We welcome contributions from the community! If you have any improvements, suggestions, or bug fixes, please don't hesitate to submit a pull request or open an issue.

<!-- This project is licensed under the MIT License. -->

