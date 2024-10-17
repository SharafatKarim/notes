+++
title = "linux"
description = "- [HW Probe](https://linux-hardware.org/?probe=c2bd74626f)"
+++

# Linux

## Personal reports

### Silvermoon

- [HW Probe](https://linux-hardware.org/?probe=c2bd74626f)
- [Blender benchmark](https://opendata.blender.org/benchmarks/602eeea9-c154-44ff-a61f-cd731cfecb29/)

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

## Battery

সর্বপ্রথমেই জেনে নিন আপনার ডিভাইসে এটা সাপোর্ট করবে কিনা। নিচের কমান্ডের মাধ্যমে,

```shell
cat /sys/power/state
```

আর তারপরে,

```shell
sudo dmesg | grep -i "acpi.*(supports"\
```

এবার খুঁজে দেখেন `S3` আছে কিনা অপশনে।

> Note from Alif bro

Fedora চালিত Acer travelmate TMP214-53 তে সাসপেন্ড (স্লিপ) ইস্যু ছিলো।
সমস্যাটা ছিলো সাসপেন্ড করে রাখলেও ব্যাটারি ড্রেন হয়ে যেত আর ব্যাগে রাখলে গরম হয়ে যেতো। অর্থাৎ সাসপেন্ড টু র‌্যাম হতো না; প্রসেসর চালু থাকতো। এই ধরনের সাসপেন্ডকে বলে s2idle যেটাতে প্রসেসর চালু থাকে। কিন্তু আমার যেটা দরকার সেটা হলো deep sleep যেটাতে শুধু ram এ হালকা পাওয়ার দেয়া হয় আর পাওয়ার লাইট ব্লিংকিং হয়। সেটা কেন যে ডিফল্ট হিসেবে সিলেক্ট করা ছিলো না, ভেবে আমি অবাক হই।

এই সমস্যা থাকার প্রমাণ হলো: cat /sys/power/mem_sleep এর আউটপুট আসবে [s2idle] deep
যেভাবে সমাধান করলাম:
/etc/default/grub খুললাম sudo nano /etc/dafault/grub কমান্ড দিয়ে।

যদি না খোলে তাহলে: cd /etc/default কমান্ড দিয়ে ওখানে গিয়ে sudo nano grub কমান্ড দিয়ে ওটা খুলুন।

ন্যানো টেক্সট এডিটর খুললে সেখান থেকে GRUB_CMDLINE_LINUX_DEFAULT এরকম বা এর কাছাকাছি কিছু দিয়ে শুরু হয় এমন লাইন খুঁজে বের করি।
লাইনের quotation mark এর ভিতরে যাই থাক না কেনো সেটার পরে একটা স্পেস দিয়ে  mem_sleep_default=deep  লিখে দেই।
উদাহরণস্বরূপ: আগে যদি GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" থাকে তবে পরে হলো: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash mem_sleep_default=deep"
এটা করার পরে ফাইলটা সেভ করি।

তারপরে grub update করতে হবে। grub update করার পদ্ধতি সবার একই নাও হতে পারে তবে sudo update-grub কিংবা sudo grub-mkconfig -o /boot/grub/grub.cfg কিংবা sudo grub2-mkconfig -o /boot/grub2/grub.cfg এরকম কোনো একটা কমান্ড দিয়ে আপনার কাজ হয়ে যাবার কথা। আর তাহলেই কাজ শেষ।
reboot করতে পারেন।
সমস্যা সমাধান হবার প্রমাণ হলো: cat /sys/power/mem_sleep এর আউটপুট আসবে s2idle [deep]

## Wireless mouse/ keyboard

Here's a kool link,

- <https://bbs.archlinux.org/viewtopic.php?id=273039>

And a sample systemd file,

```bash
# This service is used to work around an apparent bug that freezes
# keyboard and mouse inputs after waking from sleep.

[Unit]
Description=Reset the keyboard and mouse after waking from sleep
After=suspend.target hibernate.target hybrid-sleep.target suspend-then-hibernate.target

[Service]
ExecStart=/usr/local/bin/reset-input-devices.sh
CPUWeight=500

[Install]
WantedBy=suspend.target hibernate.target hybrid-sleep.target suspend-then-hibernate.
```

So good luck!

