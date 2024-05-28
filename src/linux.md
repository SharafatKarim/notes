# Linux

## Autostart

directory (user) = `~/.config/autostart/`
directory (system) = `/etc/xdg/autostart/`

To remove autostart for a program, delete the `.desktop` file in the appropriate directory.
To hide system autostart programs, copy the `.desktop` file to the user directory and add `Hidden=true` to the file.
An example, to hide `octopi-notifier.desktop`:

```bash
[Desktop Entry]
Name=Octopi Notifier
Icon=octopi
Exec=/usr/bin/octopi-notifier
Terminal=false
Type=Application
Categories=GNOME;GTK;System;
#NotShowIn=GNOME;XFCE;LXDE;KDE;
StartupNotify=true
X-LXQt-Need-Tray=true
Version=1.5
SingleMainWindow=true
Hidden=true
```

## Desktop Entry

Desktop entry directory (user) = `~/.local/share/applications/`

To add a program to the pro, create a `.desktop` file in the appropriate directory.
An example, to add `tlauncher`:

```bash
[Desktop Entry]
Categories=Game;
Comment[en_US]=A Minecraft launcher
Comment=A Minecraft launcher
Exec=java -jar /home/sharafat/Games/TLauncher.v10/TLauncher.jar
GenericName[en_US]=A Minecraft Launcher
GenericName=A Minecraft Launcher
Keywords=minecraft;
MimeType=
Name[en_US]=TLauncher
Name=TLauncher
Path=
Icon=minecraft
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
X-KDE-SubstituteUID=false
X-KDE-Username=
```

> You may need to set executable permission to the `.desktop` file.
