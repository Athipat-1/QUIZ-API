from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

API2_URL = 'http://api2:5001/sawasdeekub'  

@app.route('/sawasdeekub', methods=['GET'])
def hello():
    app.logger.info('API1: Received request at /sawasdeekub')
    try:
        resp = requests.get(API2_URL)
        resp.raise_for_status()
        data = resp.json()
        app.logger.info(f'API1: Response from API2: {data}')
        return jsonify({"message_from_api2": data["message"]})
    except Exception as e:
        app.logger.error(f'API1: Error calling API2: {e}')
        return jsonify({"error": "Failed to get response from API2"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)