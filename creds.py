import requests
import json
from requests_toolbelt.utils import dump


HOST = 'james'

CINDER_URL = 'http://%s:8776/v3/' % HOST
NOVA_URL = 'http://%s:8774/v2.1/' % HOST
AUTH_URL = 'http://%s/identity/v2.0/tokens' % HOST
PL_URL = 'http://%s/placement/' % HOST

USER = 'admin'
PASS = 'admin'
TENANT = 'admin'
DEMO_USER = '142c8f51c05a4e9592f050d6d82e1f72'
DEMO_TENANT = 'dd4b5e19a0e74bfb8a043744c6bf4318'
ADMIN_TENANT = '26e9ece758dd449b96fff2e65fb48299'


def headers():
    headers = {'content-type': 'application/json'}
    payload = {"auth":
               {"tenantName": TENANT,
                "passwordCredentials":
                {"username": USER, "password": PASS}}}
    r = requests.post(AUTH_URL,
                      data=json.dumps(payload),
                      headers=headers)
    print dump.dump_all(r)
    headers['x-auth-token'] = r.json()['access']['token']['id']
    return headers
