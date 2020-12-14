from rest_framework.exceptions import APIException

import requests

TIME_URL = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
DIFFERENCE = 400


def check_time(value):
    # check that the time value is in the correct format
    try:
        value = int(value)
    except:
        return False
    # checking for server response existence
    try:
        response = requests.get(TIME_URL)
    except:
        return False

    if response.status_code == 200:
        time = response.json().get('unixtime')
        valid = abs(int(time) - int(value)) < DIFFERENCE
        print('utils(apitime)', time)
        return bool(valid)


