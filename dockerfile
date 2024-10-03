#can change python version if we want...just put 3.8 since my computer runs 3.9.13
FROM python:3.8 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/

EXPOSE 8080
CMD [ "python","manage.py","runserver","0.0.0.0:8080" ]