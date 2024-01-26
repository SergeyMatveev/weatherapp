import mysql.connector
from pymongo import MongoClient


def main():
    # Подключение к MongoDB
    mongo_client = MongoClient("mongodb://mongo:27017/")
    mongo_db = mongo_client["weather_database"]
    mongo_collection = mongo_db["weather_data"]

    # Подключение к MySQL
    mysql_conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="password",
        database="weather"
    )
    mysql_cursor = mysql_conn.cursor()

    # Извлечение последнего документа из MongoDB
    last_record = mongo_collection.find().sort('_id', -1).limit(1)

    for record in last_record:
        name = record.get('name', 'Unknown')
        temp = record['main']['temp'] if 'main' in record and 'temp' in record['main'] else None

        if temp is not None:
            # Вставка данных в MySQL
            insert_query = "INSERT INTO weather_data (city, temperature) VALUES (%s, %s)"
            mysql_cursor.execute(insert_query, (name, temp))
            mysql_conn.commit()
            print(f"Data inserted: {name}, {temp}")
        else:
            print("No temperature data found in the record")

    # Закрытие подключений
    mysql_cursor.close()
    mysql_conn.close()
    mongo_client.close()


if __name__ == "__main__":
    main()
