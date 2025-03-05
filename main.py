from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI()

# Definimos el modelo de datos para los videojuegos
class Videojuego(BaseModel):
    id: Optional[int] = None
    nombre: str
    genero: str
    lanzamiento: int
    desarrollador: str

# Ruta al archivo JSON
JSON_FILE = "videojuegos.json"

# Función para cargar los videojuegos desde el archivo JSON
def cargar_videojuegos():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as file:
            json.dump([], file)
    with open(JSON_FILE, "r") as file:
        return json.load(file)

# Función para guardar los videojuegos en el archivo JSON
def guardar_videojuegos(videojuegos: List[dict]):
    with open(JSON_FILE, "w") as file:
        json.dump(videojuegos, file, indent=4)

# Ruta para obtener todos los videojuegos
@app.get("/videojuegos", response_model=List[Videojuego])
def obtener_videojuegos():
    return cargar_videojuegos()

# Ruta para obtener un videojuego por ID
@app.get("/videojuegos/{videojuego_id}", response_model=Videojuego)
def obtener_videojuego(videojuego_id: int):
    videojuegos = cargar_videojuegos()
    for videojuego in videojuegos:
        if videojuego["id"] == videojuego_id:
            return videojuego
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")

# Ruta para crear un nuevo videojuego
@app.post("/videojuegos", response_model=Videojuego)
def crear_videojuego(videojuego: Videojuego):
    videojuegos = cargar_videojuegos()

    # Calcular el siguiente ID disponible
    if videojuegos:
        ultimo_id = max(videojuego["id"] for videojuego in videojuegos)
        nuevo_id = ultimo_id + 1
    else:
        nuevo_id = 1  

    videojuego.id = nuevo_id

    videojuegos.append(videojuego.dict())
    guardar_videojuegos(videojuegos)

    return videojuego

# Ruta para actualizar un videojuego existente
@app.put("/videojuegos/{videojuego_id}", response_model=Videojuego)
def actualizar_videojuego(videojuego_id: int, videojuego_actualizado: Videojuego):
    videojuegos = cargar_videojuegos()
    for i, videojuego in enumerate(videojuegos):
        if videojuego["id"] == videojuego_id:
            # Forzar el ID original y actualizar el resto de los campos
            videojuego_actualizado.id = videojuego_id  # Asegurar que el ID no cambie
            videojuegos[i] = videojuego_actualizado.dict()
            guardar_videojuegos(videojuegos)
            return videojuego_actualizado
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")
# Ruta para eliminar un videojuego
@app.delete("/videojuegos/{videojuego_id}", response_model=Videojuego)
def eliminar_videojuego(videojuego_id: int):
    videojuegos = cargar_videojuegos()
    for i, videojuego in enumerate(videojuegos):
        if videojuego["id"] == videojuego_id:
            videojuego_eliminado = videojuegos.pop(i)
            guardar_videojuegos(videojuegos)
            return videojuego_eliminado
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")

# Iniciar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)