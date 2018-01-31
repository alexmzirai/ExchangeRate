from flask import Flask, render_template
import os
import json
import urllib2
from bs4 import BeautifulSoup


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')  # path to the templates folder--

app = Flask(__name__, template_folder='tmpl_dir')


def get_exchange_rates():
    rates = []  # rate initially set to an empty list
    response = urllib2.urlopen('http://api.bitcoincharts.com/v1/weighted_prices.json')  # fetch the data using urllib2
    data = response.read()     # read the data received from the response
    rdata = json.loads(data, parse_float=float)  # parse the json data from the url

    rates.append(rdata['rates']['USD'])
    rates.append(rdata['rates']['GBP'])
    rates.append(rdata['rates']['JPY'])
    rates.append(rdata['rates']['AUD'])
    return rates

    # rates = []
    # url = 'http://api.bitcoincharts.com/v1/weighted_prices.json'
    # http = urllib3.PoolManager()
    # response = http.request('GET', url)
    # soup = BeautifulSoup(response.data.decode('utf-8'))
    # data = response.read()
    # rdata = json.loads(data, parse_float=float)

    # rates.append(rdata['rates']['USD'])
    # rates.append(rdata['rates']['GBP'])
    # rates.append(rdata['rates']['JPY'])
    # rates.append(rdata['rates']['AUD'])


rates = get_exchange_rates()
print(rates)


@app.route('/')
def index():
    rates = get_exchange_rates()
    return render_template('test.html', **locals())


if __name__ == '__main__':
    app.run()
