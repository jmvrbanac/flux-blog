Title: Cuckoo 1.0.5 Release
Date: 2012-7-6
Modified: 2014-11-09 11:16
Tags: Alarm, Cuckoo, Linux, PPA, Python, Ubuntu
Slug: cuckoo-1.0.5-release
Authors: John Vrbanac

I've pushed out a new version of Cuckoo. I fixed a number of UI issues that were bugging me; including the list sorting issue that I mentioned earlier. I believe that I also fixed the locale issue that clepto1995 (reddit user) reported. Thank you for finding that! Please let me know if y'all see any bugs that need to get tackled. If you have ideas for features or would like to get involved with the project just let me know. Thanks!


Screenshots:

* [Main Window](http://i.imgur.com/EHfWt.png)
* [Edit Window](http://i.imgur.com/PYQIj.png)
* [Preferences Window](http://i.imgur.com/nl0d0.png)
* [Application Menu](http://i.imgur.com/nBkrE.png)
* [Indicator](http://i.imgur.com/vXzxc.png)
* [Unity Launcher](http://i.imgur.com/XIhAw.png)

Where to get:

* Launchpad Project: [https://launchpad.net/cuckoo-alarm](https://launchpad.net/cuckoo-alarm)
* PPA: ppa:john.vrbanac/cuckoo

**Installation:**

```bash
sudo apt-add-repository ppa:john.vrbanac/cuckoo
sudo apt-get update
sudo apt-get install cuckoo
```