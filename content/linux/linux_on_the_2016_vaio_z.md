Title: Linux on the 2016 Vaio Z
Date: 2017-2-16
Modified: 2017-2-16 23:50
Tags: Linux, Ubuntu, 2016, Vaio Z, VJZ131
Slug: linux-on-the-2016-vaio-z
Authors: John Vrbanac

I've been looking for a replacement ultrabook for the last few weeks and ran
across the new 2016 Vaio Z (VJZ131A11L). Fantastic hardware! It's sporting an
i7-6567U, Iris 550 graphics, great battery life, and a 13.3" WQHD (2560x1440)
display. Most importantly, it has a fantastic keyboard. Essentially, a 13"
i7 Macbook Pro, but with a better keyboard. Unfortunately, it has one
serious drawback; the UEFI firmware.

While the hardware is 100% linux compatible you have to jump
through a number of hoops to use Linux on the device. For some unknown reason,
you cannot start up a linux distro in EFI mode. For example, take a Ubuntu 16.10
usb drive and start it up under UEFI. It'll load up Grub, but the moment you
select an option, the screen goes black, the light on the usb drive goes out
and it just sits there. The logical next step would be to try it under legacy
mode, but that only sort of works. While it'll boot and install, I discovered
that the firmware will refuse to boot from the SSD under legacy mode.
It just complains that it cannot find Windows. It is very frustrating.

After a ton of fiddling, I finally found a workaround. I restored the laptop back
to it's original Windows 10 state. I then installed rEFInd and set it to the
default boot manager. At this point, I booted up the laptop with secure boot off,
under UEFI, and a Ubuntu usb drive in. Once in Grub, I edited the Grub entry
to include the `noefi` kernel option. Now it boots into the installer. When you
get to disk partitioning, **DO NOT TOUCH THE EFI PARTITION!** You can setup the rest
however you want. Once you finish the install and restart, you'll need to edit the
Grub entry again before you can boot into the freshly installed distro. Once
you login, you can then add the `noefi` kernel option to
`GRUB_CMDLINE_LINUX_DEFAULT` in `/etc/default/grub`. After you save that, run
`update-grub`. This will fix the Grub entries to automatically include the
option going forward. After all of that trouble, we're done. We now have a machine
booted in UEFI while running Linux in noefi mode... Fun! Pat yourself on the
back and treat yourself to a drink, because you've just gotten Linux to work on a new
Vaio Z!

Sorry that this isn't a full walk-through, but it should point you in the right
direction. Unfortunately, I spent all day trying to figure this out and didn't
have time for another rebuild. Work needs to get done and bills need to get
paid. When I redo this laptop in a couple months, I'll try to more fully
document the process.
