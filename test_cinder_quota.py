import random
import requests
import json


URL = 'http://james:8776/v3/'
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


def test_fail_if_no_tenant():
    _headers = headers()
    r = requests.post(
        URL + 'os-quota-sets',
        headers=_headers)
    assert 404 == r.status_code


def test_fail_without_admin_tenant():
    _headers = headers()
    r = requests.get(
        URL + 'os-quota-sets/%s' % demo_tenant,
        headers=_headers)
    assert 404 == r.status_code, r.text


def test_show_quotas_for_user():
    _headers = headers()

    value1 = 50
    r = requests.put(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        json={
            "quota_set": {
                "volumes": value1
            }},
        headers=_headers)
    assert 200 == r.status_code
    value2 = 100
    r = requests.put(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        json={
            "quota_set": {
                "user_id": 1,
                "volumes": value2
            }},
        headers=_headers)
    # put request for user is failed due user_id
    assert 400 == r.status_code, r.text
    assert 'Bad key' in r.json()['badRequest']['message']
    r = requests.get(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        headers=_headers)
    assert value1 == r.json()['quota_set']['volumes']
    r = requests.get(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        headers=_headers, params={'user_id': 1})
    # get request with user_id just returns quotas for tenant
    assert value1 == r.json()['quota_set']['volumes']


def test_show_details():
    _headers = headers()
    r = requests.get(
        URL + '%s/os-quota-sets/%s/detail' % (admin_tenant, demo_tenant),
        headers=_headers)
    assert 404 == r.status_code, r.text
    r = requests.get(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        headers=_headers)
    assert 200 == r.status_code, r.text
    default = r
    r = requests.get(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        headers=_headers, params={'usage': True})
    assert 200 == r.status_code, r.text
    for i in r.json()['quota_set']:
        if i == 'id':
            assert default.json()['quota_set'][i] == r.json()['quota_set'][i]
            continue
        assert default.json()['quota_set'][i] == r.json()['quota_set'][i]['limit']


def test_set_quota_for_tenant():
    value = random.randint(1, 100)
    _headers = headers()
    r = requests.put(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        json={
            "quota_set": {
                "volumes": value
            }},
        headers=_headers)
    assert 200 == r.status_code, r.text
    assert value == r.json()['quota_set']['volumes']
    r = requests.get(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        headers=_headers)
    assert 200 == r.status_code
    assert value == r.json()['quota_set']['volumes']


def test_fail_on_unknown_quota():
    _headers = headers()
    r = requests.put(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        json={
            "quota_set": {
                "volumes101": 10
            }},
        headers=_headers)
    assert 400 == r.status_code, r.text
    assert 'Bad key' in r.json()['badRequest']['message']


def test_show_defaults():
    _headers = headers()
    r = requests.get(
        URL + '%s/os-quota-sets/defaults' % (admin_tenant,),
        headers=_headers)
    assert 200 == r.status_code, r.text
    assert 'volumes' in r.json()['quota_set']


def test_delete():
    _headers = headers()
    r = requests.delete(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        headers=_headers)
    assert 200 == r.status_code, r.text
    value = 10 # default values for volumes
    r = requests.get(
        URL + '%s/os-quota-sets/%s' % (admin_tenant, demo_tenant),
        headers=_headers)
    assert 200 == r.status_code, r.text
    assert value == r.json()['quota_set']['volumes']
