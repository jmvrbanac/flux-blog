Title: Fixing tap to click in Debian Stretch
Date: 2016-7-10
Modified: 2016-7-10 01:00
Tags: Linux, debian, touchpad, tap to click
Slug: fixing-debian-touchpad
Authors: John Vrbanac

As I had some success with Debian Stretch on my desktop this week, I decided
to give it a try on my ultrabook. For reference purposes, it's a Samsung ATIV
Book 9 13.3 (NP900X3K-K01US). While the touchpad originally didn't function in
the installer, it worked just fine once Debian Stretch was installed. The
problem I ran into was that I couldn't enable tap-to-click in the touchpad settings.
After some research, I discovered that apparently one way to solve the issue was to
remove a conflicting package called **xserver-xorg-input-synaptics**. As a
result, I ran:

```shell
sudo apt-get remove xserver-xorg-input-synaptics
```

Once completed, I restarted the laptop. After logging back in, I was able to
go into Gnome's Mouse and Touchpad settings and it allowed me to enable
tap-to-click!

This seems like a bit of a drastic workaround, but it seemed to work for me.
Hopefully, it works for you as well.
