FROM python:3.9-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./bot/. .

EXPOSE 8080

CMD ["python", "bot.py"]