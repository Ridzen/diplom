Финальный проект, для IT Academy

Во первых склонте проект

git clone https://github.com/Ridzen/diplom/tree/main

Установите и активируйте виртуальное окружение

sudo apt install python3-venv python3 -m venv venv source venv/bin/activate

Установите все библиотеки

pip install -r req.txt

Создайте файл settings.ini на уровне собственного проекта, скопируйте его под текст и добавьте свое значение:

[SYSTEM] DJANGO_KEY=key DJANGO_DEBUG=True or False HOST=localhost:8000

[DATABASE] DATABASE_PASSWORD=password DATABASE_USER=user DATABASE_NAME=dbname DATABASE_HOST=localhost or host DATABASE_PORT=5432 or host-port


Синхронизируйте базу данных с Django:

    python manage.py makemigrations
    python manage.py migrate

Создать суперпользователя

    python manage.py createsuperuser

И, наконец, запустите проект:

    python manage.py runserver
____________________________________________________________________________________________

Изначальная идея проекта была улучшить текущий сайт mlbb.com, но сейчас мы стараемся сделать его лучше. В будущем планирую продолжать доработку этого проекта увеличивая его функционал и CRM систему. 

Текущий проект обладает:
CRUD Героев, и его скиллами
СRUD Категорий Героев
