import requests
from rest_framework.exceptions import APIException

TIME_URL = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
DIFFERENCE = 50


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
        raise APIException('without connection internet')
    #
    if response.status_code == 200:
        time = response.json().get('unixtime')
        valid = abs(int(time) - int(value)) < DIFFERENCE
        print('value_utils', value)
        print('utils(apitime)', time)
        return bool(valid)


