import random
import requests
import json
from creds import *


def test_fail_if_no_tenant():
    _headers = headers()
    r = requests.post(
        CINDER_URL + 'os-quota-sets',
        headers=_headers)
    assert 404 == r.status_code


def test_fail_without_ADMIN_TENANT():
    _headers = headers()
    r = requests.get(
        CINDER_URL + 'os-quota-sets/%s' % DEMO_TENANT,
        headers=_headers)
    assert 404 == r.status_code, r.text


def test_show_quotas_for_user():
    _headers = headers()

    value1 = 50
    r = requests.put(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        json={
            "quota_set": {
                "volumes": value1
            }},
        headers=_headers)
    assert 200 == r.status_code
    value2 = 100
    r = requests.put(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
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
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        headers=_headers)
    assert value1 == r.json()['quota_set']['volumes']
    r = requests.get(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        headers=_headers, params={'user_id': 1})
    # get request with user_id just returns quotas for tenant
    assert value1 == r.json()['quota_set']['volumes']


def test_show_details():
    _headers = headers()
    r = requests.get(
        CINDER_URL + '%s/os-quota-sets/%s/detail' % (ADMIN_TENANT, DEMO_TENANT),
        headers=_headers)
    assert 404 == r.status_code, r.text
    r = requests.get(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        headers=_headers)
    assert 200 == r.status_code, r.text
    default = r
    r = requests.get(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
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
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        json={
            "quota_set": {
                "volumes": value
            }},
        headers=_headers)
    assert 200 == r.status_code, r.text
    assert value == r.json()['quota_set']['volumes']
    r = requests.get(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        headers=_headers)
    assert 200 == r.status_code
    assert value == r.json()['quota_set']['volumes']


def test_fail_on_unknown_quota():
    _headers = headers()
    r = requests.put(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
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
        CINDER_URL + '%s/os-quota-sets/defaults' % (ADMIN_TENANT,),
        headers=_headers)
    assert 200 == r.status_code, r.text
    assert 'volumes' in r.json()['quota_set']
    print r.json()


def test_delete():
    _headers = headers()
    r = requests.delete(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        headers=_headers)
    assert 200 == r.status_code, r.text
    value = 10 # default values for volumes
    r = requests.get(
        CINDER_URL + '%s/os-quota-sets/%s' % (ADMIN_TENANT, DEMO_TENANT),
        headers=_headers)
    assert 200 == r.status_code, r.text
    assert value == r.json()['quota_set']['volumes']
