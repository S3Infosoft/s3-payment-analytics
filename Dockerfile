FROM ubuntu:18.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y gcc python3-pip python3-dev python3-tk

RUN mkdir /app
WORKDIR /app
COPY ./app /app
COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "api.py" ]

