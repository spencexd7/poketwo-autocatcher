
# **Poketwo Autocatcher**

Automate catching Pokémon in Poketwo using the help of the [P2 Assistant Bot](https://discord.com/oauth2/authorize?client_id=854233015475109888).

## **Overview**
This script is designed to help catch Pokémon automatically in Poketwo by reacting quickly to spawn events. With a properly configured setup, it can greatly enhance your ability to capture Pokémon without needing manual intervention.  

> ⚠ **Disclaimer**: Use at your own risk. If your Discord or Poketwo account gets banned, we are not responsible.  
> **Note:** You should have the [P2 Assistant Bot](https://discord.com/oauth2/authorize?client_id=854233015475109888) added to your server for this script as it detects the name with the help bot's help.

## **Setup**

1. Clone the repository or download the project files.
2. Create a `config.json` file in the root directory with your bot's token and the IDs of the channels you want it to operate in.

### **Config Example (`config.json`):**
```json
{
  "token": "YOUR_DISCORD_TOKEN_HERE",
  "channels": [
    "CHANNEL_ID_1",
    "CHANNEL_ID_2",
    "CHANNEL_ID_3"
  ]
}
```

### **Installation**
1. Make sure you have **Python 3.8+** installed.
2. Install the required libraries using:
   ```bash
   pip install discord.py-self asyncio
   ```
   
### **Running the Bot**
Run the bot using the following command:
```bash
python main.py
```

## **Features**
- Automatically detects names and catches Pokémon spawned by Poketwo with the help of P2 Assistant bot.
- Configurable to operate in specific channels.
- Uses a fast response time to ensure maximum catch success.

## **Usage Tips**
- Avoid using it on your main Discord account to minimize the risk of a ban.
- Monitor the bot to ensure it behaves as expected and adjust channel IDs as necessary.
- Be mindful of using this tool excessively, as automated behavior could be flagged.

## **Disclaimer**
This bot is meant for educational purposes only. Using automation tools on Discord can result in bans or other penalties. By using this tool, you agree to take full responsibility for your actions and any consequences that arise.
