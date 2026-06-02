FROM prefecthq/prefect:3-latest

WORKDIR /app

# on copie les dépendances en premier pour profiter du cache docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flow.py .

# URL de l'API Prefect pointe vers le service prefect-server du compose
ENV PYTHONIOENCODING=utf-8
ENV PREFECT_API_URL=http://prefect-server:4200/api

# lancement du pipeline serve() gère le scheduler et le worker
CMD ["python", "flow.py"]