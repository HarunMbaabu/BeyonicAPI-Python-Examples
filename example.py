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

Error:beyonic.errors.ResponseError: 500 error: b'{"detail":"An unexpected error has occurred. Please report to support@beyonic.com. Error Id: None"}'
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