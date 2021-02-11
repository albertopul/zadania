import json
import requests
import csv
from flask import Flask, render_template, request, redirect
import logging
app = Flask(__name__)

#. Defining columns in cvs file.

rates_data = []

#. FUNCTIONS
    # Obtain data from NBP, create rates_list and export it to kursy.csv
    #1. Loading api.nbp to receive data list by using requests

def get_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    return response.json()[0]['rates']



# Export rates_list to courses.csv
def export_to_csv(rates_data):
    csv_columns = ["currency", "code", "bid", "ask"]
    with open("currency.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=';')
        writer.writeheader()
        for item in rates_data:
            writer.writerow(item)
            

# WEB
    # Create webpage http://localhost:5000/courses


@app.route('/currency/', methods=['GET', 'POST'])
def currency():
    rates_data = get_rates()
    export_to_csv(rates_data)
    codes = []
    
    for item in rates_data:
        codes.append(item['code'])

    message = ""
    if request.method == 'POST':
        bid_rate = ''

        data_form = request.form
        amount = float(data_form.get('amount'))
        code = data_form.get('code')

        for item in rates_data:
            if item['code'] == code:
                bid_rate = float(item['bid'])
                break

        if not bid_rate:
            message = f"Unrecognized code: {code}"
        else:
            message = f"You exchanged {amount} {code} by rate {bid_rate}, which is {amount * bid_rate} PLN"

    return render_template("currency.html", codes=codes, message=message)


if __name__ == "__main__":
    app.run(debug=False)

