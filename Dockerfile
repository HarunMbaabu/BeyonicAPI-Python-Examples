FROM python:3.8-slim-buster

COPY . .

COPY ./requirements.txt ./requirements.txt

WORKDIR .

RUN pip install -r requirements.txt

CMD [ "python3", "getExamples.py" ]