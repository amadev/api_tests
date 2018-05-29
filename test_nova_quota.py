import random
import requests
import json
from creds import *

# C = Client(
#     NOVA_URL[0:-1],
#     convert_names=True)


# def test_show_quotas_for_user():
#     _headers = headers()
#     r = requests.get(
#         NOVA_URL + 'os-quota-sets/%s?user_id=1&user_id=2' % DEMO_TENANT_ID,
#         headers=_headers)
#     assert 200 == r.status_code, r.text


def test_get_quota_details():
    # C.os_quota_sets(DEMO_TENANT_ID).detail().get()
    c = Client(
        NOVA_URL[0:-1],
        convert_names=True,
        user=DEMO_USER,
        pswd=DEMO_PASS,
        tenant=DEMO_TENANT)
    # c.os_quota_sets(DEMO_TENANT_ID).detail().get(status_code=403)
    # C.limits().get()
    c.limits().get()
