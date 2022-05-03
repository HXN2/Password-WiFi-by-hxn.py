import os
import requests
import socket
from sys import platform
import webbrowser
url = "https://t.me/HEXiN1K"
webbrowser.open(url)
from colorama import *
from datetime import datetime

app_name = " WiFi PasS "
now = datetime.now()

current_time = now.strftime

name = socket.gethostname()

myHostName = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\n===========================================================")


print(Fore.YELLOW+'\n Welcome you in my program' + app_name + "Made by hxn.py < insta")


name = (Fore.WHITE+"""\n                    Hello sir """ +name+Style.RESET_ALL)
print(name)

import datetime
e = datetime.datetime.now()
print (Fore.CYAN+"""\n                   Your Day is """+"%s/%s/%s" % (e.day, e.month, e.year))
print ("""\n                   The time is """+ "%s:%s:%s" % (e.hour, e.minute, e.second))

host = (Fore.WHITE+"""\n                  Your platform is """+ platform+Style.RESET_ALL)
print(host)

api = "https://api.ipify.org/?format=json"
req = requests.get(api)
response = req.json()
a = response["ip"]

IP = ("""\n                Your Local iP is """+Fore.RED+a+Style.RESET_ALL)
print(IP)


v = (Fore.RED+"""\n                    Your iNFO PROXY is\n"""+Style.RESET_ALL)

print(v)
print(s)

print("\n===========================================================")

url = "https://instagram.com/hxn.py/"
webbrowser.open(url)
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))

        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
input("")

