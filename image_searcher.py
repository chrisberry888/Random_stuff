import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def display_map():
    # Search Google Images for an image of a map of the United States
    search_url = "https://www.google.com/search?q=united+states+map&tbm=isch"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the URL of the first image result
    img_url = "https:"+soup.find('img')['src']

    # Use the `requests` library to get the image
    img_data = requests.get(img_url).content

    # Use the `PIL` library to open and display the image
    img = Image.open(BytesIO(img_data))
    img.show()

if __name__ == "__main__":
    display_map()
