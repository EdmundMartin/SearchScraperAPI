FROM python:3-slim

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
RUN apt-get update

EXPOSE 5000
COPY . /server
WORKDIR /server


CMD ["python", "-OO", "-u", "run.py"]