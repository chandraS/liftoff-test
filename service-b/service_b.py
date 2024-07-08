from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    logger.info(f"Received data: {data}")
    # Process the received data (for now, just print it)
    return jsonify({"status": "success", "received_data": data})

@app.route('/health', methods=['GET'])
def health_check():
    # Return a simple status response
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)