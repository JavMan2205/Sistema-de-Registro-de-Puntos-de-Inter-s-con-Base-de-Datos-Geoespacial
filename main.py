from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Sistema de Puntos de Interés Geoespacial")

# Configuración de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

# Modelo de datos para recibir información
class PuntoInteres(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    latitud: float
    longitud: float

@app.get("/")
def read_root():
    return {"status": "Online", "message": "API de Puntos de Interés funcionando"}

# 1. Registrar un nuevo punto
@app.post("/puntos/")
def crear_punto(punto: PuntoInteres):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        
        query = """
            INSERT INTO puntos (nombre, descripcion, categoria, ubicacion)
            VALUES (%s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326));
        """
        cur.execute(query, (punto.nombre, punto.descripcion, punto.categoria, punto.longitud, punto.latitud))
        conn.commit()
        return {"message": "Punto registrado exitosamente"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

# 2. Listar puntos con filtro de categoría o radio
@app.get("/puntos/")
def listar_puntos(categoria: Optional[str] = None, lat: Optional[float] = None, lon: Optional[float] = None, radio_km: Optional[float] = None):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT id, nombre, descripcion, categoria, ST_Y(ubicacion::geometry) as lat, ST_X(ubicacion::geometry) as lon FROM puntos WHERE 1=1"
    params = []

    if categoria:
        query += " AND categoria = %s"
        params.append(categoria)
    
    # Filtro geoespacial: ST_DWithin busca en un radio (en metros)
    if lat and lon and radio_km:
        query += " AND ST_DWithin(ubicacion, ST_SetSRID(ST_MakePoint(%s, %s), 4326), %s)"
        params.extend([lon, lat, radio_km * 1000])

    cur.execute(query, params)
    puntos = cur.fetchall()
    cur.close()
    conn.close()
    return puntos