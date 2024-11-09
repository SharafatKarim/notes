+++
title = "mysql"
description = "- Pull the image from the docker hub"
+++

# My SQL

## Installation

### Docker

- Pull the image from the docker hub

```bash
docker pull mysql
```

or, using podman?

```bash
podman pull docker.io/library/mysql
```

- Now, let’s create our first container from the mysql image. Here is the command we will use:

```bash
docker run --name test-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=tree -d mysql
```

> run: creates a new container or starts an existing one
> --name CONTAINER_NAME: gives the container a name. The name should be readable and short. In our case, the name is test-mysql.
> -e ENV_VARIABLE=value: the -e tag creates an environment variable that will be accessible within the container. It is crucial to set MYSQL_ROOT_PASSWORD so that we can run SQL commands later from the container. Make sure to store your strong password somewhere safe (not your brain).
> -d: short for detached, the -d tag makes the container run in the background. If you remove this tag, the command will keep printing logs until the container stops.
> image_name: the final argument is the image name the container will be built from. In this case, our image is mysql.
> -p HOST_PORT:CONTAINER_PORT: the -p tag maps a port from the host machine to the container. In this case, we are mapping port 3306 from the host to the container. This is the default port for MySQL.

If the command returns a long string of gibberish (the container ID), it means the container has started. You can check its status with docker ps:

- To access the terminal inside your container, you can use the following command:

```bash
docker exec -it container_name bash
```
- And then to login to mysql:

```bash
mysql -u root -p
```

