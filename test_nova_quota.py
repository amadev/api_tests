import random
import requests
import json
from creds import *

def test_show_quotas_for_user():
    _headers = headers()
    r = requests.get(
        NOVA_URL + 'os-quota-sets/%s?user_id=1&user_id=2' % DEMO_TENANT,
        headers=_headers)
    assert 200 == r.status_code, r.text
