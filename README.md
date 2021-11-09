### **Beyonic API Python Examples.** 

The beyonic APIs Docs Reference: https://apidocs.beyonic.com/ , You can discuss Beyonic API on [slack](https://beyonic.com/join-community)

The Beyonic API is a [representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer), REST based application programming interface that lets you extend the Beyonic dashboard features into your application and systems, allowing you to build amazing payment experiences. 

**With the Beyonic API you can:**
- Receive and send money  and prepaid airtime.
- List currencies and networks supported by the Beyonic API.
- Check whether a bank is supported by the Beyonic API.
- View your account transactions history.
- Add, retrieve, list, and update contacts to your Beyonic account.
- Use webhooks to send notifications to URLs on your server that when specific events occur in your Beyonic account (e.g. payments).


### **Getting Help**
For usage, general questions, and discussions the best place to go to is [Beyhive Slack Community](https://beyonic.com/join-community), also feel free to clone and edit this repository to meet your project, application or system requirements.

To start using the Beyonic Python API, you need to start by downloading the Beyonic API official Python client library and setting your secret key.

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

# Listing account: Working. 
accounts = beyonic.Account.list() 
print(accounts)


#Listing currencies: Not working yet.
'''
supported_currencies = beyonic.Currency.list()
print(supported_currencies)

Supported currencies are: USD, UGX, KES, BXC, GHS, TZS, RWF, ZMW, MWK, BIF, EUR, XAF, GNF, XOF, XOF
'''

#Listing networks: Not working yet.
"""
networks = beyonic.Network.list()
print(networks)
"""

#Listing transactions: Working. 
transactions = beyonic.Transaction.list()
print(transactions) 

#Listing contact: Working. 
mycontacts = beyonic.Contact.list() 
print(mycontacts) 


#Listing events: Not working yet.
'''
events = beyonic.Event.list()
print(events)

Error: AttributeError: module 'beyonic' has no attribute 'Event'
'''

```

**Docker file**

```Dockerfile
FROM python:3.8-slim-buster

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
    command: python getExamples.py
    volumes:
      - .:/pythonBeyonicExamples
```

Now we are going to run the following command from the same directory where the docker-compose.yml file is located. The docker compose up command will start and run the entire app.

```docker 

docker compose up

``` 

### **Output** 
**NB:** The screenshot below might differ according to your account deatils and your transcations in deatils. 

![docker compose up preview](https://github.com/HarunMbaabu/BeyonicAPI-Python-Examples/blob/main/Resources%20/Screenshot%202021-10-06%20at%2015.27.12.png)

To stop the container running on daemon mode use the below command.

```docker
docker compose stop
```

**Output**

![docker compose preview](https://github.com/HarunMbaabu/BeyonicAPI-Python-Examples/blob/main/Resources%20/compose%20down.png)


Contributing to this repository. 
All contributions, bug reports, bug fixes, enhancements, and ideas are welcome, You can get in touch with me on twitter [@HarunMbaabu](https://twitter.com/HarunMbaabu).
