# Standard library level imports
import glob 
import random
import shutil
import time
from io import BytesIO 
from PIL import Image
from ctypes import windll 

# Third party library level imports
import praw
import requests
import win32api
from requests import get

reddit = praw.Reddit(
    client_id="REDACTED",
    client_secret="REDACTED",
    user_agent="REDACTED",
)

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

subreddit = reddit.subreddit('wallpapers')

for post in subreddit.hot(limit = 1000):
    if post.url.endswith('jpg') or post.url.endswith('png'):
        response = requests.head(post.url)
        image_raw = get(post.url)
        image = Image.open(BytesIO(image_raw.content))
        image_width, image_height = image.size

        if image_width == width and image_height == height:
             
            response = requests.get(post.url, stream=True)
            path = f"C:\\Users\\Cooper\\Desktop\\Wallpaper SCRAPER\\images\\{post.url.split('/')[-1]}"
            with open(path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

def rando_wallpaper():
    wallpapers = glob.glob("C:\\Users\\Cooper\\Desktop\\Wallpaper SCRAPER\\images\\*")
    image_path =  random.choice(wallpapers)

     # Set the image as the desktop background
    SPI_SETDESKWALLPAPER = 20
    windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


interval = 1 * 60 # X minutes
while True:
        rando_wallpaper()
        time.sleep(interval)