FROM continuumio/miniconda3
MAINTAINER Robin Doumerc <robin@qwantresearch.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update  
RUN apt-get install -y build-essential gunicorn
RUN pip install --upgrade pip==9.0.3
RUN mkdir -p /deploy/api/logs
COPY . /deploy/api

RUN pip install -r /deploy/api/requirements/requirements.txt

WORKDIR /deploy/api
RUN python3 setup.py install
EXPOSE 5000

ENV NEWS_PG_USER=postgres
ENV NEWS_PG_PWD=pgpwd
# Start gunicorn
CMD [ "gunicorn" , "-b", '0.0.0.0', "news_api/app:app" ]
