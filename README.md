### **Beyonic API Python Examples.** 


The beyonic APIs Doc Reference: https://apidocs.beyonic.com/

To start using the Beyonic API Python API, you need to start by downloading the Beyonic API fficial Python client library and setting your secret key.


**Install the Beyonic API Python Official client library** 

```python
>>> pip install beyonic
```

**Setting your secrete key.** 

To set the secrete key install the python-dotenv modeule, **Python-dotenv** is a Python module that allows you to specify environment variables in traditional UNIX-like “.env” (dot-env) file within your Python project directory, it helps us work with SECRETS and KEYS without exposing them to the outside world, and keep them safe during development too.

**Installing python-dotenv modeule**

```python 
>>> pip install python-dotenv
```

**Creating a .env file to keep our secrete keys.**

```bash
>>> touch .env
``` 

Inside your .env file specify the Beyonic API Token . 

**.env file** 
```python
BEYONIC_ACCESS_KEY = "enter your API "
```

You will get your API Token by clicking your user name on the bottom left of the left sidebar menu in the Beyonic web portal and selecting ‘Manage my account’ from the dropdown menu. The API Token is shown at the very bottom of the page.


#### **[getExamples.py](https://github.com/HarunMbaabu/BeyonicAPI-Python-Examples/blob/main/getExamples.py)**

```python
import os 
import beyonic
from dotenv import load_dotenv

load_dotenv()

myapi = os.environ['BEYONIC_ACCESS_KEY']

beyonic.api_key = myapi 

'''
Common get methods 
'''

#Listing account.
'''
accounts = beyonic.Account.list() 
print(accounts)
'''

#Listing currencies.
'''
currencies = beyonic.Currency.list()
print(currencies)

Error:
beyonic.errors.ResponseError: 500 error:
b'{"detail":"An unexpected error has occurred. Please report to support@beyonic.com. Error Id: None"}'
'''

#Listing networks
'''
networks = beyonic.Network.list()
print(networks)
'''

#Listing transactions.
transactions = beyonic.Transaction.list()
print(transactions) 

#Listing contact.
contacts = beyonic.Contact.list() 
print(contacts) 


#Listing events
'''
events = beyonic.Event.list()
print(events)

Error: AttributeError: module 'beyonic' has no attribute 'Event'
'''

```

**Docker file**

```Dockerfile
FROM python:3.6

COPY . .

COPY ./requirements.txt ./requirements.txt

WORKDIR .

RUN pip install -r requirements.txt


CMD [ "python3", "getExamples.py" ]
```

**Build docker image called demo** 

```docker
>>> docker build -t bey .
``` 

**Run docker image called demo**

```docker
>>>docker run -t -i bey 
``` 

Now, I’ll create a Docker compose file to run a Docker container using the Docker image we just created. 


```docker-compose.yml

version: "3.6"
services:
  app:
    build: .
    command: python main.py
    ports:
      - "5000:5000"
    volumes:
      - .:/python-flask
```

Now we are going to run the following command from the same directory where the docker-compose.yml file is located. The docker compose up command will start and run the entire app.

```docker 

docker compose up

``` 

To stop the container running on daemon mode use the below command.

```docker
docker-compose stop
```

