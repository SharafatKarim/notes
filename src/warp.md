# Warp

When the Internet was built, computers weren’t mobile. They sat in offices next to data centers. The Internet has changed but the assumptions made 30 years ago are making your experience slower and less secure.

1.1.1.1 with WARP replaces the connection between your device and the Internet with a modern, optimized, protocol.

- [Website](https://one.one.one.one/)
- [Play Store](https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone)

## Android

### Keys

Maybe replit? There are several keys tricks. Or, some telegram bots, like,

- [Warp Plus Channel](https://t.me/warpplus)
- [Warp Plus Bot](https://t.me/generatewarpplusbot)
- [Key generator site](https://warpwarpbish.netlify.app/)

### Zero Trust

It's a simple trick that may not work in future. Copy the device/ client id from `Settings > Advanced > Diagonstics > Client configuration` to `Settings > Advanced > Connection Options > DNS settings > Gateway DoH Subdomain`.

> Zero trup isn't recommended from me, if you already have warp+, I guess.

## Warp CLI

Available on linux also!

- [Instructions](https://developers.cloudflare.com/warp-client/get-started/linux/)

Start the service first,

```bash
sudo systemctl enable --now warp-svc.service
```

 Initial Connection

### To connect for the very first time

- Register the client `warp-cli registration new`.

> Or, if you have previous registration, check it's help menu,
> `warp-cli registration --help`.
> But before using license don't forget the above new command.

- Connect `warp-cli connect`.
- Run `curl https://www.cloudflare.com/cdn-cgi/trace/` and verify that warp=on.

> Also there's `wrap mode` command. Feel free to explore.
