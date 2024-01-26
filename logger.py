from pymongo import MongoClient
import time

client = MongoClient("mongodb://mongodb:27017/")
db = client.logdb
collection = db.logs

while True:
    log_entry = {"log_message": f"Log entry at {time.ctime()}"}
    collection.insert_one(log_entry)
    print(log_entry["log_message"])
    time.sleep(1)
