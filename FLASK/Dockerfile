FROM python:3.6

COPY . .

COPY ./requirements.txt ./requirements.txt

WORKDIR .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]