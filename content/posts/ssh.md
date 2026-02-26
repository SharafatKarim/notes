+++
title = "ssh"
description = "SSH to connect to a remote server."
+++

# SSH

SSH to connect to a remote server.

## GUI method?

Use `putty` for GUI method.

- <https://archlinux.org/packages/extra/x86_64/putty/>

## Login SSH with .ppk file on Terminal

Convert your `.ppk` to `.pem` file using puttygen.

```bash
puttygen JokerX_KEY_PAIR.ppk -O private-openssh -o JokerX_KEY_PAIR.pem
```

Now, login to your server using the `.pem` file.

```bash
ssh -i JokerX_KEY_PAIR.pem
```

## SSH Port Forwarding

Forwarding remote port to local port.

```bash
ssh -L 1337:127.0.0.1:1337 test@192.168.122.34
```

### Reference

- <https://askubuntu.com/questions/818929/login-ssh-with-ppk-file-on-ubuntu-terminal>

