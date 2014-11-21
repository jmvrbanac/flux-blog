Title: Packmap - Python Package Dependency Mapping
Date: 2014-08-18
Modified: 2014-08-18 12:00
Tags: Launchpad, Python, PyPI, Utility, Dependencies
Slug: packmap
Authors: John Vrbanac

A month or so ago I ran into an issue where a nested dependency for one
of the projects I've been working on changed and caused a significant
number of tests to start failing. Unfortunately, it took me hours to
try to determine which one of the huge number of dependencies caused
the failure.

After dealing with the problem, I started wishing for a tool that could
help me monitor when Python dependencies change. I tried a number of the
existing Python tools, but they really only worked for smaller projects.
As a result, I ended up building PackMap.

PackMap is a simple utility which finds all dependent packages for a
given Python package. It does this by installing the package and all
of its dependencies into a clean and temporary virtual environment then
probing the installed components for their actual requirements.

There are two different ways that I use PackMap. First is to just to
generate a visual diagram for easy Human consumption. The second is
a JSON output that I use in CI systems. The primary benefit is that I
can easily diff the resulting JSON to determine which package has been
changed. Give it a shot yourself!

**Project Links:**

* GitHub: [jmvrbanac/PackMap](https://github.com/jmvrbanac/PackMap)
* PyPI: [PackMap](https://pypi.python.org/pypi/packmap)

**Supported Python Versions:**

* 2.7.8

**Installation:**

```bash
pip install packmap -U
```

