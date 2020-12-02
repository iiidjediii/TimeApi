import requests

TIME_URL = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
DIFFERENCE = 30


def check_time(value):
    try:
        value = int(value)
    except:
        return False

    response = requests.get(TIME_URL)
    if response.status_code != 200:
        return False

    time = response.json().get('unixtime')

    valid = abs(time - value) < DIFFERENCE

    return bool(valid)
