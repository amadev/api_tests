import uuid
import random
import requests
import json
from creds import *
from requests_toolbelt.utils import dump


class PlacementClient(object):

    KEYWORDS = [
        'resource_classes',
        'resource_providers',
        'inventories',
        'usages',
        'aggregates'
        'allocations'
    ]

    def __init__(self, url=PL_URL[0:-1]):
        self.url = url

    def __getattr__(self, name):
        if name in ['get', 'post', 'put', 'delete']:
            return lambda *args, **kwargs: self.call(name, *args, **kwargs)
        elif name in self.KEYWORDS:
            return PlacementClient(self.url + '/' + name)
        else:
            raise RuntimeError('unknown keyword %s' % name)

    def __call__(self, *args):
        params = [self.url]
        params.extend(args)
        return PlacementClient('/'.join(params))

    def call(self, method, *args, **kwargs):
        _headers = headers()
        print 'calling url', self.url
        status_code = kwargs.pop('status_code', 200)
        r = getattr(requests, method)(
            self.url, headers=_headers, *args, **kwargs)
        assert status_code == r.status_code, r.text
        print dump.dump_all(r)
        if not r.text:
            return {}
        return r.json()


PLC = PlacementClient()


def get_resource_providers_uuids():
    r = PLC.resource_providers().get()
    return [rp['uuid'] for rp in r['resource_providers']]


RPS = get_resource_providers_uuids()
RP_UUID = RPS[0]
RP_UUID_NEW = '92637880-2d79-43c6-afab-d860886c6391'


def test_get_version():
    _headers = headers()
    r = requests.get(PL_URL, headers=_headers)
    print r.json()
    assert 200 == r.status_code, r.text


def test_get_resource_providers():
    _headers = headers()
    r = requests.get(PL_URL + 'resource_providers', headers=_headers)
    print r.json()
    assert 200 == r.status_code, r.text


def test_create_resource_providers():
    PLC.resource_providers().post(json={'name': 'Ceph Storage Pool'},
                                  status_code=201)
    id = str(uuid.uuid4())
    PLC.resource_providers().post(json={'name': 'NFS Share',
                                        'uuid': id},
                                  status_code=201)
    new = set(get_resource_providers_uuids()) - set(RPS)
    PLC.resource_providers(list(new)[0]).get()
    PLC.resource_providers(list(new)[0]).put(json={'name': 'Shared storage'})

    assert 2 == len(new)
    for id in new:
        PLC.resource_providers(id).delete(status_code=204)

def test_get_inventories():
    _headers = headers()
    r = requests.get(
        PL_URL + 'resource_providers/' + RP_UUID + '/inventories',
        headers=_headers)
    print r.json()
    assert 200 == r.status_code, r.text


def test_get_inventories():
    _headers = headers()
    r = requests.get(
        PL_URL + 'resource_providers/' + RP_UUID + '/inventories',
        headers=_headers)
    print dump.dump_all(r)
    assert 200 == r.status_code, r.text


def test_create_inventory_fail():
    _headers = headers()
    r = requests.post(
        PL_URL + 'resource_providers/1/inventories',
        headers=_headers)
    assert 404 == r.status_code, r.text
    r = requests.post(
        PL_URL + 'resource_providers/' + RP_UUID + '/inventories',
        headers=_headers)
    # no json
    assert 400 == r.status_code, r.text
    r = requests.post(
        PL_URL + 'resource_providers/' + RP_UUID + '/inventories',
        headers=_headers,
        json={
            "resource_provider_generation": 1,
            "resource_class": "DISK_GB",
            "allocation_ratio": 1.0,
            "max_unit": 35,
            "min_unit": 1,
            "reserved": 0,
            "step_size": 1,
            "total": 35
        })
    # duplicate disk_gb
    assert 409 == r.status_code, r.text


def test_create_inventory():
    _headers = headers()
    # create new resource provider
    r = requests.post(
        PL_URL + 'resource_providers',
        headers=_headers,
        json={
            "name": "Global NFS share",
            "uuid": RP_UUID_NEW
        }
    )
    assert 201 == r.status_code, r.text
    # create inventory
    r = requests.post(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=_headers,
        json={
            "resource_class": "PCI_DEVICE",
            "allocation_ratio": 1.0,
            "max_unit": 35,
            "min_unit": 1,
            "reserved": 0,
            "step_size": 1,
            "total": 35
        })
    assert 201 == r.status_code, r.text
    # delete inventoriy
    r = requests.delete(
        PL_URL + 'resource_providers/' + RP_UUID_NEW +
        '/inventories/PCI_DEVICE',
        headers=_headers)
    assert 204 == r.status_code, r.text
    # delete resource provider
    r = requests.delete(
        PL_URL + 'resource_providers/' + RP_UUID_NEW,
        headers=_headers,
        json={
            "resource_provider_generation": 1,
        })
    assert 204 == r.status_code, r.text


def test_generation_conflict():
    _headers = headers()
    r = requests.post(
        PL_URL + 'resource_providers',
        headers=_headers,
        json={
            "name": "Global NFS share",
            "uuid": RP_UUID_NEW
        }
    )
    assert 201 == r.status_code, r.text
    r = requests.put(
        PL_URL + 'resource_providers/' + RP_UUID_NEW,
        headers=_headers,
        json={
            "name": "Global NFS share 2",
        }
    )
    assert 200 == r.status_code, r.text
    # default generation is 0, update didn't change it
    assert r.json()['generation'] == 0
    # create inventory
    r = requests.post(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=_headers,
        json={
            "resource_class": "PCI_DEVICE",
            "allocation_ratio": 1.0,
            "max_unit": 35,
            "min_unit": 1,
            "reserved": 0,
            "step_size": 1,
            "total": 35
        })
    assert 201 == r.status_code, r.text
    assert r.json()['resource_provider_generation'] == 1
    # update inventory
    r = requests.put(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=_headers,
        json={
            'resource_provider_generation': 1,
            'inventories': {
                "VCPU": {
                    "allocation_ratio": 10.0,
                    "reserved": 2,
                    "total": 64
                },
                "MEMORY_MB": {
                    "allocation_ratio": 2.0,
                    "step_size": 4,
                    "max_unit": 16,
                    "total": 128
                }
            }
        })
    print dump.dump_all(r)
    assert 200 == r.status_code, r.text
    assert r.json()['resource_provider_generation'] == 2
    # update inventory with previous generation should fail
    r = requests.put(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=_headers,
        json={
            'resource_provider_generation': 1,
            'inventories': {
                "PCI_DEVICE": {
                    "allocation_ratio": 1.0,
                    "max_unit": 35,
                    "min_unit": 1,
                    "reserved": 0,
                    "step_size": 1,
                    "total": 41
                }
            }
        })
    assert 409 == r.status_code, r.text

    r = requests.delete(
        PL_URL + 'resource_providers/' + RP_UUID_NEW,
        headers=_headers)
    # print dump.dump_all(r)
    assert 204 == r.status_code, r.text


def test_delete_one():
    _headers = headers()
    # create new resource provider
    r = requests.post(
        PL_URL + 'resource_providers',
        headers=_headers,
        json={
            "name": "Global NFS share",
            "uuid": RP_UUID_NEW
        }
    )
    assert 201 == r.status_code, r.text
    # create inventory
    r = requests.post(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=_headers,
        json={
            "resource_class": "PCI_DEVICE",
            "allocation_ratio": 1.0,
            "max_unit": 35,
            "min_unit": 1,
            "reserved": 0,
            "step_size": 1,
            "total": 35
        })
    assert 201 == r.status_code, r.text
    # create inventory
    r = requests.post(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=_headers,
        json={
            "resource_class": "SRIOV_NET_VF",
            "allocation_ratio": 1.0,
            "max_unit": 35,
            "min_unit": 1,
            "reserved": 0,
            "step_size": 1,
            "total": 35
        })
    assert 201 == r.status_code, r.text
    # delete inventoriy
    r = requests.delete(
        PL_URL + 'resource_providers/' +
        RP_UUID_NEW + '/inventories/PCI_DEVICE',
        headers=_headers)
    assert 204 == r.status_code, r.text
    # request with resource class specification deletes that class only
    _headers = headers()
    r = requests.get(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=_headers)
    assert 200 == r.status_code, r.text
    assert 1 == len(r.json()['inventories'].keys()), r.json()
    # delete all inventories
    delete_headers = _headers.copy()
    delete_headers.update({'OpenStack-API-Version': 'placement 1.5'})
    r = requests.delete(
        PL_URL + 'resource_providers/' + RP_UUID_NEW + '/inventories',
        headers=delete_headers)
    print dump.dump_all(r)
    assert 204 == r.status_code, r.text
    # delete resource provider
    r = requests.delete(
        PL_URL + 'resource_providers/' + RP_UUID_NEW,
        headers=_headers)
    assert 204 == r.status_code, r.text


def test_get_resource_classes():
    _headers = headers()
    # create new resource provider
    r = requests.get(
        PL_URL + 'resource_classes/DISK_GB',
        headers=_headers,
    )
    print dump.dump_all(r)
    # because of empty nova_api.resource_classes
    assert 404 == r.status_code, r.text


def test_get_inventory_by_class():
    PLC.resource_providers(RP_UUID).inventories('VCPU').get()


def test_update_inventory_by_class():
    generation = PLC.resource_providers(RP_UUID).get()['generation']
    PLC.resource_providers(RP_UUID).inventories('DISK_GB').put(
        json={
            'resource_provider_generation': generation,
            'total': 50})


def test_client():
    p = PLC.resource_providers(RP_UUID)
    assert PL_URL + 'resource_providers/' + RP_UUID == p.url, p.url
    p = PLC.resource_providers(RP_UUID).inventories()
    assert PL_URL + 'resource_providers/' + \
        RP_UUID + '/inventories' == p.url, p.url
    p = PLC.resource_providers()
    assert PL_URL + 'resource_providers'
    p = PLC.resource_providers().inventories()
    assert PL_URL + 'resource_providers/inventories'
    func = PLC.resource_providers().get
    assert RP_UUID == PLC.resource_providers().\
        get()['resource_providers'][0]['uuid']
