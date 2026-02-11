import requests

def get_news():
    # api_key = "pub_37dbdee1ba2e498ba7156a6b5d632c8a"

    url = "https://newsdata.io/api/1/latest? apikey=pub_37dbdee1ba2e498ba7156a6b5d632c8a"

    response = requests.get(url)
    data = response.json()
    return data