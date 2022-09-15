-- install postgress
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

-- use admin user postgress to perform administrative tasks
sudo -u postgres psql

-- create database
CREATE DATABASE myproject;

-- create user
CREATE USER petsembi WITH PASSWORD '123456';

-- configure user settings so that you dont have to set them always
ALTER ROLE petsembi SET client_encoding TO 'utf8';
ALTER ROLE petsembi SET default_transaction_isolation TO 'read committed';
ALTER ROLE petsembi SET timezone TO 'UTC';

-- grand privileges
GRANT ALL PRIVILEGES ON DATABASE EmployeeDB TO petsembi;

--quit the interactive shell
\q




-- ADJUST DJANGO MAIN PROJECT SETTINGS FILE TO THE FOLLOWING (The projects part)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employeedb',
        'USER': 'petsembi',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '',

    }
}


-- in case the following error happens
django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: No module named 'psycopg2'


-- solve it using: 
pip install psycopg2-binary