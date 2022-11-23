FROM python:3.9-slim
ADD . /code
WORKDIR /code
RUN apt-get update
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]