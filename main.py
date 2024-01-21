import requests
import discord

# Function to send a message through a Discord bot
async def send_bot_message(token, message):
    try:
        # Create a bot client
        client = discord.Client()

        @client.event
        async def on_ready():
            print(f"We have logged in as {client.user}")

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

        await client.login(token)
        await client.connect()

        while True:
            # Send messages until the user decides to exit
            message = input("Enter the message you want to send via the bot (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            # Send the message
            channel = await client.fetch_channel(1141837051415769198)  # Replace with your channel ID
            await channel.send(message)
            print("Message sent successfully!")

        await client.close()
    except Exception as e:
        print(f"Failed to send message: {e}")

# Function to display the "hm..." menu
def send_message_hm(token):
    while True:
        message = input("Enter the message you want to send via the bot (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        send_bot_message(token, message)

# Modify the main function to include the "hm..." menu option
def main():
    menu_text = """
                 _
__      __  ___ | |__   _ __   _   _ | | __ _ __ 
\ \ /\ / / / _ \| '_ \ | '_ \ | | | || |/ /| '__|
 \ V  V / |  __/| |_) || | | || |_| ||   < | |   
  \_/\_/   \___||_.__/ |_| |_| \__,_||_|\_\|_|   
                                                 
    """
    suggestion_text = "If you want to suggest stuff, add me on Discord: falcon7834 also join our discord! https://discord.gg/eFc5nZSSbC"

    print(menu_text)
    print(suggestion_text)

    option = input("Select an option (main, suggest, fakenukrv2, featureme, hm...): ")

    if option == "main":
        webhook_url = "https://discord.com/api/webhooks/1145419676231401572/IvqLz3KqAe39tEWIHNhi3fEsMBaSmBHr2S76qHwddl2HM9Enyf0THMHru5mLuAzKondr"
        send_message_submenu(webhook_url)
    elif option == "suggest":
        webhook_url_duplicate = "https://discord.com/api/webhooks/1144721438180393060/iuGIYrdix5G0cySvteWMMwN60rx21RLX6qjrgbrMmkxr0xXnDppJP2Ei2JzwxkGtK77J"
        send_message_submenu(webhook_url_duplicate)
    elif option == "fakenukrv2":
        webhook_url_fakenukrv2 = "https://discord.com/api/webhooks/1144721438180393060/iuGIYrdix5G0cySvteWMMwN60rx21RLX6qjrgbrMmkxr0xXnDppJP2Ei2JzwxkGtK77J"
        send_message_submenu(webhook_url_fakenukrv2, include_input_prompts=True)
    elif option == "featureme":
        webhook_url_featureme = "https://discord.com/api/webhooks/1144721438180393060/iuGIYrdix5G0cySvteWMMwN60rx21RLX6qjrgbrMmkxr0xXnDppJP2Ei2JzwxkGtK77J"
        send_message_submenu(webhook_url_featureme)
    elif option == "hm...":
        bot_token = "MTEzNzQ5OTE5MTYwMjU5ODAyOA.GWDajg.DhHZukhnUCRqv4dccK-Sck8NWCt_f5Zjs6XjDw"  # Replace with your bot token
        send_message_hm(bot_token)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
