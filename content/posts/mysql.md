+++
title = "mysql"
description = "1. Pull the image from the docker hub"
+++

# My SQL

## Installation

### Docker

1. Pull the image from the docker hub

```bash
docker pull mysql
```

or, using podman?

```bash
podman pull docker.io/library/mysql
```

2. Now, let’s create our first container from the mysql image. Here is the command we will use:

```bash
docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=strong_password -d mysql
```

> run: creates a new container or starts an existing one
> --name CONTAINER_NAME: gives the container a name. The name should be readable and short. In our case, the name is test-mysql.
> -e ENV_VARIABLE=value: the -e tag creates an environment variable that will be accessible within the container. It is crucial to set MYSQL_ROOT_PASSWORD so that we can run SQL commands later from the container. Make sure to store your strong password somewhere safe (not your brain).
> -d: short for detached, the -d tag makes the container run in the background. If you remove this tag, the command will keep printing logs until the container stops.
> image_name: the final argument is the image name the container will be built from. In this case, our image is mysql.

If the command returns a long string of gibberish (the container ID), it means the container has started. You can check its status with docker ps:

3. To access the terminal inside your container, you can use the following command:

```bash
docker exec -it container_name bash
```
4. And then to login to mysql:

```bash
mysql -u root -p
```

