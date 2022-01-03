# homelab-pi-discord-bot

# Setup development environment
```sh
virtualenv venv
source venv/bin/activate.fish
pip install -r requirements.txt
```

# Config and environment vars
```json
# config.json
{
    "master-01": "192.168.0.201:3000",
    "worker-01": "192.168.0.202:3000",
    "worker-02": "192.168.0.203:3000",
    "worker-03": "192.168.0.204:3000"
}
```
```env
# .env
DISCORD_TOKEN=<DISCORD_TOKEN>
DISCORD_GUILD_ID=<DISCORD_GUILD_ID>
```

# Local development
```sh
# Run on machine
python src/main.py

# Run on docker
earthly +compose-up
earthly +compose-down
```

# Release
```sh
earthly --build-arg TAG=<TAG> --push +release
```
