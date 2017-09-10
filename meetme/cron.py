import requests


def my_scheduled_job():
    url = "https://meetme-gemastik.herokuapp.com/"
    req = requests.get(url)