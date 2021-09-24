import requests
import shutil

my_api_key = "9e6c04dfda3479b024fc1c693806d1eb"


def get_weather_info(location):  # get api information from OpenWeatherMap
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&units=metric&appid="+my_api_key)
    weather = response.json()
    return weather


def download_icon(url):  #  code form google to download images.
    # Set up the image URL and filename
    image_url = url
    filename = "icon.png"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        # print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')
