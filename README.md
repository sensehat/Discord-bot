---

# 🤖 Discord Automation Bot

This is a Python-based Discord bot designed to automate various tasks in a Discord server, such as welcoming new members, muting, banning, and providing help information for users.

## Features
- **Ping**: Test if the bot is online with `sudo ping`.
- **Welcome New Members**: Automatically welcomes new members and assigns a default role.
- **Help Command**: Displays a help menu with bot commands.
- **Moderation**: Commands for muting, unmuting, kicking, and banning members.
- **Message Purging**: Clear a specified number of messages.

## Prerequisites

Ensure you have the following installed before setting up the bot:

1. **Python 3.6+**: The bot requires Python 3.6 or higher.
2. **discord.py**: The library to interact with Discord API.
3. **Dotenv (Optional)**: If you want to use environment variables for token management.

Install required libraries using pip:

```bash
pip install discord.py
```

## ⚙️ Bot Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sensehat/Discord-bot.git
    chmod +x bot.py
    ```

2. **Configure the bot**:
    - Obtain your bot token from the [Discord Developer Portal](https://discord.com/developers/applications) and place it in the `client.run()` method at the bottom of the script.
    - Set up the command prefix in the bot. The default prefix I made is  `sudo `. You can change it by modifying the `command_prefix` in the following line:

    ```python
    client = commands.Bot(command_prefix="sudo ")
    ```

3. **Customize welcome messages**:
    - In the `on_member_join` event, configure the welcome channel and the default role assigned to new members. Update the `channel = client.get_channel()` to the channel ID where you want the welcome message to be sent.
    - You can also modify the welcome message and default role name.

4. **Run the bot**:
    - Execute the bot script:
    ```bash
    python bot.py
    ```

5. **Invite the bot to your server**:
    - Generate an OAuth2 URL from the Discord Developer Portal and invite your bot to your Discord server.

## 🛠️ Commands

| Command               | Description                                   | Permission Required   |
|-----------------------|-----------------------------------------------|-----------------------|
| `sudo help`           | Displays a list of available commands         | None                  |
| `sudo ping`           | Checks if the bot is online                   | None                  |
| `sudo clear [amount]` | Clears a specified number of messages         | Manage Messages       |
| `sudo mute <@member>` | Mutes a member                                | Administrator         |
| `sudo unmute <@member>`| Unmutes a member                             | Administrator         |
| `sudo kick <@member>` | Kicks a member from the server                | Administrator         |
| `sudo ban <@member>`  | Bans a member from the server                 | Administrator         |
| `sudo warn <@member> [reason]` | Warns a member with an optional reason | Administrator         |

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
