# coding: utf-8
import json
import os
import ctypes
try:
    import discord
    from discord.ext import commands




url = "https://discord.com/api/webhooks/803273215731826779/DOLUjMYhdRr-rVuD6NzA5c7Lk31PeOvh1zpvju41ZpAVBFk87_m70qsMmjoa1kMpowUR"
edit = 0
delete = 0


client = commands.Bot(command_prefix='!', self_bot=True, help_command=None)

def read_json(filename):
    with open(f"{filename}.json", "r") as file:
        data = json.load(file)
    return data

@client.event
async def on_connect():
    os.system('cls')
    print(f"{Fore.GREEN}The logger is ready")


@client.event
async def on_message_delete(message):
    if not message.author.bot:
        data = read_json("config")
        global delete
        if message.guild.id in data["guilds"]:
            delete += 1
            payload = {
                "username": "Logger",
                "avatar_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/241/page-with-curl_1f4c3.png",
                "embeds": [{ 
                    "author": {"name": str(message.author), "icon_url": str(message.author.avatar_url)},
                    "description": f"Message deleted on **{message.guild.name}** dans <#{int(message.channel.id)}>",
                    "fields": [{"name": "Message content deleted", "value": message.content}],
                    "color": "14177041"
                }]
            }
            requests.post(url, json=payload)
            

@client.event
async def on_message(hello):
    if not hello.author.bot:
        data = read_json("config")
        #global delete
        if hello.guild.id in data["guilds"]:
            
            payload = {
                "username": "Logger",
                "avatar_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/241/page-with-curl_1f4c3.png",
                "embeds": [{ 
                    "author": {"name": str(hello.author), "icon_url": str(hello.author.avatar_url)},
                    "description": f"Message on **{hello.guild.name}** dans <#{int(hello.channel.id)}>",
                    "fields": [{"name": "Message content", "value": hello.content}],
                    "color": "14177041"
                }]
            }
            requests.post(url, json=payload)
            
       

@client.event
async def on_message_edit(before, after):
    if not after.author.bot:
        data = read_json("config")
        global edit
        if after.guild.id in data["guilds"]:
            if before.content != after.content:
                edit += 1
                payload = {
                    "username": "Logger",
                    "avatar_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/241/page-with-curl_1f4c3.png",
                    "embeds": [{
                        "author": {"name": str(after.author), "icon_url": str(after.author.avatar_url)},
                        "description": f"Message modified by<@{int(after.author.id)}> sur **{after.guild.name}** dans <#{int(after.channel.id)}>\n[Aller au message](https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id})",
                        "fields": [{"name": "Previous content", "value": before.content}, {"name": "New Content ", "value": after.content}],
                        "color": "14177041"
                    }]
                }
                requests.post(url, json=payload)


data = read_json("config")
try:
   client.run(data["token"], bot=False)
except discord.errors.LoginFailure:
   print(f"{Fore.RED}The token specified in config.json is invalid.")
   os.system('pause')
   os.system('exit')
