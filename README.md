# freegamenotif

Notifier for free games

Right now includes sources:

- Epic games

And notifs:

- Discord webhook

originally made for my discord server <https://discord.gg/kNyh9RPm5n>, we now use <https://freestuffbot.xyz> in that server.

## env

- `FGN_FORCE` should be either `true` or `false`, Indicates if fgn should ignore already notified games and notify them anyway. Used for development.
- `FGN_WEB` should be either `true` or `false`, Indicates if fgn should start a web server on port 8080. Used for automatic running.
- `FGN_DISCORD_URL` should be a discord webhook url, The discord webhook to send to.
- `FGN_DISCORD_LOG` should be a discord webhook url, Logging webhook used for debugging.
