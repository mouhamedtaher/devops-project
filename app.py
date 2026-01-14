import logging
import uuid
import time
from flask import Flask, jsonify, request, g
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# --- METRICS ---
metrics = PrometheusMetrics(app)

# --- TRACING & LOGGING CONFIGURATION ---
# On configure les logs pour qu'ils soient lisibles
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [TraceID: %(trace_id)s] - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Ce filtre permet d'injecter le TraceID dans chaque ligne de log
class TraceIdFilter(logging.Filter):
    def filter(self, record):
        # Si la requête a un ID, on l'utilise, sinon 'N/A'
        record.trace_id = getattr(g, 'request_id', 'N/A')
        return True

logger.addFilter(TraceIdFilter())

# --- MIDDLEWARE TRACING ---
@app.before_request
def start_trace():
    # 1. Générer un ID unique pour chaque visiteur
    g.request_id = str(uuid.uuid4())
    g.start_time = time.time()
    # 2. On loggue le début de la requête avec son ID
    logger.info(f"Reçu: {request.method} {request.path}")

@app.after_request
def end_trace(response):
    # 3. Calculer la durée
    duration = time.time() - g.start_time
    # 4. Ajouter le Trace ID dans l'en-tête de la réponse (pour le client)
    response.headers['X-Trace-Id'] = g.request_id
    logger.info(f"Répondu: {response.status} en {duration:.4f}s")
    return response

# --- DONNÉES ---
tasks = [
    {"id": 1, "title": "Faire le Tracing", "done": True},
    {"id": 2, "title": "Configurer DAST", "done": False}
]

# --- ROUTES ---
@app.route('/')
def home():
    logger.info("Traitement de la page d'accueil")
    return jsonify({
        "message": "DevOps Project Final Version", 
        "version": "version": "3.0.0-FORCE",
        "trace_id": g.request_id
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    logger.info(f"Récupération de {len(tasks)} tâches")
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        logger.error("Échec ajout: Titre manquant")
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {"id": len(tasks) + 1, "title": data['title'], "done": False}
    tasks.append(new_task)
    logger.info(f"Tâche ajoutée: {new_task['title']}")
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # nosec