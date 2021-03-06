import sys
sys.path.append("..")
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import render_template
import emailscrappers

app = Flask(__name__)
CORS(app)

@app.route('/citydeals/<string:city>', methods=['GET'])
def get_deals(city):
    x = emailscrappers.TheFlightDeal(city)
    y = emailscrappers.SecretFlying(city)
    e = emailscrappers.EmailScraper(city, "", [x, y])
    deals = e.call_scrappers()
    return jsonify({'deals': deals})

@app.route('/subscriptions/<string:email>', methods=['GET'])
def get_subscriptions(email):
    return jsonify({'subscriptions': ["Boston", "New York"]})

@app.route('/citydeals/newuser', methods=['POST'])
def new_user():
    req_json = request.get_json()
    print(req_json)

    return "success"



if __name__ == '__main__':
    app.run(debug=True)