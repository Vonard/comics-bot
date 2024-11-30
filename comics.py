import requests


def download_image(url, filename, api_key=""):
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(f"{filename}", 'wb') as file:
        file.write(response.content)


def download_comic(comic_number):
    url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic = response.json()
    download_image(comic["img"], f"{comic_number}.png")


def get_latest_comic_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["num"]
