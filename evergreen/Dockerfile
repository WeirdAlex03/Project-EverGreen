FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /root
COPY pyproject.toml .
RUN pip3 install poetry 
RUN poetry config virtualenvs.create false --local


RUN poetry install 
COPY . .

EXPOSE 8080

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait
RUN ["/wait"]

SHELL [ "poetry", "run" ]

