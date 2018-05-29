import requests
import json
from requests_toolbelt.utils import dump


HOST = 'james'

CINDER_URL = 'http://%s:8776/v3/' % HOST
NOVA_URL = 'http://%s/compute/v2.1/' % HOST
AUTH_URL = 'http://%s/identity/v2.0/tokens' % HOST
PL_URL = 'http://%s/placement/' % HOST

USER = 'admin'
PASS = 'admin'
TENANT = 'admin'
DEMO_USER = 'demo'
DEMO_PASS = 'admin'
DEMO_TENANT = 'demo'
TENANT_ID = '475bd22e5d3949a08a59a9fdb19850f5'
DEMO_TENANT_ID = '7b45e6344a874fb8986294a255aea17c'


def headers(user=None, pswd=None, tenant=None):
    user = user or USER
    pswd = pswd or PASS
    tenant = tenant or TENANT
    headers = {'content-type': 'application/json'}
    payload = {"auth":
               {"tenantName": tenant,
                "passwordCredentials":
                {"username": user, "password": pswd}}}
    r = requests.post(AUTH_URL,
                      data=json.dumps(payload),
                      headers=headers)
    print dump.dump_all(r)
    headers['x-auth-token'] = r.json()['access']['token']['id']
    return headers


class Client(object):

    def __init__(self, url=PL_URL[0:-1], keywords=None, convert_names=False,
                 user=None, pswd=None, tenant=None):
        self.url = url
        self.keywords = keywords or []
        self.convert_names = convert_names
        self.user = user
        self.pswd = pswd
        self.tenant = tenant

    def __getattr__(self, name):
        if self.convert_names:
            name = name.replace('_', '-')
        if name in ['get', 'post', 'put', 'delete']:
            return lambda *args, **kwargs: self.call(name, *args, **kwargs)
        elif not self.keywords or name in self.keywords:
            return Client(self.url + '/' + name,
                          keywords=self.keywords,
                          convert_names=self.convert_names,
                          user=self.user,
                          pswd=self.pswd,
                          tenant=self.tenant)
        else:
            raise RuntimeError('unknown keyword %s' % name)

    def __call__(self, *args):
        params = [self.url]
        params.extend(args)
        return Client('/'.join(params),
                      keywords=self.keywords,
                      convert_names=self.convert_names,
                      user=self.user,
                      pswd=self.pswd,
                      tenant=self.tenant)

    def call(self, method, *args, **kwargs):
        _headers = headers(self.user, self.pswd, self.tenant)
        print 'calling url %s for user  %s' % (self.url, self.user)
        status_code = kwargs.pop('status_code', 200)
        version = kwargs.pop('version', None)
        if version:
            _headers.update(
                {'OpenStack-API-Version': 'placement %s' % version})
        r = getattr(requests, method)(
            self.url, headers=_headers, *args, **kwargs)
        print dump.dump_all(r)
        assert status_code == r.status_code, r.text
        if not r.text:
            return {}
        return r.json()
