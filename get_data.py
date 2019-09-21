import time
import json
import requests

from urllib.parse import urlencode, quote

from _credentials import *

BASE_URL = "https://api.stackexchange.com/"
VERSION = "2.2"
HEADERS = {"X-API-Access-Token": access_token}
PARAMETERS = {"site": "stackoverflow", "team": "stackoverflow.com/c/comsc", "key": key}


def make_request_url(endpoint, params):
    return BASE_URL + VERSION + "/" + endpoint + "?" + urlencode(params)


def get_answers():
    endpoint = "answers"

    request_url = make_request_url(endpoint, PARAMETERS)

    r = requests.get(request_url, headers=HEADERS)
    with open("answers.%s.json" % (time.time()), "w") as outfile:
        json.dump(r.json(), outfile)


def get_questions():
    endpoint = "questions"

    request_url = make_request_url(endpoint, PARAMETERS)

    r = requests.get(request_url, headers=HEADERS)
    with open("questions.%s.json" % (time.time()), "w") as outfile:
        json.dump(r.json(), outfile)


def get_users():
    endpoint = "users"
    request_url = make_request_url(endpoint, PARAMETERS)

    r = requests.get(request_url, headers=HEADERS)
    with open("users.%s.json" % (time.time()), "w") as outfile:
        json.dump(r.json(), outfile)


def get_tags():

    endpoint = "tags"

    parameters = PARAMETERS.copy()

    parameters["sort"] = "popular"
    parameters["order"] = "desc"
    parameters["pagesize"] = "100"

    request_url = make_request_url(endpoint, parameters)

    r = requests.get(request_url, headers=HEADERS)
    with open("tags.%s.json" % (time.time()), "w") as outfile:
        json.dump(r.json(), outfile)


if __name__ == "__main__":
    get_tags()
    get_questions()
    get_answers()
    get_users()
