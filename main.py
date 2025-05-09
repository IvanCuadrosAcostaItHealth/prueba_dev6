from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

TOKEN_VALIDO = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjQwNDAxODczNjgiLCJuYmYiOjE3NDU1MTAyMjYsImV4cCI6MTc0NTUxMzgyNiwiaWF0IjoxNzQ1NTEwMjI2fQ.hMzyK85g_emAWKQXOTaPrmFrVi5Y04mkvyvjJuBpA80"

@app.get("/login")
def login(usuario: str = None, contrasenia: str = None):
    if usuario is None or contrasenia is None:
        raise HTTPException(status_code=500, detail="Parámetros faltantes")

    if usuario == "pruebaMovil" and contrasenia == "desarrollador123":
        return {"estado": True, "token": TOKEN_VALIDO}
    else:
        return {"estado": False, "token": ""}

class TokenRequest(BaseModel):
    token: str

@app.post("/obtenerData")
async def obtener_data(request: Request):
    try:
        data = await request.json()
        token = data.get("token")
    except Exception:
        raise HTTPException(status_code=500, detail="Estructura del body incorrecta")

    if token != TOKEN_VALIDO:
        return {"status": False, "data": []}

    return {
        "status": True,
        "data": [
            {"fecha": "01/01/2025", "sistólica": 120, "diastólica": 80},
            {"fecha": "02/01/2025", "sistólica": 115, "diastólica": 75},
            {"fecha": "03/01/2025", "sistólica": 129, "diastólica": 80},
            {"fecha": "04/01/2025", "sistólica": 135, "diastólica": 90},
            {"fecha": "05/01/2025", "sistólica": 89, "diastólica": 60},
            {"fecha": "06/01/2025", "sistólica": 70, "diastólica": 50},
            {"fecha": "07/01/2025", "sistólica": 120, "diastólica": 80},
            {"fecha": "08/01/2025", "sistólica": 120, "diastólica": 80},
            {"fecha": "09/01/2025", "sistólica": 150, "diastólica": 80},
            {"fecha": "10/01/2025", "sistólica": 160, "diastólica": 90},
            {"fecha": "11/01/2025", "sistólica": 89, "diastólica": 59},
            {"fecha": "12/01/2025", "sistólica": 120, "diastólica": 60},
            {"fecha": "13/01/2025", "sistólica": 120, "diastólica": 55},
            {"fecha": "14/01/2025", "sistólica": 150, "diastólica": 90},
            {"fecha": "15/01/2025", "sistólica": 115, "diastólica": 75}
        ]
    }