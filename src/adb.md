# Adb

## Pair & Connect

Use the following, to pair first,

```shell
adb pair ipaddr:port
```

Then use the following command to connect:

```shell
adb connect ipaddr:port
```

Use the following to list them out,

```shell
adb devices -l
```

## Mirror

```shell
adb shell screenrecord --bit-rate 8000000 --size 1280x720 --time-limit 180 /sdcard/video.mp4
```
