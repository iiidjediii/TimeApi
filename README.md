### Time API

#### Описание

Использвался django-rest-framework для создания rest-api

#### Установка

```shell script
pip install -r requirements.txt
```

#### Запуск

```shell script

python manage.py migrate

# start server
python manage.py runserver
```

#### Проверка времени
Доступен post-запрос к конечной точке http://127.0.0.1:8000/time.
В теле запроса передается время в формате Unix
```example
{
    "value":1608100094
}
```

#### Авторизация
В заголовке запроса должен передаваться токен авторизации (base64 encode "username"+"password")

#### Проверка работоспособности

```shell script
curl --location --request POST 'http://127.0.0.1:8000/time' \
--header 'Authorization: ZGF5OmRheQ==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "value":1608116916
}'
```
##### Для проверки работоспособности использовался Postman с вышеуказанными параметрами запроса.
###### Изначально предполагается создание суперпользователя:

```shell script
python manage.py createsuperuser
```
###### Создание пользователей через панель администратора:

```shell script
http://127.0.0.1:8000/admin
```
После этого раскомментировать строку 'core.middleware.token_check_middleware' в settings (middleware), после чего каждый запрос будет проверяться на токен авторизации.