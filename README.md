# 🚀 DevOps Project: Task Manager API

Ce projet est une démonstration complète d'une chaîne **DevOps** moderne.
Il s'agit d'une API REST (Python/Flask) conteneurisée, automatisée et monitorée.

## 🛠️ Stack Technique

* **Application :** Python, Flask
* **Conteneurisation :** Docker
* **Orchestration :** Docker Compose
* **CI/CD :** GitHub Actions (Build & Push automatique vers Docker Hub)
* **Observabilité :** Prometheus (Collecte) & Grafana (Visualisation)

---

## 🏗️ Architecture

Le projet lance 3 services interconnectés via Docker Compose :
1.  **Web API (Flask) :** L'application principale (Port 5000).
2.  **Prometheus :** Récupère les métriques de l'API toutes les 15s (Port 9090).
3.  **Grafana :** Affiche les tableaux de bord de surveillance (Port 3000).

---

## 🚀 Comment lancer le projet (Quickstart)

Vous avez seulement besoin de **Docker** installé sur votre machine.

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/mouhamedtaher/devops-project.git](https://github.com/mouhamedtaher/devops-project.git)
    cd devops-project
    ```

2.  **Lancer la stack complète :**
    ```bash
    docker-compose up --build
    ```

3.  **Accéder aux services :**
    * 🌍 **API :** `http://localhost:5000`
    * 📊 **Grafana :** `http://localhost:3000` (Login: `admin` / `admin`)
    * 🔥 **Prometheus :** `http://localhost:9090`

---

## 📡 API Endpoints

| Méthode | URL | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Vérifier que l'API est en ligne |
| `GET` | `/health` | Healthcheck (pour Kubernetes/Docker) |
| `GET` | `/metrics` | Métriques pour Prometheus |
| `GET` | `/tasks` | Lister toutes les tâches |
| `POST` | `/tasks` | Créer une nouvelle tâche (JSON: `{"title": "..."}`) |

---

## ⚙️ CI/CD Pipeline

Ce projet utilise **GitHub Actions**.
À chaque `push` sur la branche `main`, le pipeline :
1.  🏗️ Construit l'image Docker.
2.  🔑 Se connecte à Docker Hub de manière sécurisée (Secrets).
3.  📦 Pousse la nouvelle image publiquement.

---

## 📊 Monitoring (Configuration Grafana)

Une fois connecté à Grafana (`localhost:3000`) :
1.  Ajoutez une **Data Source** de type **Prometheus**.
2.  URL du serveur : `http://prometheus:9090` (Nom du service Docker).
3.  Importez ou créez un dashboard avec la métrique : `flask_http_request_total`.

---
*Réalisé dans le cadre d'un projet d'apprentissage DevOps.*