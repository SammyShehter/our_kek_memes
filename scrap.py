import os
import json
import time
import cssutils
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from utils import get_video_hash, get_image_hash, sendMessage


def write_to_json(filepath, json_data):
    with open(filepath, "w") as json_file:
        json.dump(json_data, json_file)


def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)


raw_data = read_json_file('./list.json')
channels = list(raw_data.keys())
base_url = "https://t.me/"
memes_dictionary = {}
current_datetime = datetime.now().strftime('%d.%m.%Y_%H:%M')
current_run_duplicates = {}

for channel in channels:
    working = True
    last_post = raw_data[channel]
    times_moved_to_next_post = 6

    while working:
        time.sleep(10)
        try:
            html_text = requests.get(
                f"{base_url}{channel}/{last_post}?embed=1&mode=tme").text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

        last_post += 1
        soup = BeautifulSoup(html_text, 'lxml')
        post = soup.find('a', class_="tgme_widget_message_photo_wrap")

        try:
            if not post:
                post_is_video = soup.find(
                    'video', class_="tgme_widget_message_video")
                if post_is_video:
                    times_moved_to_next_post = 6
                    video_src = post_is_video.get('src')
                    if video_src in current_run_duplicates:
                        continue
                    current_run_duplicates[video_src] = True
                    check_url_dup = os.system(
                        f"grep -r -l {video_src} ./archive/")
                    if check_url_dup == 0:
                        continue
                    video_hash = get_video_hash(video_src)
                    if video_hash in current_run_duplicates:
                        continue
                    current_run_duplicates[video_hash] = True
                    check_content_dup = os.system(
                        f"grep -r -l {video_hash} ./archive/")
                    if check_content_dup == 0:
                        continue
                    memes_dictionary[f'{channel}_{last_post}'] = {'hash': video_hash, 'src': video_src}
                    continue
                post_not_found = soup.find(
                    'div', class_="tgme_widget_message_error")
                if post_not_found and post_not_found.text == "Post not found":
                    if times_moved_to_next_post == 0:
                        last_post -= 7
                        raw_data[channel] = last_post
                        working = False
                    times_moved_to_next_post -= 1
            else:
                times_moved_to_next_post = 6
                style = cssutils.parseStyle(post['style'])
                url = style['background-image'].strip('url()')
                if url in current_run_duplicates:
                    continue
                current_run_duplicates[url] = True
                check_url_dup = os.system(f"grep -r -l {url} ./archive/")
                if check_url_dup == 0:
                    continue
                image_hash = get_image_hash(url)
                if image_hash in current_run_duplicates:
                    continue
                current_run_duplicates[image_hash] = True
                check_content_dup = os.system(f"grep -r -l {image_hash} ./archive/")
                if check_content_dup == 0:
                    continue
                memes_dictionary[f'{channel}_{last_post}'] = {'hash': image_hash, 'src': url}
        except Exception as e:
            sendMessage(f"An error occurred at scrap: {e}")
            raw_data[channel] = last_post
            working = False
write_to_json('./list.json', raw_data)
if memes_dictionary:
    write_to_json('./archive/' + current_datetime + '.json', memes_dictionary)
