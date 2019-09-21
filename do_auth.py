import requests

from urllib.parse import urlencode, quote

from _credentials import *


def build_auth_url():

    base_url = "https://stackoverflow.com/"
    endpoint = "oauth"
    params = {
        "client_id": client_id,
        "redirect_uri": "http://cs.cf.ac.uk/",
        "scope": "no_expiry,access_team|stackoverflow.com/c/comsc",
    }

    auth_url = base_url + endpoint + "?" + urlencode(params, quote_via=quote)
    return auth_url


def do_auth():

    base_url = "https://stackoverflow.com/"
    endpoint = "oauth/access_token/json"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": "http://cs.cf.ac.uk/",
    }

    r = requests.post(base_url + endpoint, params)
    print(r.json())


if __name__ == "__main__":
    #
    # Run build_auth_url to put the url together. Copy this url into a browser,
    # auth the app, then copy the code from the address bar to the _credentials
    #

    # print(build_auth_url())

    #
    # Run do_auth and get the access_token. Store it in _credentials
    #

    print(do_auth())
    pass
