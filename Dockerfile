FROM python:3.8-slim

WORKDIR /app

COPY logger.py /app

CMD ["python", "./logger.py"]


'''
# Используйте официальный образ Python как базовый
FROM python:3.8

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте файлы requirements.txt в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте исходный код приложения в контейнер
COPY . .

# Команда для запуска приложения
CMD ["python", "./app.py"]
'''
