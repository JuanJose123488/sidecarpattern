# 🚀 Sidecar Pattern con FastAPI + Fluentd + Docker Compose

Este proyecto implementa el **patrón Sidecar**, donde una aplicación
principal (FastAPI) delega las operaciones de logging a un contenedor
auxiliar (**Fluentd**) encargado de recolectar, transformar y enviar los
logs.

## 📂 Estructura del Proyecto

    SIDE-CAR PATTERN/
    │
    ├── app/
    │   ├── Dockerfile
    │   └── main.py
    │
    ├── fluentd/
    │   ├── Dockerfile
    │   └── fluent.conf
    │
    └── docker-compose.yml

### 🔹 app/main.py

Aplicación básica en **FastAPI**, expone los endpoints y genera logs que
serán enviados al contenedor sidecar (Fluentd).

### 🔹 app/Dockerfile

Construye la imagen de FastAPI.

### 🔹 fluentd/Dockerfile

Construye la imagen de Fluentd.

### 🔹 fluentd/fluent.conf

Define entradas, filtros y salidas de logs.

### 🔹 docker-compose.yml

Orquesta la aplicación y el sidecar.

## 🐳 Ejecución

### Construir e iniciar:

    docker-compose up --build

Docs:

    http://localhost:8000/docs

## 📘 Patrón Sidecar

-   La app envía logs a Fluentd.
-   Fluentd procesa y redirige logs.
-   Desacopla observabilidad de la app.

## ⚙️ Comandos útiles

    docker-compose down
    docker ps
    docker-compose build
