from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    logging.info("Petición recibida en /")
    return {"mensaje": "Hola desde el microservicio con Sidecar"}

