# Sistema de Registro de Puntos de Interés (POI) Geoespaciales

Este proyecto consiste en una arquitectura de microservicios diseñada para gestionar puntos de interés geográficos. Permite registrar lugares con coordenadas exactas, categorizarlos y realizar consultas de proximidad (filtros por radio de kilómetros) utilizando capacidades geoespaciales avanzadas.

## Arquitectura del Sistema

El sistema está orquestado mediante **Docker Compose** y se divide en tres capas principales:

1.  **Proxy Reverso (Nginx):** Actúa como puerta de enlace en el puerto 80, redirigiendo el tráfico al backend.
2.  **API REST (FastAPI/Python):** Gestiona la lógica de negocio, validación de datos con Pydantic y comunicación con la base de datos.
3.  **Base de Datos (PostGIS):** Extensión geoespacial de PostgreSQL que permite el almacenamiento y cálculo eficiente de geometrías (puntos, radios, distancias).

## Requisitos Previos

* Docker Desktop (instalado y en ejecución).
* WSL 2 (si se utiliza Windows).

## Instalación y Despliegue

1. Clone el repositorio o sitúese en la carpeta del proyecto.
2. Ejecute el siguiente comando en su terminal para levantar los servicios:

# docker compose up --build
