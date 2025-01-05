# Windows

Some windowsy stuffs!

## ISO

- <https://gravesoft.dev/>

## Activation

- <https://massgrave.dev/>
- <https://github.com/massgravel/Microsoft-Activation-Scripts>

## Check license status

```shell
slmgr /xpr
```

or,

```shell
slmgr /dli
```

### tldr

Open powershell as administrator and execute,

```shell
irm https://get.activated.win | iex
```

## Battery

### Battery Report

```shell
powercfg /batteryreport
```

### Modern Standby

Modern Standby is a low-power state that allows your device to stay up-to-date whenever a suitable network is available. It's like a smartphone, always connected, always ready to receive notifications.

```shell
powercfg /availablesleepstates
```
