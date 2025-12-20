import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

# Logs (requis pour l'observabilité)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tasks = []

@app.route('/')
def home():
    return jsonify({"message": "DevOps API is running", "version": "1.0"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks)+1, "title": data.get('title')}
    tasks.append(task)
    logger.info(f"Task added: {task['title']}")
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)