#can change python version if we want...just put 3.8 since my computer runs 3.9.13
# TODO: change requirements.txt to poetry
FROM python:3.8

ENV HOME /root
WORKDIR /root

COPY . . 
RUN pip3 install -r requirements.txt
COPY . /code/

EXPOSE 8080
CMD [ "python","manage.py","runserver","0.0.0.0:8080" ]