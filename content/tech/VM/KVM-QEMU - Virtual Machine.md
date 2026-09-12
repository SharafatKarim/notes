Let's dig into some blogs first,
- https://computingforgeeks.com/install-kvm-arch-linux/

## Setup

first pacman,
```
sudo pacman -S qemu-full virt-manager virt-viewer libvirt dnsmasq edk2-ovmf swtpm iptables-nft
```

|Package|Purpose|
|---|---|
|`qemu-full`|Complete QEMU installation with all architecture support and features (x86, ARM, etc.)|
|`virt-manager`|GTK-based graphical interface for creating and managing virtual machines|
|`virt-viewer`|Console viewer for connecting to VM displays (SPICE/VNC)|
|`libvirt`|Virtualization management daemon and API – the glue that ties KVM and QEMU together|
|`dnsmasq`|Lightweight DHCP and DNS server for NAT-based VM networking|
|`edk2-ovmf`|UEFI firmware for virtual machines – required for UEFI-boot VMs and Secure Boot|
|`swtpm`|Software TPM 2.0 emulator – needed for Windows 11 VMs and TPM-dependent operating systems|
|`iptables-nft`|Firewall backend that libvirt uses to set up NAT networking rules|

One thing worth mentioning: the old `bridge-utils` package is no longer needed on current Arch installations. Bridge creation is handled by `iproute2`, which is already part of the base system.

then start the service,
```
sudo systemctl enable --now libvirtd
```

### user to the group

```
sudo usermod -aG libvirt $(whoami)
```

### Configure the Default NAT Network

well you sure can do it from the virtual machine manager as well, so it's k inda optional

```
sudo virsh net-start default
sudo virsh net-autostart default
```

## Enabling Nested Virtualization

Nested virtualization lets you run VMs inside VMs. This is useful for testing hypervisors, running Kubernetes clusters with KVM nodes, or developing virtualization-related software. To enable it permanently, create a modprobe configuration file.

For Intel CPUs:

```
echo "options kvm_intel nested=1" | sudo tee /etc/modprobe.d/kvm-intel.conf
```


For AMD CPUs:

```
echo "options kvm_amd nested=1" | sudo tee /etc/modprobe.d/kvm-amd.conf
```

Reboot for the change to take effect, then verify nested virtualization is enabled:

```
cat /sys/module/kvm_intel/parameters/nested
```

The output should be `Y` or `1`, confirming nested virtualization is active.

## Changing default storage pool

you can use virtual machine manager to do so with GUI