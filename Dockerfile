from ubuntu:18.04

COPY . /opt/scrapy

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN python3 --version

RUN apt-get install curl -y

RUN apt-get install chromium-chromedriver -y

RUN ln -s /usr/bin/chromedriver /usr/local/bin/chromedriver
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["scrapy.py"]
