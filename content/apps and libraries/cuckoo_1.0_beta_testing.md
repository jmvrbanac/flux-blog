Title: Cuckoo 1.0 Beta Testing
Date: 2012-7-5
Modified: 2014-11-09 10:47
Tags: Alarm, App Showdown, Cuckoo, Linux, PPA, Python, Ubuntu
Slug: cuckoo-1.0-beta
Authors: John Vrbanac


Cuckoo is ready to be beta tested! I had an issue with packaging on the
build servers that I had to fix before I could get this thing out. With
that fix done, you can find Cuckoo in the PPA mentioned below.

There are still a few UI issues that I’m working on, but you should be
able to give this thing a go. One of the UI issues that’ll be addressing
is the list sorting. Currently, the alarm list doesn’t sort at all. I hope
to have that done late tonight after I get off work. Please report any
bugs you find on the Launchpad project page. Thanks!

* Launchpad Project: [https://launchpad.net/cuckoo-alarm](https://launchpad.net/cuckoo-alarm)
* PPA: ppa:john.vrbanac/cuckoo

**Installation:**

```bash
sudo apt-add-repository ppa:john.vrbanac/cuckoo
sudo apt-get update
sudo apt-get install cuckoo
```