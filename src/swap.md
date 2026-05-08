# Swap

## How-to-Enable-Swap-on-Ubuntu

Enabling swap space on your Ubuntu system is an essential task for optimizing performance, especially if you're running resource-intensive applications. Swap space acts as an overflow area for your RAM, allowing your system to continue functioning smoothly when the physical memory is fully utilized. In this guide, we'll walk you through the process of enabling swap on Ubuntu.

### Step 1: Check Existing Swap Space
Before creating new swap space, it's important to check if any swap is already enabled. Use the following command to display any existing swap:

```
sudo swapon --show
```

If the output is empty, it means no swap is currently enabled on your system.

### Step 2: Create a Swap File
Next, create a swap file using the fallocate command. This command will allocate the specified amount of disk space for the swap file. In this example, we'll create a 10 GB swap file:

```
sudo fallocate -l 10G /swapfile
```

### Step 3: Secure the Swap File
To prevent unauthorized access to the swap file, it's important to set the correct permissions. Use the chmod command to restrict access:

```
sudo chmod 600 /swapfile
```

### Step 4: Set Up the Swap File
Now that the swap file is created and secured, you need to set it up as a swap space using the mkswap command:

```
sudo mkswap /swapfile
```

### Step 5: Enable the Swap File
After setting up the swap file, enable it with the following command:


```
sudo swapon /swapfile
```

To confirm that the swap file is active, you can re-run the `sudo swapon --show` command, and you should see the new swap space listed.

### Step 6: Make the Swap File Permanent
To ensure that the swap file is enabled every time your system boots, you'll need to add it to the /etc/fstab file. Open the file in a text editor:

```
sudo nano /etc/fstab
```

Add the following line at the end of the file:

```
swapfile swap swap defaults 0 0
```

Save the file and exit the text editor.