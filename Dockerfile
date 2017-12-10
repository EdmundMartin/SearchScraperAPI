FROM python:3-slim

COPY requirements.txt .
RUN pip install --upgrade && pip install -r requirements.txt
RUN apt-get update

EXPOSE 5000
COPY . /server
WORKDIR /server
RUN apt-get update \
    && pip install -r /server/requirements.txt


CMD ["python", "-OO", "-u", "run.py"]