FROM ubuntu:latest
RUN apt-get update && apt-get install -y socat
RUN mkdir /home/task
WORKDIR /home/task/
ADD shell flag.txt key ./
RUN chmod +x ./shell
ENTRYPOINT ["socat", "TCP-LISTEN:34567,reuseaddr,fork", "EXEC:./shell"]