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

### Reference

- <https://askubuntu.com/questions/818929/login-ssh-with-ppk-file-on-ubuntu-terminal>
