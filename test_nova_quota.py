import random
import requests
import json


URL = 'http://james:8774/v2/'
AUTH_URL = 'http://james:35357/v2.0/tokens'
USER = 'admin'
PASS = 'admin'
TENANT = 'admin'
demo_user = 'b1fa50a718bc4a5999d34b73dba4092d'
demo_tenant = '2aaadeb0f0714d2c8ba5b1547c4afd68'
admin_tenant = '2c0490c4401949ad8e5677a15c433976'


def headers():
    headers = {'content-type': 'application/json'}
    payload = {"auth":
               {"tenantName": TENANT,
                "passwordCredentials":
                {"username": USER, "password": PASS}}}
    r = requests.post(AUTH_URL,
                      data=json.dumps(payload),
                      headers=headers)
    headers['x-auth-token'] = r.json()['access']['token']['id']
    return headers


def test_show_quotas_for_user():
    _headers = headers()
    r = requests.get(
        URL + 'os-quota-sets/%s?user_id=1&user_id=2' % demo_tenant,
        headers=_headers)
    assert 200 == r.status_code, r.text
