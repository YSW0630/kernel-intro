# linux-in-practice-2nd

Experimental code for *Linux no Shikumi: Expanded and Revised Edition*.

# Setting Up the Experiment Environment

To run the experimental programs from the book on Ubuntu 20.04, run the following commands to install the required packages and configure your user account.

```console
$ sudo apt update && sudo apt install binutils build-essential golang sysstat python3-matplotlib python3-pil fonts-takao fio qemu-kvm virt-manager libvirt-clients virtinst jq docker.io containerd libvirt-daemon-system
$ sudo adduser `id -un` libvirt
$ sudo adduser `id -un` libvirt-qemu
$ sudo adduser `id -un` kvm
```
