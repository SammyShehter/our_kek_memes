import os
import requests
import hashlib
import json

gpt_url = "http://localhost:8000/respond"


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
        requests.post(os.getenv("KEK_ALERT"),
                      headers={'Content-Type': 'application/json'}, json=data)
    except Exception as e:
        print(f"An error occurred at main.sendMessage: {e}")


def get_answer(user: str, text: str):
    try:
        payload = json.dumps({
            "id": user,
            "service_origin": "our_kek_memes",
            "text": text
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", gpt_url, headers=headers, data=payload)
        if response.status_code == 200:
            raw_response = response.json()
            if raw_response['error']:
                print("Error received in response.")
                return 'ok'
            elif 'message' in raw_response:
                return raw_response['message']
            else:
                print("No 'message' key found in the response.")
                return 'ok'
        else:
            print(f"Request failed with status code: {response.status_code}")
            return 'ok'
    except Exception as e:
        print(e)
        return 'ok'