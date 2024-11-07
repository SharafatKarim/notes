## ArchLinux

An operating system that is based on Linux. It is a free and open-source software. It is a rolling release system. It is a lightweight and flexible operating system. It is a simple and easy to use operating system. It is a fast and efficient operating system. It is a secure and stable operating system. It is a powerful and customizable operating system. It is a reliable and robust operating system. It is a versatile and extensible operating system. It is a modern and up-to-date operating system. It is a user-friendly and intuitive operating system. It is a community-driven and collaborative operating system. It is a cutting-edge and innovative operating system. It is a feature-rich and comprehensive operating system. It is a high-performance and high-quality

## Installation

Follow these sites,
- <https://sharafat.pages.dev/archlinux-install/>
- <https://sharafat.pages.dev/archlinux-post-install/>

And don't forget official wiki. It's the best!

## Misc

### Avoid signature check

Go to `/etc/pacman.conf` and edit the following `SigLevel` to `Never`,

```conf
SigLevel = Never
```

### Docker image

- Link to the docker image: <https://hub.docker.com/_/archlinux>

Must keep an eye on the following line!

> ⚠️⚠️⚠️ NOTE: For Security Reasons, these images strip the pacman lsign key. This is because the same key would be spread to all containers of the same image, allowing for malicious actors to inject packages (via, for example, a man-in-the-middle). In order to create a lsign-key run `pacman-key --init` on the first execution, but be careful to not redistribute that key. ⚠️⚠️⚠️
