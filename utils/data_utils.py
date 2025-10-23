import json
from utils.config import DATOS_USUARIOS

#Lee usuarios para traducirlos
def leer_usaurios():
    with open(DATOS_USUARIOS,"r" , encoding="utf-8") as data:
        return json.load(data)