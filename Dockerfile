FROM python:3.10-slim

WORKDIR /factorial-app

#copy project
COPY . .

CMD ["python3", "main.py"]