import os
import colored
import pystyle
import colorama
from colored import fg
from pystyle import Write, System, Colors, Colorate, Anime
from colorama import *
import discord
from discord.ext import commands

os.system("cls")
print(Colorate.Horizontal(Colors.yellow_to_red, """
╔════════════════════════════════════════════════════════════════════════════════════╗                          
║██████╗░██╗░█████╗░██╗░░██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██╔══██╗██║██╔══██╗██║░██╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██████╔╝██║███████║█████╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██╔═══╝░██║██╔══██║██╔═██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║██║░░░░░██║██║░░██║██║░░██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║███╗░░░███╗░█████╗░███████╗███████╗██████╗░███╗░░░███╗░░░░██████╗░░██████╗░████████╗║
║████╗░████║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗░████║░░░░██╔══██╗██╔═══██╗╚══██╔══╝║
║██╔████╔██║███████║███████╗███████╗██║░░██║██╔████╔██║░░░░██████╔╝██║░░░██║░░░██║░░░║
║██║╚██╔╝██║██╔══██║╚════██║╚════██║██║░░██║██║╚██╔╝██║░░░░██╔══██╗██║░░░██║░░░██║░░░║
║██║░╚═╝░██║██║░░██║███████║███████║██████╔╝██║░╚═╝░██║░░░░██████╔╝╚██████╔╝░░░██║░░░║
║╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═╝░░░░░╚═╝░░░░╚═════╝░░╚═════╝░░░░╚═╝░░░║
╚════════════════════════════════════════════════════════════════════════════════════╝"""))
# Demander le token du bot, le message et l'ID du serveur
bot_token = input(Colorate.Horizontal(Colors.yellow_to_red, "Entrez le token du bot : "))
message_template = input(Colorate.Horizontal(Colors.yellow_to_red, "Entrez le message (utilisez {user} pour mentionner l'utilisateur ) : "))
guild_id = int(input(Colorate.Horizontal(Colors.yellow_to_red, "Entrez l'ID du serveur : ")))

# Initialiser le bot
intents = discord.Intents.default()
intents.members = True  # Activer l'intention des membres
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')
    
    guild = bot.get_guild(guild_id)
    if guild is None:
        print(f'Impossible de trouver le serveur avec l\'ID {guild_id}')
        await bot.close()
        return

    for member in guild.members:
        if member.bot:
            continue  # Ignorer les autres bots
        personalized_message = message_template.replace("{user}", member.mention).replace("\\n", "\n")
        try:
            await member.send(personalized_message)
            print(f'Message envoyé à {member.name}')
        except Exception as e:
            print(f'Impossible d\'envoyer un message à {member.name}: {e}')

    await bot.close()

bot.run(bot_token)