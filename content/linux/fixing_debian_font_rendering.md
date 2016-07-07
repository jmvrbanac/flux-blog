Title: Fixing Debian Font Rendering
Date: 2016-7-7
Modified: 2016-7-7 12:00
Tags: Linux, debian, fonts, rendering
Slug: fixing-debian-font-rendering
Authors: John Vrbanac

I've been playing around with Debian Stretch this week and one of the really
annoying issues I ran into was with font rendering. I was trying to figure out
why my nice fonts looked like garbage. Come to find out, I was just missing a
configuration file! So, if you're like me and want nice and smooth fonts on
Debian, put the following into a file called **.fonts.conf** in your home
directory.

```xml
<?xml version='1.0'?>
<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
<fontconfig>
 <match target="font">
  <edit mode="assign" name="rgba">
   <const>rgb</const>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="hinting">
   <bool>true</bool>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="hintstyle">
   <const>hintslight</const>
  </edit>
 </match>
 <match target="font">
  <edit mode="assign" name="antialias">
   <bool>true</bool>
  </edit>
 </match>
  <match target="font">
    <edit mode="assign" name="lcdfilter">
      <const>lcddefault</const>
    </edit>
  </match>
</fontconfig>
```

Once that file has been saved at **~/.fonts.conf** restart your machine! When
you login again, your fonts should now be as smooth as butter!
