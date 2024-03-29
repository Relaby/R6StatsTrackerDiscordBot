# Siege Stats Tracker Discord Bot
## Introduction
This Discord bot provides Rainbow Six Siege player statistics. It fetches data from Ubisoft's servers and provides users with various stats including ranked and casual.
Made using (https://github.com/CNDRD/siegeapi) get components here.
Required to enter a Ubisoft email and password to access ubisoft api recommended to use a brand new ubisoft account.

## Features
- Fetch player statistics from Ubisoft servers.
- Provide detailed statistics including ranked and casual stats.
- Display player profile information such as level, wins, losses, K/D ratio, and more.
- Customizable command prefix.

## Usage
- To use the bot, simply invite it to your Discord server and start using the provided commands. (https://discord.com/oauth2/authorize?client_id=1206808503931371540&scope=bot&permissions=8)
- Grab stats of Xbox, Playstation, and PC!
- .ranked [platform] [username]
- .casual [platform] [username]

## Setup
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain your Ubisoft email and password and update the `config.py` file.
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
