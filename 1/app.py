from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

# Налаштування логів
logging.basicConfig(level=logging.INFO)

# 
@app.route('/')
def index():
    return "Welcome to the DevOps Test App", 200


# Ендпоінт для HTTPS запитів
@app.route('/https', methods=['GET', 'POST'])
def https_trigger():
    data = {
        "headers": dict(request.headers),
        "method": request.method,
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(),
    }
    app.logger.info(f"HTTPS Request: {data}")
    return {"status": "success", "data": data}, 200

# Ендпоінт для Scheduler
@app.route('/scheduler', methods=['POST'])
def scheduler_trigger():
    timestamp = datetime.now().isoformat()
    payload = request.get_json()
    app.logger.info(f"Scheduler Triggered at {timestamp} with payload: {payload}")
    return {"status": "success", "timestamp": timestamp, "payload": payload}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
