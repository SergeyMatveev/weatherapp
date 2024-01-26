import requests
import time
from pymongo import MongoClient

api_key = '079025fd2d352a88e95dc71b9a51efcc'
url = f"https://api.openweathermap.org/data/2.5/weather?lat=40.64&lon=22.93&appid={api_key}"


def get_weather_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def send_to_mongodb(data):
    client = MongoClient('mongodb://mongo:27017/')
    db = client.weather_database
    collection = db.weather_data

    if data is not None:
        collection.insert_one(data)


if __name__ == "__main__":
    while True:
        weather_data = get_weather_data(url)
        send_to_mongodb(weather_data)
        time.sleep(300)  # Пауза в 300 секунд (5 минут)
