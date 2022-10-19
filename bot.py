#!/usr/bin/python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

# This is Telegram Video Watermark Adder Bot's Source Code.
# I Hardly Made This. So Don't Forget to Give Me Credits.
# Done this Huge Task for Free. If you guys not support me,
# I will stop making such things!

# Edit anything at your own risk!

# Don't forget to help me if I done any mistake in the codes.
# Support Group: @linux_repo 
# Bots Channel: @Discovery_Updates
import os
import os.path
import requests
import time
import json
import urllib.request
import random
import asyncio
import wget
import glob
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from plugins import download_poster, fetch, sizeof_fmt, send_video_handler_fmax, download_fmax
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen
from pyrogram import Client, filters
from configs import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, Message
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MessageNotModified
from bs4 import BeautifulSoup
import numpy as np
from deep_translator import GoogleTranslator
from proxyfix import proxyfix, proxycheck

AHBot = Client(Config.BOT_USERNAME, bot_token=Config.BOT_TOKEN, api_id=Config.API_ID, api_hash=Config.API_HASH)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}				
@AHBot.on_message(filters.command(["start", "help"]) & filters.private)
async def HelpWatermark(bot, cmd):
	await cmd.reply_text(
		text=Config.USAGE_WATERMARK_ADDER,
		parse_mode="Markdown",
		reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Developer", url="https://t.me/modbots"), InlineKeyboardButton("Support Group", url="https://t.me/linux_repo")], [InlineKeyboardButton("Bots Channel", url="https://t.me/Discovery_Updates")]]),
		disable_web_page_preview=True
	)
@AHBot.on_message(filters.command(["jav", "javs"]) & filters.private)

async def Jav(bot, cmd):
    user_id = cmd.from_user.id
    dl_path = str(user_id)
    a = await bot.send_message(
            chat_id=cmd.chat.id,
            text="HELLO",
        )
    pages = np.arange(1,3)# [1,2,3,4,5]
    for page in pages:
        url = f"https://www.allnporn.com/page/{page}/?filter=latest"
        page = requests.get(url, headers=headers)       
        soup = BeautifulSoup(page.content, 'lxml') 
        articles = soup.find_all('article')
        #print(soup)
        for art in articles:
            f = open('proxy.json')
            reqData = json.load(f)
            prox = reqData['proxy']    
            proxy = proxycheck(prox)
            
            print(proxy)
            try:
                img = art.find('img')['data-src']
                link = art.find('a')['href']
                title = art.find('a')['title'] 
                #cat,star,tag,video =  fetch(link)
                video = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
                with open(dl_path +'/videos.json') as json_file:
                    json_decoded = json.load(json_file)
                if not link in json_decoded:
                
                    file = urllib.request.urlopen(video)
                    filesize = file.length
                    readableSize = sizeof_fmt(filesize)
                    print(filesize)
                    if (int(filesize) < 1073741824):
                        print("i am here")
                       
                        print(dl_path)
                        if not os.path.exists(dl_path):
                            os.makedirs(dl_path)
                        poster = download_poster(img, dl_path)
                        vresult = download_fmax(video, dl_path)
                        videoname = os.path.basename(video)
                        file_path = os.path.join(f"{dl_path}/{videoname}")
                        if os.path.exists(file_path):
                            editable = await bot.send_message(
                                                                            chat_id=cmd.chat.id,
                                                                            text= "wait for a moment",
                                            
                                                                            )	
                            translated = GoogleTranslator(source='auto', target='my', proxies=proxy).translate(text=title)
                            width = 100
                            height = 100
                            duration = 0
                            metadata = extractMetadata(createParser(file_path))
                            if metadata.has("duration"):
                                duration = metadata.get('duration').seconds
                            if metadata.has("width"):
                                width = metadata.get("width")
                            if metadata.has("height"):
                                height = metadata.get("height")	
                            video_thumbnails = str(cmd.from_user.id) + "/" + "thumb.jpg"
                            file_size = os.path.getsize(file_path)
                            sent_vid = await send_video_handler_fmax(bot, cmd, file_path, video_thumbnails, duration, width, height, editable, file_size, translated)
                            vid = str(sent_vid.message_id)
                            json_decoded[link] = vid

                            with open(dl_path +'/videos.json', 'w') as json_file:
                                json.dump(json_decoded, json_file)
                            await editable.delete()
                            os.remove(video_thumbnails)
                            os.remove(file_path)
                            #filelist = glob.glob(os.path.join(dl_path, "*.*"))
                            #for f in filelist:
                            #    os.remove(f)
                        #await bot.send_photo(
                        #    chat_id=cmd.chat.id,
                        #    photo = 'thumb.jpg',
                        #    caption="👇" + translated + "...🎬 HD 🔞 " + str(star) + "Size: "+ readableSize,
                        #)
                        #os.remove('thumb.jpg')
                    else:
                        pass
                else:
                    pass
            except:
                pass
            #await bot.edit_message_text(
            #                text=f'>>>>>>>>>{page}<<<<<<<<<<',
            #                chat_id=cmd.chat.id,
            #                message_id=a.message_id
            #        )
   
AHBot.run()
