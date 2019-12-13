FROM php:7.1-fpm

RUN apt-get update && apt-get install -y socat

WORKDIR /home/task/

ADD index.php info.txt flag.txt ./

ENTRYPOINT ["php", "-S", "0.0.0.0:34567", "index.php"]