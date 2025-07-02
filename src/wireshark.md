## Wireshark

### Archlinux

1. To install in Archlinux,

```shell
yay wireshark
```

for GUI, install the `wireshark-qt` one.

2. Add your user to the `wireshark` usergroup.

```shell
sudo usermod -a -G wireshark $(whoami)
```

3. And re-login and reboot.
