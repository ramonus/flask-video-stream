FROM alpine

RUN apk update && apk add python3
ADD ./ /data
WORKDIR /data
RUN pip3 install -r requirements.txt
CMD python3 server.py