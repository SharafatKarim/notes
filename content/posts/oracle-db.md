+++
title = "oracle-db"
description = "Mainly I will be focusing linux, but will work on mac as well with same commands."
+++

# Oracle Database

## Installation

Mainly I will be focusing linux, but will work on mac as well with same commands.

> For windows? You can download the installer from the official website and follow the instructions.
>
> - <https://www.oracle.com/database/technologies/xe-downloads.html>

### Setup a container

Docker and podman are the two most popular containerization tools. I will be using podman for this, and I will recommend podman as well. Why? Maybe I will write a blog on this later.

Whatever, let's install podman! You can follow the official documentation for this. I guess most of the major linux distributions have podman in their official repositories.

Like, for Arch Linux:

```bash
sudo pacman -S podman
```

### Pull the image

There are mainly two images available for free, full and lite.

To get the full image:

```bash
podman pull container-registry.oracle.com/database/free:latest
```

And to be honest, it's a huge image around 9.48 G. So, I will recommend the lite version. It may take upto 2 G.

```bash
podman pull container-registry.oracle.com/database/free:23.5.0.0-lite
```

### Run the container

Now let's go ahead and actually run the container.

```bash
podman run -d -p 1521:1521 --name oracle-db container-registry.oracle.com/database/free:23.5.0.0-lite
```

Here, I have used the lite version of the image. You can use the full version as well. Just replace the image name.
And the port `1521` is the default port for Oracle Database. You can change it if you want.

> Flag `-d` is used to run the container in the background.
> Flag `-p` is used to map the host port to the container port.
> Flag `--name` is used to give a name to the container. (Try to remember it!)

### Set a password

Here I have used `1234` as the password. You can use whatever you want.

```bash
podman exec -it oracle-db ./setPassword.sh 1234
```

### Connect to the database

You can use any database client to connect to the database. I will be using SQL\*Plus.

```bash
podman exec -it oracle-db sqlplus
```

And then enter the following details:

- Username: `system`
- Password: `1234` (Or the one you set in the previous step!)

### Stop the container

```bash
podman stop oracle-db
```

### Start the container

```bash
podman start oracle-db
```

> You may need to start the container if you have restarted your system!

## Misc

### Port address

To get your outgoing forwarded port from podman, use the following,

```bash
podman port oracle-db     
```

## Integration

### VSCODE

It would be weird if we have to use terminal everytime we want to access our database, right?
Let's use vscode. Simply install the following extension,

- <https://marketplace.visualstudio.com/items?itemName=Oracle.sql-developer>

> Or, Launch VS Code Quick Open (Ctrl+P), paste the following command, and press enter.
>
> `ext install Oracle.sql-developer`
>
> The size of this extension is more than 300 M, so it'll take a bit of time.

- Now on our left/ right toolbar, you will find a icon, and maybe try to add a new connection? You will asked to fill up a form.

- For the port number try to use the one you got from `podman port oracle-db`.

- For the username, use `system`.

- And for the password, use the one you set in the previous steps.

- For the service name, it should be `FREE`. Or you can use the following code in `sqlplus` to get the service name,

```sql
SELECT VALUE 
FROM V$PARAMETER 
WHERE NAME = 'service_names';
```

And you are good to go!

