import time
import math
import requests
import urllib.request
import wget
from urllib.error import HTTPError
from humanfriendly import format_timespan
from configs import Config
#from bot.helpers.utils import progress_for_pyrogram, humanbytesz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
def humanbytes(size: int) -> str:
    if not size:
        return ""
    power = 2 ** 10
    number = 0
    dict_power_n = {
        0: " ",
        1: "K",
        2: "M",
        3: "G",
        4: "T",
        5: "P"
    }
    while size > power:
        size /= power
        number += 1
    return str(round(size, 2)) + " " + dict_power_n[number] + 'B'

    # (c) @AbirHasan2005


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n".format(
            ''.join(["●" for i in range(math.floor(percentage / 5))]),
            ''.join(["○" for i in range(20 - math.floor(percentage / 5))])
            )

        tmp = progress + Config.PROGRESS.format(
            round(percentage, 2),
            humanbytesz(current),
            humanbytesz(total),
            humanbytesz(speed),
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="**{}**\n\n {}".format(
                    ud_type,
                    tmp
                ),
                parse_mode='markdown'
            )
        except:
            pass


def humanbytesz(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]


async def send_video_handler(bot, message, output_vid, video_thumbnail, duration, width, height, editable, file_size):
    c_time = time.time()
    ids = str(message.from_user.id) + '/'
    name = str(output_vid).replace("%20", " ").replace('.mp4', '').replace('.mkv', '').replace('./downloads/', '').replace(ids, '')

    sent_vid = await bot.send_video(
        chat_id=message.chat.id,
        video=output_vid,
        caption=f"**File Name:** `{name}`\n**Video Duration:** `{format_timespan(duration)}`\n**File Size:** `{humanbytesz(file_size)}`\n\n'@moedyiu",
        thumb=video_thumbnail,
        duration=duration,
        width=width,
        height=height,
        reply_to_message_id=message.message_id,
        supports_streaming=True,
        #reply_markup=InlineKeyboardMarkup([InlineKeyboardButton("Developer", url="https://t.me/AbirHasan2005")]),
        progress=progress_for_pyrogram,
        progress_args=(
            "Uploading, Wait Sir ...",
            editable,
            c_time
        )
    )
    return sent_vid

def download_fmax(url, dl_path):
  try:
    filename = wget.download(url, dl_path)

    return True
  except HTTPError:
    return False

def download_poster(url, dl_path):
  opener = urllib.request.URLopener()
  opener.addheader('User-Agent', 'whateveyuyr')
  filename = dl_path + "/thumb.jpg"
  try:
      r = opener.retrieve(url, filename)
  except HTTPError:
      Error = "Cannot Download"
      return Error
def download_fmax(url, dl_path):
  try:
    filename = wget.download(url, dl_path)

    return True
  except HTTPError:
    return False
def fetch(url):
    #url = 'https://www.allnporn.com/cumshot-lucky-black-dude-fucks-sexy-asian-milf-nicole-doshi-roughly/'
    page = requests.get(url, headers=headers)       
    soup = BeautifulSoup(page.content, 'lxml') 
    video =  soup.find('source',type="video/mp4")['src']
    #tags =  soup.find_all('a', class_='label')
    cat = []
    star = []
    tag = []
    #for ta in tags:
    #    if 'fa fa-folder' in ta:
    #        t = ta['title'].upper()#changing upper letters
    #        cat.append(t)
    #    else:
    #        pass
    #return res, video
    category = soup.find_all('i', class_= 'fa fa-folder')
    for ca in category:
        cat.append(((ca.parent)['title']).upper())
    #print(cat)
    
    stars = soup.find_all('i', class_= 'fa fa-star')
    for sa in stars:
        star.append(((sa.parent)['title']).upper())
    

    tags = soup.find_all('i', class_= 'fa fa-tag')
    for ta in tags:
        tag.append(((ta.parent)['title']).upper())
    #print(tag)
    return cat,star,tag,video

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

async def send_video_handler_fmax(bot, message, output_vid, video_thumbnail, duration, width, height, editable, file_size, title):
    c_time = time.time()
    ids = str(message.from_user.id) + '/'
    name = str(output_vid).replace("%20", " ").replace('.mp4', '').replace('.mkv', '').replace('./downloads/', '').replace(ids, '')

    sent_vid = await bot.send_video(
        chat_id=message.chat.id,
        video=output_vid,
        caption=f"**JAV DESP:** `{title}`\n**Video Duration:** `{format_timespan(duration)}`\n**File Size:** `{humanbytesz(file_size)}`\n\n'@moedyiu",
        thumb=video_thumbnail,
        duration=duration,
        width=width,
        height=height,
        #reply_to_message_id=message.message_id,
        supports_streaming=True,
        #reply_markup=InlineKeyboardMarkup([InlineKeyboardButton("Developer", url="https://t.me/AbirHasan2005")]),
        progress=progress_for_pyrogram,
        progress_args=(
            "Uploading New Video ...",
            editable,
            c_time
        )
    )
    return sent_vid