from prefect import task, flow, logging
import random
import time

FLOW_INTERVAL_SECONDS = 10
DRIFT_THRESHOLD = 0.5
RETRAIN_RETRIES = 2
RETRY_DELAY_SECONDS = 5

@task(retries=RETRAIN_RETRIES, retry_delay_seconds=RETRY_DELAY_SECONDS, log_prints=True)
def detect_drift() -> tuple[float, bool]:
    score = random.random()
    drift_detected = score < DRIFT_THRESHOLD
    
    print(f"[DRIFT_CHECK] Score généré : {score}")
    
    if drift_detected:
        print(f"[ALERT] Dérive détectée, réentraînement nécessaire")
    else:
        print(f"[OK] Pas de dérive détectée")

    return score, drift_detected

@task(retries=RETRAIN_RETRIES, retry_delay_seconds=RETRY_DELAY_SECONDS, log_prints=True)
def retrain_model(score: float):
    print(f"[RETRAIN] Démarrage du réentraînement suite au score: {score}")
    time.sleep(10)

    # Exception pour simuler un échec du réentraînement
    if random.random() < 0.2:
        print(f"[RETRAIN] Échec du réentraînement, prefect va retenter {RETRAIN_RETRIES} fois")
    else:
        print(f"[RETRAIN] Réentraînement terminé avec succès")


@flow(name="monitoring-drift-flow", log_prints=True)
def monitoring_flow():
    score, drift_detected = detect_drift()
    
    if drift_detected:
        retrain_model(score)
    else:
        print(f"[OK] modèle stable, aucune action nécessaire")
        

if __name__ == "__main__":
    monitoring_flow.serve(
        name="monitoring-drift-flow",
        interval=FLOW_INTERVAL_SECONDS,
    )
    