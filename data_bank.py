from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

def export_items_to_csv():
  with open('rates.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
     for rate in item['rates']:
       writer.writerow({'currency': rate['currency'], 'code': rate['code'], 'bid': rate['bid'],  'ask': rate['ask']})

items = []  
@app.route("/currency")
def currency():
 with open('rates.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
   items.append({'code':row['code'], 'ask':float(row['ask'])})
 return render_template("currency_calculator.html", items=items)

@app.route("/currency", methods=["get", "post"])
def amount():
 name1 = request.form['code']
 name2 = int(request.form['name'])
 for item in items:
   if name1==item['code']:
    cost = round(item['ask'] * name2, 2)
 return render_template("currency_calculator.html", name1=name1, name2=name2, items=items, cost=cost)

if __name__ =='__main__':
 app.run(debug=True)