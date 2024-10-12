#can change python version if we want...just put 3.8 since my computer runs 3.9.13
# TODO: change requirements.txt to poetry
FROM python:3.10


WORKDIR /root

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080
CMD [ "python3","manage.py","runserver","0.0.0.0:8080"]