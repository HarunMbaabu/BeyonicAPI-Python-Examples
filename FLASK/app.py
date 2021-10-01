import os
import beyonic
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)  
myapi = os.environ['BEYONIC_ACCESS_KEY']

@app.route("/")
def index():
    return "Hello World"

#creating payment
@app.route("/payment", methods = ['POST', 'GET'])
def makepayment():
    if request.method == "POST":
        data = request.form
        phonenumber = data['phonenumber']
        first_name = data["first_name"]
        last_name = data['last_name']
        amount = data['amount']
        currency = data['currency']
        description = data['description']
        callback_url='https://my.website/payments/callback',
        
        payment = beyonic.Payment.create(
                       phonenumber = phonenumber,
                       first_name = first_name,
                       last_name = last_name, 
                       amount = amount,
                       currency = currency,
                       description = description,
                       callback_url = callback_url
                       #metadata={'id': '1234', 'name': 'Lucy'}
                       )
        return 'success'               
    return render_template('payments.html')

#list all your transactions
@app.route("/transactions")
def transactions ():
    transactions  = beyonic.Transaction.list()
    return transactions 



if __name__ == '__main__':
    app.run(debug=True)