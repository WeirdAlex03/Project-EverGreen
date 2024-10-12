FROM python:3.10

ENV HOME /root
WORKDIR /root

COPY pyproject.toml .
RUN pip3 install poetry 
RUN poetry config virtualenvs.create false --local

RUN poetry install 
COPY . .

EXPOSE 8080
SHELL [ "poetry", "run" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]