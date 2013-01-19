DropShot
========

DropShot is a simple application that makes sharing screenshots easy. Simply assign a keyboard shortcut to the DropShot service and once it is triggered you will be able to select the screen area you want to share. From there, DropShot will automatically save the image file in your Dropbox folder and set a sharing link to your clipboard so you can share it easily with `Cmd+v`.

How to install
--------------

Download the `zip` file from the `Tags` menu, extract it and run
> python install.py

The installer will ask for your Dropbox user number (which can be found when you share a file, for instance `https://dl.dropbox.com/u/7831941/foto.jpg`) and the path to your Public folder (defaults to `~/DropBox/Public`).

After that you just need to setup a keyboard shortcut to activate DropShot. You can do this on `System Preferences -> Keyboard -> Keyboard Shortcuts -> Services`, scrolling down all the way to find the DropShot service. Click on `add shortcut` and press the key combination you want.

And that's it. Every time you trigger DropShot with the key combination you chose you will be able to select an area of screen to share. The sharing URL wil be on your clipboard, one `Cmd+v` away.

Next steps
-------------------
* Stop using the deprecated Dropbox Public folder
* Use Dropbx API to generate the sharing URL
* Develop Windows version
