FROM python:3.9-alpine3.12

WORKDIR /usr/src/bot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
COPY . .

RUN python3 -m pip install --upgrade pip &&\
    pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn --bind 0.0.0.0:$PORT eliza.wsgi
