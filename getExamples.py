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

Supported currencies are:  
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
