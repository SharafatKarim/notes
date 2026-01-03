+++
title = "podman"
description = "Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. Its command-line interface is similar to Docker's, making it easy for users familiar with Docker to transition to Podman."
+++

# Podman

Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. Its command-line interface is similar to Docker's, making it easy for users familiar with Docker to transition to Podman.

## Installation

### Registries

- [Red Hat - Container Registries](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/working-with-container-registries_building-running-and-managing-containers)

## Packages

### N8N

To install,

```bash
podman run -d \
 --name n8n \
 --network=host \
 -e GENERIC_TIMEZONE="Asia/Dhaka" \
 -e TZ="Asia/Dhaka" \
 -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
 -e N8N_RUNNERS_ENABLED=true \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
 ```
