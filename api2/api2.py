from flask import Flask, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/sawasdeekub', methods=['GET'])
def hello():
    app.logger.info('API2: Received request at /sawasdeekub')
    return jsonify({"message": "sawasdeekub from API2!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)