import os
import sys
import time
import subprocess
import ctypes
try:
    import colorama
    import pystyle
    import colored
    import discord
    import asyncio
    import datetime
    import requests
    import itertools
except ModuleNotFoundError:
    os.system("pip install -r requirements.txt")

from pystyle import *

def execute_script(script_name):
    script_path = os.path.join('utils', script_name)
    subprocess.run(['python', script_path], check=True)

def set_console_fullscreen():
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hwnd = kernel32.GetConsoleWindow()

    style = user32.GetWindowLongW(hwnd, -16)
    user32.SetWindowLongW(hwnd, -16, style | 0x00040000)

    user32.ShowWindow(hwnd, 3)  # SW_MAXIMIZE

def print_menu():
    text = """ 
                                                ╔════════════════════════════════╗
                                                ║██████╗░██╗░█████╗░██╗░░██╗░░░░░║
                                                ║██╔══██╗██║██╔══██╗██║░██╔╝░░░░░║
                                                ║██████╔╝██║███████║█████╔╝░░░░░░║
                                                ║██╔═══╝░██║██╔══██║██╔═██╗░░░░░░║
                                                ║██║░░░░░██║██║░░██║██║░░██╗░░░░░║╔════════════════════════════════╗
                                                ║╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░║║ Dev: _piak_                    ║
                                                ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║║ Discord: discord.gg/VbYYUM9Z6c ║
                                                ║███████╗██████╗░███████╗███████╗║║ Version: FREE                  ║
                                                ║██╔════╝██╔══██╗██╔════╝██╔════╝║╚════════════════════════════════╝
                                                ║█████╗░░██████╔╝█████╗░░█████╗░░║
                                                ║██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░║
                                                ║██║░░░░░██║░░██║███████╗███████╗║
                                                ║╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝║
                                                ╚════════════════════════════════╝

                                                1. Token Informations
                                                2. Token Nuker
                                                3. MassReport
                                                4. Server MassDM (bot)
                                                5. Server Cloner

    """
    print(Colorate.Horizontal(Colors.yellow_to_red, text))

def main():
    os.system("cls")
    set_console_fullscreen()
    while True:
        print_menu()
        choice = input(Colorate.Horizontal(Colors.yellow_to_red, "Enter your choice: ")).strip()

        if choice == "1":
            execute_script("token_info.py")
        elif choice == "2":
            execute_script("token_nuker.py")
        elif choice == "3":
            execute_script("discord_massreport.py")
        elif choice == "4":
            execute_script("server_massdm.py")
        elif choice == "5":
            execute_script("server_cloner")
        else:
            os.system("cls")
            print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice, please try again."))

if __name__ == "__main__":
    main()