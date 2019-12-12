FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1
RUN apk add socat

WORKDIR /app
ADD main.py ./
RUN chmod +x ./main.py
ADD start.sh ./
RUN chmod +x ./start.sh

ENTRYPOINT ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:./start.sh"]