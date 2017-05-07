import random
import requests
import json
from creds import *
from requests_toolbelt.utils import dump


VERSION = '2.42'


def test_server_details():
    _headers = headers()
    r = requests.get(
        NOVA_URL + '/servers/detail?system_metadata={"foo":"bar"}',
        headers=_headers)
    assert 400 == r.status_code, r.text
    assert 'system_metadata' in r.json()['badRequest']['message']


def test_add_tags():
    _headers = headers()
    _headers.update({'X-OpenStack-Nova-API-Version': '2.42'})

    r = requests.get(
        NOVA_URL + 'servers/detail',
        headers=_headers)
    assert 200 == r.status_code, r.text
    instances = r.json()['servers']
    assert len(instances) > 0
    assert instances[0]['tags'] == []

    r = requests.put(
        NOVA_URL + 'servers/' + instances[0]['id'] + '/tags',
        headers=_headers,
        json={"tags": ['foo', 'baz', 'qux']})
    print dump.dump_all(r)
    assert 200 == r.status_code, r.text

    r = requests.get(
        NOVA_URL + 'servers/detail',
        headers=_headers)
    assert 200 == r.status_code, r.text
    instances = r.json()['servers']
    assert len(instances) > 0
    assert set(instances[0]['tags']) == set(['foo', 'baz', 'qux'])

    r = requests.delete(
        NOVA_URL + 'servers/' + instances[0]['id'] + '/tags',
        headers=_headers)
    print dump.dump_all(r)
    assert 204 == r.status_code, r.text

    r = requests.get(
        NOVA_URL + 'servers/detail',
        headers=_headers)
    assert 200 == r.status_code, r.text
    instances = r.json()['servers']
    assert len(instances) > 0
    assert instances[0]['tags'] == []


def test_put_empty_tag():
    _headers = headers()
    _headers.update({'X-OpenStack-Nova-API-Version': '2.42'})

    r = requests.get(
        NOVA_URL + 'servers/detail',
        headers=_headers)
    assert 200 == r.status_code, r.text
    instances = r.json()['servers']
    assert len(instances) > 0
    assert instances[0]['tags'] == []

    r = requests.put(
        NOVA_URL + 'servers/' + instances[0]['id'] + '/tags',
        headers=_headers,
        json={"tags": ['   ']})
    print dump.dump_all(r)
    assert 200 == r.status_code, r.text

    r = requests.delete(
        NOVA_URL + 'servers/' + instances[0]['id'] + '/tags',
        headers=_headers)
    print dump.dump_all(r)
    assert 204 == r.status_code, r.text

    r = requests.put(
        NOVA_URL + 'servers/' + instances[0]['id'] + '/tags',
        headers=_headers,
        json={"tags": ['', 'abc']})
    print dump.dump_all(r)
    assert 200 == r.status_code, r.text


def test_os_hypervisors():
    _headers = headers()
    r = requests.get(
        NOVA_URL + 'os-hypervisors',
        headers=_headers)
    print dump.dump_all(r)
    assert 200 == r.status_code, r.text
    _headers = headers()
    r = requests.get(
        NOVA_URL + 'os-hypervisors/detail',
        headers=_headers)
    print dump.dump_all(r)
    assert 200 == r.status_code, r.text
