# M6 - Brief 1 - Monitoring de dérive avec Prefect

Pipeline Prefect simulant la surveillance continue d'un modèle IA en production

## Structure du projet

```
m6-brief-1/
├── README.md
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── flow.py
```

## Lancement avec Docker

```bash
docker compose up --build
```

L'UI Prefect est accessible sur http://localhost:4200

## Lancement en local

```bash
pip install -r requirements.txt
prefect server start
```

Dans un second terminal :

```bash
export PREFECT_API_URL=http://127.0.0.1:4200/api
python flow.py
```

## Fonctionnement

Le pipeline s'exécute toutes les 10 secondes. Il génère un score aléatoire entre 0 et 1
Si le score est inférieur à 0.5, une dérive est détectée et un réentraînement est déclenché.
Les logs sont visibles dans l'UI Prefect
