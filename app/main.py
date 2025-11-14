import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/mensaje")
def mensaje(texto: str = Query(...)):
    saludo = f"Hola, {texto}!"
    logging.info(f"Saludando con: {saludo}")
    return {"mensaje": saludo}

