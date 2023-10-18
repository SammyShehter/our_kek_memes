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
    
    for chunk in response.iter_content(chunk_size=4096):
        hash_object.update(chunk)

    hex_dig = hash_object.hexdigest()
    return hex_dig

def get_image_hash(url):
    response = requests.get(url)
    image_content = response.content
    
    hash_object = hashlib.sha256(image_content)
    hex_dig = hash_object.hexdigest()

    save_content_to_file("images", hex_dig, image_content)
    
    return hex_dig
