import cssutils
from bs4 import BeautifulSoup
import requests
import time
import json
from datetime import datetime
import os


def write_to_json(filepath, jsonData):
    with open(filepath, "w") as json_file:
        json.dump(jsonData, json_file)


def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        dump = json.load(json_file)
        return dump


raw_list = read_json_file('./list.json')
parsed_keys = raw_list.keys()
channels = list(parsed_keys)
base_url = "https://t.me/"
memes_dictionary = {}
current_datetime = datetime.now().strftime('%d.%m.%Y_%H:%M')

for channel in channels:
    working = True
    lastPost = raw_list[channel]

    while working:
        time.sleep(10)
        html_text = requests.get(base_url + channel + '/' +
                                 str(lastPost)+'?embed=1&mode=tme').text

        soup = BeautifulSoup(html_text, 'lxml')
        try:
            post = soup.find('a', class_="tgme_widget_message_photo_wrap")
            if not post:
                post_not_found = soup.find(
                    'div', class_="tgme_widget_message_error")
                if post_not_found and post_not_found.text == "Post not found":
                    raw_list[channel] = lastPost
                    working = 0
                lastPost += 1
                continue
            lastPost += 1
            style = cssutils.parseStyle(post['style'])
            url = style['background-image'].replace(
                'url(', '').replace(')', '')
            exit_status = os.system(f"grep -r -l '{url}' ./archive/*.json")
            if exit_status == 0:
                continue
            memes_dictionary[f'{channel}_{lastPost}'] = url+'\n'
        except Exception as e:
            raw_list[channel] = lastPost
            working = 0

write_to_json('./list.json', raw_list)

if memes_dictionary:
    write_to_json('./archive/' + current_datetime + '.json', memes_dictionary)
