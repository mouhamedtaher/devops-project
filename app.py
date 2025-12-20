import logging
from flask import Flask, jsonify, request
# 1. Import de la librairie de métriques
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# 2. Initialisation des métriques (Cela crée la route /metrics automatiquement)
metrics = PrometheusMetrics(app)

# --- CONFIGURATION LOGGING ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- BASE DE DONNÉES SIMULÉE ---
tasks = [
    {"id": 1, "title": "Initialiser le projet DevOps", "done": True},
    {"id": 2, "title": "Configurer GitHub Actions", "done": True}
]

# --- ROUTES ---

@app.route('/')
def home():
    logger.info("Accès à la racine")
    return jsonify({"message": "DevOps Project API is running!", "version": "1.0.0"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    logger.info("Récupération de la liste des tâches")
    return jsonify({"tasks": tasks, "count": len(tasks)})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        logger.error("Erreur: Tentative d'ajout sans titre")
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "done": False
    }
    tasks.append(new_task)
    logger.info(f"Nouvelle tâche créée: {new_task['title']}")
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)