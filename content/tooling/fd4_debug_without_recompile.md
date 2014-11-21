Title: FlashDevelop 4 – Debug projects without recompiling
Date: 2012-3-30
Modified: 2014-11-09 10:30
Tags: Tools, FlashDevelop
Slug: fd4-debug-without-recompile
Authors: John Vrbanac

If you are using FlashDevelop for a large enterprise flash application
you probably use data from external sources such as XML files or some
other source. As a result, you end up having to restart the application
through the IDE quite frequently. With FlashDevelop, it forces you to
recompile the application every time you wish to do this. Well, there is
a quick modification you can make to FlashDevelop that’ll let you force
debug the project without having to recompile it.

Instructions:

* Open up the macro editor (Macros – Edit Macros)
* Click Add
* Select the new “Untitled” macro
* Change the label to something like “Run (w/o compile)”
* Change the shortcut to something you can remember (I use CTRL-F5)
* Edit the Entries section and add the following:  PluginCommand|ProjectManager.PlayOutput
* Click Ok
* You’re done!

Note: If you the keyboard shortcut you selected is already in use you
will need to restart FlashDevelop before the shortcut becomes active.
Just to be safe, you might restart your FlashDevelop anyhow.
