import requests
import time
import logging
from pymongo import MongoClient
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

api_key = '079025fd2d352a88e95dc71b9a51efcc'
url = f"https://api.openweathermap.org/data/2.5/weather?lat=40.64&lon=22.93&appid={api_key}"


def get_weather_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.warning("Weather data fetched successfully.")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return None


def send_to_mongodb(data):
    try:
        client = MongoClient('mongodb://mongo:27017/')
        db = client.weather_database
        collection = db.weather_data

        if data is not None:
            collection.insert_one(data)
            logging.warning("Data sent to MongoDB.")
    except Exception as e:
        logging.error(f"Error sending data to MongoDB: {e}")


if __name__ == "__main__":
    logging.warning("the app is running.")
    while True:
        weather_data = get_weather_data(url)
        send_to_mongodb(weather_data)
        time.sleep(300)
