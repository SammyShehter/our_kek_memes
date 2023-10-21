import os
import requests
import hashlib


def save_content_to_file(folder, filename, content):
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(os.path.join(folder, filename), 'wb') as f:
        f.write(content)


def get_video_hash(url):
    response = requests.get(url, stream=True)

    hash_object = hashlib.sha256()

    video_chunks = []

    for chunk in response.iter_content(chunk_size=4096):
        video_chunks.append(chunk)
        hash_object.update(chunk)

    hex_dig = hash_object.hexdigest()

    video_content = b"".join(video_chunks)
    save_content_to_file("videos", f"{hex_dig}.mp4", video_content)

    return hex_dig


def get_image_hash(url):
    response = requests.get(url)
    image_content = response.content

    hash_object = hashlib.sha256(image_content)
    hex_dig = hash_object.hexdigest()

    save_content_to_file("images", f"{hex_dig}.jpg", image_content)

    return hex_dig


def sendMessage(message):
    try:
        data = {
            "service": "Our Memes",
            "message": message
        }
        requests.post("http://localhost:8887",
                      headers={'Content-Type': 'application/json'}, json=data)
    except Exception as e:
        print(f"An error occurred at main.sendMessage: {e}")
