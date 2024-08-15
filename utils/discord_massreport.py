import requests
import threading
import os
from colored import *
from pystyle import *

DEFAULT_REPORT_REASON = "Inappropriate content"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MassReport(tokens, guild_id, channel_id, message_id, reason):
    threads = []
    for token in tokens:
        thread = threading.Thread(target=Report, args=(token, guild_id, channel_id, message_id, reason))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(Colorate.Horizontal(Colors.green_to_yellow, "All reports have been processed.\n"))

def Report(token, guild_id, channel_id, message_id, reason):
    url = 'https://discordapp.com/api/v8/report'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }
    payload = {
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason
    }

    response = requests.post(url, json=payload, headers=headers)
    
    status = response.status_code
    response_message = response.json().get('message', 'Unknown error')

    if status == 201:
        print("Report successfully sent!\n")
    elif status in (401, 403):
        print(f"{response_message}\n")
    else:
        print(f"Error: {response_message} | Status Code: {status}\n")

def load_tokens(file_path):
    tokens = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(" : ")
            if len(parts) == 2:
                token = parts[0].strip()
                tokens.append(token)
    return tokens

if __name__ == "__main__":
    clear()
    print(Colorate.Horizontal(Colors.yellow_to_red, """
╔═════════════════════════════════════════════════════════════════════════════════════════╗ 
║██████╗░██╗░█████╗░██╗░░██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██╔══██╗██║██╔══██╗██║░██╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██████╔╝██║███████║█████╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██╔═══╝░██║██╔══██║██╔═██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██║░░░░░██║██║░░██║██║░░██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║███╗░░░███╗░█████╗░███████╗███████╗░░░░██████╗░███████╗██████╗░░██████╗░██████╗░████████╗║
║████╗░████║██╔══██╗██╔════╝██╔════╝░░░░██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝║
║██╔████╔██║███████║███████╗███████╗░░░░██████╔╝█████╗░░██████╔╝██║░░░██║██████╔╝░░░██║░░░║
║██║╚██╔╝██║██╔══██║╚════██║╚════██║░░░░██╔══██╗██╔══╝░░██╔═══╝░██║░░░██║██╔══██╗░░░██║░░░║
║██║░╚═╝░██║██║░░██║███████║███████║░░░░██║░░██║███████╗██║░░░░░╚██████╔╝██║░░██║░░░██║░░░║
║╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░║
╚═════════════════════════════════════════════════════════════════════════════════════════╝
"""))
    file_path = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter the file path for tokens: "))
    tokens = load_tokens(file_path)
    
    guild_id = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter the server ID: "))
    channel_id = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter the channel ID: "))
    message_id = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter the message ID: "))
    
    reason = input(Colorate.Horizontal(Colors.yellow_to_red, f"Enter the report reason (default: {DEFAULT_REPORT_REASON}): ")).strip()
    if not reason:
        reason = DEFAULT_REPORT_REASON

    MassReport(tokens, guild_id, channel_id, message_id, reason)