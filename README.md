### Time API

#### Описание

Использвался django-rest-framework для создания rest-api, SQLite в качестве БД

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
Время передается в формате Unix в body post-запроса в формате JSON. 

#### Авторизация
В заголовке запроса должен передаваться токен авторизации (base64 encode "username"+"password")

#### Проверка работоспособности

```shell script
curl -H "Authorization: token" http://127.0.0.1:8000/time
```
##### Пример запроса
```shell script
curl -H "Authorization:ZGF5OmRheQ==" http://127.0.0.1:8000/time?value=1607514830
```