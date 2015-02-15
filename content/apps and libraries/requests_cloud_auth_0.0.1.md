Title: Requests-Cloud-Auth - Simple cloud auth extensions
Date: 2015-2-15
Modified: 2015-2-15 15:07
Tags: Python, PyPI, Library, Requests, Cloud, Authentication
Slug: requests-cloud-auth-0.0.1
Authors: John Vrbanac

If you're like me, you've run into the situation where you want to interface
with your cloud resources, but you don't want to use the official clients due
to the number of dependencies it would introduce into your project. This is
where the requests-cloud-auth library comes in. You can make the one or two
cloud API calls you need without incurring the expense of heavy cloud clients.

Requests-Cloud-Auth is a simple collection of extensions for the Requests
library that will do the work of authenticating, caching tokens, and adding
header information to your HTTP requests. Currently, the library only supports
Keystone V2 and Rackspace Cloud; however, in the future I plan on including
support for Keystone V3, HP Cloud, Digital Ocean, and other cloud providers as
people request them.

Example:
--------

```python
import requests
from requests_cloud_auth import rackspace

auth = rackspace.RackspacePasswordAuth(
    username='my_user',
    password='my_pass'
)

# Pre-auth as we need our project_id to list our cloud servers
auth.authenticate()

url = 'https://ord.servers.api.rackspacecloud.com/v2/{0}/servers'.format(auth.project_id)
resp = requests.get(url, auth=auth)
```


Installation:
--------------

```shell
pip install requests-cloud-auth
```

Project Links:
----------------

* GitHub: [jmvrbanac/requests-cloud-auth](https://github.com/jmvrbanac/requests-cloud-auth)
* PyPI: [requests-cloud-auth](https://pypi.python.org/pypi/requests-cloud-auth)
* Documentation: [![Documentation Status](https://readthedocs.org/projects/requests-cloud-auth/badge/?version=latest)](http://requests-cloud-auth.readthedocs.org)
* Travis CI: [![Build Status](https://travis-ci.org/jmvrbanac/requests-cloud-auth.svg?branch=master)](https://travis-ci.org/jmvrbanac/requests-cloud-auth)
