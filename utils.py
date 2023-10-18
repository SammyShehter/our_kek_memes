import requests
import hashlib

def get_video_hash(url):
    response = requests.get(url, stream=True)
    
    hash_object = hashlib.sha256()
    
    for chunk in response.iter_content(chunk_size=4096):
        hash_object.update(chunk)

    return hash_object.hexdigest()

def get_image_hash(url):
    response = requests.get(url)
    image_content = response.content
    
    hash_object = hashlib.sha256(image_content)
    hex_dig = hash_object.hexdigest()
    
    return hex_dig
