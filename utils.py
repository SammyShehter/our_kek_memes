import os
import requests
import hashlib


def save_content_to_file(folder, filename, content):
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(os.path.join(folder, filename), 'wb') as f:
        f.write(content)


def get_video_hash(url, save_folder=None):
    response = requests.get(url, stream=True)

    hash_object = hashlib.sha256()

    video_chunks = []

    for chunk in response.iter_content(chunk_size=4096):
        video_chunks.append(chunk)
        hash_object.update(chunk)

    hex_dig = hash_object.hexdigest()

    video_content = b"".join(video_chunks)
    save_content_to_file("videos", hex_dig, f"{video_content}.mp4")

    return hex_dig


def get_image_hash(url):
    response = requests.get(url)
    image_content = response.content

    hash_object = hashlib.sha256(image_content)
    hex_dig = hash_object.hexdigest()

    save_content_to_file("images", hex_dig, f"{image_content}.jpg")

    return hex_dig
