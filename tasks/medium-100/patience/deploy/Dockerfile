FROM ubuntu:latest

RUN apt update
RUN apt install -y socat libseccomp-dev

ADD . /app

WORKDIR /app

RUN chmod +x ./serve.sh

CMD ["./serve.sh"]