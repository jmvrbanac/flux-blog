Title: RoundCube Unity WebApp Plugin
Date: 2012-8-6
Modified: 2014-11-09 11:16
Tags: Apps, Linux, Plugins, Ubuntu, Unity
Slug: roundcube-unity-webapp-plugin
Authors: John Vrbanac


A few weeks ago, Mark Shuttleworth announced the Unity WebApps concept.
Personally, I love the concept; however, I noticed that there was support
for gmail, but I couldn’t find support for the RoundCube webmail client
I use on my own servers. To remedy this, I decided to write a plugin for
roundcube that adds Unity WebApp support to your self-hosted RoundCube
instance.

**Features:**

* Allows you to go straight to composing a new message or viewing your
address book through the launcher or the HUD.
* Adds HUD Entries for each one of your mailbox folders.
* Adds MessagingEntries for every folder with unread messages.
* Shows a Unity notification when you recieve a new message.
* Shows the number of total unread messages, across all folders, on the
Unity Launcher icon.

You can find the latest version on the Launchpad project:

* Project Page: [Launchpad Project](https://launchpad.net/roundcube-unity-webapp-plugin)
* Plugin: [Download](https://launchpad.net/roundcube-unity-webapp-plugin/trunk/0.1/+download/roundcube-unity-webapp-plugin-0.1.tar.gz)

Note: Currently the plugin is only tested with RoundCube 0.7.2, so it may
or may not work for other versions.

**Known Issues:**

I have also noticed that occasionally, Firefox 14.0.1 (only seen on the
latest version) will just crash the first time accessing the page;
restarting Firefox seems to resolve the issue. I haven't discovered what
is causing this and it doesn't appear to extend to Chromium.