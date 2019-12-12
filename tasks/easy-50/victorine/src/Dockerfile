FROM python:3.7-alpine

RUN apk add gcc musl-dev socat

ADD ./ /app

ADD ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]