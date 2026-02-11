import requests
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("NEWS_KEY")

def get_news():

    url = f"https://newsdata.io/api/1/latest? apikey={api}"

    response = requests.get(url)
    data = response.json()
    return data