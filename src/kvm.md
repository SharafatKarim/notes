# KVM - Virtual Machine

KVM, Kernel-based Virtual Machine, is a hypervisor built into the Linux kernel. It is similar to Xen in purpose but much simpler to get running.

- [Read more here...](https://wiki.archlinux.org/title/KVM)

## Setup

For ArchLinux,
- <https://wiki.archlinux.org/title/KVM#How_to_use_KVM>
- <https://wiki.archlinux.org/title/QEMU>

And, yet an another good guide,
- <https://computingforgeeks.com/install-kvm-qemu-virt-manager-arch-manjar/>

## Can't start KVM guest: "network 'default' is not active"?


First, confirm that the default network is indeed inactive:

```bash
sudo virsh net-list --all
```

If so, start the default network:

```bash
sudo virsh net-start default
```

Run the first command line again to see if it worked.

And, for autostart, I believe it is,
```bash
sudo virsh net-autostart default
```
> [Credit - askubuntu](https://askubuntu.com/questions/1036297/cant-start-kvm-guest-network-default-is-not-active)
