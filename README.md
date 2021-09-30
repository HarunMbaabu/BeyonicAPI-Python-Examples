### **Beyonic API Python Examples.** 


**Install the Beyonic API Python Official client library** 


```python
pip install beyonic
```


**Using the python-dotenv module.** 

Create a .env file using the following commands on your terminal or power shell.

```bash 
>>>touch .env
``` 

Inside your .env file specify the Beyonic API okey, get your API Token by clicking your user name on the bottom left of the left sidebar menu in the Beyonic web portal and selecting ‘Manage my account’ from the dropdown menu. The API Token is shown at the very bottom of the page.


**.env file** 
```python
BEYONIC_ACCESS_KEY = "Enter your API "
```

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

