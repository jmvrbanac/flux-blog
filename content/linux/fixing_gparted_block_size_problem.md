Title: Fixing the block size on a usb drive
Date: 2016-3-12
Modified: 2016-3-12 12:54
Tags: Linux, gparted
Slug: fixing-usb-drive-block-size
Authors: John Vrbanac

This afternooon, I plugged in a usb drive to put a Linux installer on; however,
when I opened gparted to format it, gparted gave me the following error "The
driver descriptor says the physical block size is 2048 bytes, but Linux says
it is 512 bytes".

This is usually caused by accidently using the wrong block size when copied an
iso to the drive. This is an annoying problem, but it's rather easy to fix.

The way I fix this problem is to use ```dd``` to write the correct block size
back onto the disk and then reformat the drive.

Here is the command I use:

```shell
sudo dd if=/dev/zero of=/dev/<id_of_your_device> bs=2048
```

Once this has completed, open gparted. Create a new partition table (gpt or msdos)
and create a new partition in the format you wish. Apply the changes and you are done!
