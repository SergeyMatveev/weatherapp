FROM python:3.8-slim

WORKDIR /app

COPY testapp.py /app

CMD ["python", "./testapp.py"]



