import requests

TIME_URL = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
DIFFERENCE = 30


def check_time(value):
    try:
        value = int(value)
    except:
        return False

    response = requests.get(TIME_URL)
    if response.status_code == 200:
        time = response.json().get('unixtime')
        valid = abs(int(time) - int(value)) < DIFFERENCE
        print('valeu', value)
        return bool(valid)



response = requests.get(TIME_URL)
time = response.json().get('unixtime')
print(time)