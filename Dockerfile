# 1. On part d'une version légère de Python
FROM python:3.9-slim

# 2. On crée un dossier de travail dans le conteneur
WORKDIR /app

# 3. On copie les fichiers de votre PC vers le conteneur
COPY requirements.txt .
COPY app.py .

# 4. On installe les dépendances dans le conteneur
RUN pip install --no-cache-dir -r requirements.txt

# 5. On dit à Docker que l'app écoute sur le port 5000
EXPOSE 5000

# 6. La commande pour lancer l'app quand le conteneur démarre
CMD ["python", "app.py"]