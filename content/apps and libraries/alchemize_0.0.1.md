Title: Alchemize - Easy (De)serialization Models
Date: 2014-12-20
Modified: 2014-12-20 01:00
Tags: Python, PyPI, Library, Alchemize, Models
Slug: alchemize-0.0.1
Authors: John Vrbanac


I just released a new small project of mine called Alchemize.
Lately, I've been writing a lot of clients and services in Python and
I've noticed that there tends to be quite a bit of code duplication
between the data models that interact with the DB's and APIs. It seems like
you have one for your ORM and one for your API input/output. It really becomes a
pain to maintain. This is what spawned the idea of Alchemize.

There are plenty of de/serialization libraries out there. Unfortunately,
nearly all of them that I've seen are centered around you creating
a separate model for it; the exact thing I'm trying to avoid. What I
wanted was something I could use to augment my existing ORM models. Enter
Alchemize!

Alchemize allows for complete two-way serialization and deserialization of
JSON data via an explicit mapping. This mapping allows for you to even
create nested structures for easier data handling.

I know this is kind of a niche project, but perhaps other people who
need to do similar things might find it useful.

Installation:
--------------

```shell
pip install alchemize
```

Project Links:
----------------

* GitHub: [jmvrbanac/alchemize](https://github.com/jmvrbanac/alchemize)
* PyPI: [alchemize](https://pypi.python.org/pypi/alchemize)
* Documentation: [![Documentation Status](https://readthedocs.org/projects/alchemize/badge/?version=latest)](http://alchemize.readthedocs.org)
* Travis CI: [![Build Status](https://travis-ci.org/jmvrbanac/alchemize.svg?branch=master)](https://travis-ci.org/jmvrbanac/alchemize)
* Coveralls: [![Coverage Status](https://img.shields.io/coveralls/jmvrbanac/alchemize.svg)](https://coveralls.io/r/jmvrbanac/alchemize?branch=master)