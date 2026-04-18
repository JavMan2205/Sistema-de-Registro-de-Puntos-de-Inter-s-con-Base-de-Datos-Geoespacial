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

El sistema estará disponible en: http://localhost/

Guía de Uso de la API
Documentación Interactiva (Swagger)
Acceda a la interfaz de pruebas en: http://localhost/docs

Endpoints Principales
Listado General: GET /puntos/ - Muestra todos los POIs (incluyendo los 5 puntos precargados de Guatemala).

Registro de Punto: POST /puntos/ - Permite enviar un JSON con nombre, descripcion, categoria, latitud y longitud.

Filtro Geoespacial: GET /puntos/?lat={lat}&lon={lon}&radio_km={km} - Retorna solo los puntos dentro del radio especificado.

Persistencia y Seguridad
Persistencia: Se utiliza un volumen de Docker (geo_data) para asegurar que la información no se pierda al reiniciar los contenedores.

Redes: Los servicios se comunican a través de una red interna bridge (geo_network), exponiendo únicamente el puerto 80 del proxy al exterior.

Desarrollado por: Javier
Entorno de desarrollo: Intel Core i5 12450H | NVIDIA GTX 1650 | WSL 2 (Ubuntu)
