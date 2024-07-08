import os
import requests
import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the Service B URL from environment variable
service_b_url = os.getenv('SERVICE_B_URL')

@app.route('/send', methods=['GET'])
def send_data():
    data = {"message": "Hello from Service A"}
    logger.info(f"Sending data to {service_b_url}")
    response = requests.post(f"{service_b_url}/data", json=data)
    logger.info(f"Received response: {response.status_code} - {response.text}")
    return jsonify({"status": "data sent", "response": response.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)