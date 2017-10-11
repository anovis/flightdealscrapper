import sys
sys.path.append("..")
from flask import Flask, jsonify
from flask_cors import CORS
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

if __name__ == '__main__':
    app.run(debug=True)