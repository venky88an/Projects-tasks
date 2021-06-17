FROM python:3.8

WORKDIR /fast-api-app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . ./app

CMD ["python","./app/hello_world.py"]


