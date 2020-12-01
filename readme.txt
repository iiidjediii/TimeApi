Описание
Использвался django-rest-framework для создания rest-api, SQlite в качестве БД

Предварительно:
pip install Django
pip install django-rest-framework
python manage.py runserver - запускаем локальный сервер

http://127.0.0.1:8000/admin - адмика
http://127.0.0.1:8000/home/ - точка входа в апи


Устанавливаем переменную окружения:
cmd:
set MYAPI_CORE_AUTH_TOKEN=value

curl -H "token:value" http://127.0.0.1:8000/hello/ - проверка подходит ли токен
