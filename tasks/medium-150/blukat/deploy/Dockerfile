FROM python:3.7-alpine

RUN apk add socat gcc musl-dev

RUN pip install pycrypto

RUN mkdir /app

WORKDIR /app

ADD server.py .

RUN chmod +x server.py

CMD ["socat", "TCP-LISTEN:31337,fork,reuseaddr", "EXEC:./server.py"]