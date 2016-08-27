Title: Aumbry - Quick Configuration for Python Apps
Date: 2016-8-27
Modified: 2016-8-27 18:00
Tags: Python, PyPI, Library, Configuration, Consul
Slug: aumbry
Authors: John Vrbanac

One of the things that I've ran into a lot lately is having to write hookups
to fetch and deserialize configuration from multiple sources. Lately, a lot of
that is loading data from a file for local development and then loading from
Consul when the app is deployed.

There are a bunch of config libraries out there, so I was a bit hesitant to
write yet another config library. However, I really didn't find an existing
library that did what I need. What I needed was a library that could load
my configuration from either the disk or from some remote source such as Consul.
When it did load the config, I needed it to be in easy to access and test Python
object structures; not a bunch of dictionaries like most do. I also needed it
to be able to configure the loading via environmental variables (specifically
for Docker containers). So it seemed appropriate to toss together a library to
handle my needs.

Aumbry may be one of those niche use-cases for me, but perhaps others might
find it useful. Check it out, take a peak at the docs, and see if it might help
you out on your projects as well!


Installation:
--------------

```shell
# Install base package
pip install aumbry

# Install consul support
pip install aumbry['consul']

# Install yaml support
pip install aumbry['yaml']
```

Project Links:
----------------

* GitHub: [pyarmory/aumbry](https://github.com/pyarmory/aumbry)
* PyPI: [aumbry](https://pypi.python.org/pypi/aumbry)
* Documentation: [![Documentation Status](https://readthedocs.org/projects/aumbry/badge/?version=latest)](https://aumbry.readthedocs.io)
* Travis CI: [![Build Status](https://travis-ci.org/pyarmory/aumbry.svg?branch=master)](https://travis-ci.org/pyarmory/aumbry)
* CodeCov: [![Coverage](http://codecov.io/github/pyarmory/aumbry/coverage.svg?branch=master)](http://codecov.io/github/pyarmory/aumbry?branch=master)
