import random
import requests
import json
from creds import *


def test_server_details():
    _headers = headers()

    r = requests.get(
        NOVA_URL + '/servers/detail?system_metadata={"foo":"bar"}',
        headers=_headers)
    assert 400 == r.status_code, r.text
    assert 'system_metadata' in r.json()['badRequest']['message']
