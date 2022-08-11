Финальный проект, для IT Academy

Во первых склонте проект

git clone https://github.com/Ridzen/globusconsalting.git

Установите и активируйте виртуальное окружение

sudo apt install python3-venv python3 -m venv venv source venv/bin/activate

Установите все библиотеки

pip install -r req.txt

Создайте файл settings.ini на уровне собственного проекта, скопируйте его под текст и добавьте свое значение:

[SYSTEM] DJANGO_KEY=key DJANGO_DEBUG=True or False HOST=localhost:8000 or host

[DATABASE] DATABASE_PASSWORD=password DATABASE_USER=user DATABASE_NAME=dbname DATABASE_HOST=localhost or host DATABASE_PORT=5432 or host-port

Этот проект работает на Postgresql, поэтому установите его:

sudo apt-get update sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / sudo apt-get install postgresql postgresql-contrib (Ubuntu) sudo -u postgres psql

Введите свой postgresql и создайте базу данных:

sudo -u postgres psql CREATE DATABASE ; CREATE USER WITH PASSWORD 'your_super_secret_password'; ALTER ROLE SET client_encoding TO 'utf8'; ALTER ROLE SET default_transaction_isolation TO 'read committed'; ALTER ROLE SET timezone TO 'UTC'; GRANT ALL PRIVILEGES ON DATABASE TO '';

Синхронизируйте базу данных с Django:

    python manage.py makemigrations
    python manage.py migrate

Создать суперпользователя

    python manage.py createsuperuser

И, наконец, запустите проект:

    python manage.py runserver
