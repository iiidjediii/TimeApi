### Time API

#### Описание

Использвался django-rest-framework для создания rest-api, SQLite в качестве БД

#### Установка

```shell script
pip install -r requirements.txt
```

#### Запуск

```shell script
export MYAPI_CORE_AUTH_TOKEN=token

python manage.py migrate

# start server
python manage.py runserver
```


#### Проверка работоспособности

```shell script
curl -H "Authorization: Basic value" http://127.0.0.1:8000
```