Title: Moving to Debian Stretch (Testing)
Date: 2016-7-12
Modified: 2016-7-12 13:00
Tags: Linux, debian
Slug: moving-to-debian-stretch
Authors: John Vrbanac

Those who have talked to me in the past few months know that I've been
a bit discontent with Ubuntu lately. Specifically around the stability of 16.04.
A couple years ago, I switched to using Ubuntu Gnome. Originally, I felt that
Unity had some very interesting UX ideas to increase productivity (specifically
the HUD). However, in recent years I feel that Unity really hasn't been making
much progress. Anyhow, over the past year, I've mainly stayed with Ubuntu due
to its compatiblity in the workplace; since everyone seems to make packages for
"Ubuntu". I tried various other distributions but they were either too unstable,
too old, or a pain to manage for a work machine.

I don't know who recommended it to me, but someone mentioned for me to try
Debian Testing (Stretch). So I pulled the trigger about two weeks ago and
rebuilt my primary work machine with it. I'm still using Gnome 3, as my
current workflow has been adapted to that; however, I was pleasently surprised.
A lot of the rougher aspects that I remember from strict Debian are gone.
Full-disk encryption is available at install time and dealing with propriary Nvidia
drivers was simple and straight forward. Using Debian Testing gives me
the newer packages I need without dealing with messy backports. There was one
oddity around font rendering that I had to fix, but other than that, its been
remarkably smooth on my Skylake desktop! Consider me impressed!

I also tried it on my Skylake laptop which wasn't quite as smooth. The touchpad
didn't work during the installer, but it came alive after the install was done.
Also, I had to enable the non-free repos and install the atheros firmware package
for my wifi to start functioning, but that really wasn't a surprise. So it was
a little more work to install, but it's running quite smooth now. We'll see if
this is a long-term change, but so far, it's looking pretty positive. If you
want to step away from Ubuntu and just try something alittle different, give
it a shot!

[Debian Testing Wiki](https://wiki.debian.org/DebianTesting)
