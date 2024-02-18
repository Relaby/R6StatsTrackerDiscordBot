# Siege Stats Discord Bot

![Bot Logo](insert_logo_url_here)

## Introduction
This Discord bot provides Siege (Tom Clancy's Rainbow Six Siege) player statistics. It fetches data from Ubisoft's servers and provides users with various stats including ranked, casual, and unranked stats.

## Features
- Fetch player statistics from Ubisoft servers.
- Provide detailed statistics including ranked, casual, and unranked stats.
- Display player profile information such as level, wins, losses, K/D ratio, and more.
- Customizable command prefix and Twitch streaming status.

## Usage
To use the bot, simply invite it to your Discord server and start using the provided commands.

### Commands
- `{command_prefix}ranked [name]`: Get the player's ranked stats.
- `{command_prefix}casual [name]`: Get the player's casual stats.
- `{command_prefix}unranked [name]`: Get the player's unranked stats.
- `{command_prefix}help`: Display a list of available commands.

## Setup
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain your Ubisoft email and password and update the `config.py` file.
4. Set up a Twitch account and obtain the streaming URL.
5. Customize the bot's settings in the `config.py` file.
6. Run the bot using `python bot.py`.

## Configuration
- `BOT_TOKEN`: Your Discord bot token.
- `TWITCH_URL`: URL of your Twitch stream.
- `COMMAND_PREFIX`: Prefix used to invoke bot commands.

## Contributing
Contributions are welcome! If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.

## Issues
If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
