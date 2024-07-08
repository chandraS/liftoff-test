from prometheus_client import start_http_server, Counter
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging to file with level DEBUG
logging.basicConfig(filename='service_b.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    logger.info(f"Received data: {data}")
    # Increment the Prometheus counter
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    # Process the received data (for now, just print it)
    return jsonify({"status": "success", "received_data": data})

if __name__ == '__main__':
    # Start Prometheus metrics server
    start_http_server(8000)
    # Start Flask application
    app.run(host='0.0.0.0', port=5000)
