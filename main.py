from fastapi import FastAPI, HTTPException
from models import Telemetry
from database import db

app = FastAPI(title="Monitor de Qualidade da Água")

# CREATE
@app.post("/telemetry/")
def create_telemetry(data: Telemetry):
    db.append(data)
    return {"msg": "Dados recebidos com sucesso", "id": len(db)-1}

# READ (listar todos)
@app.get("/telemetry/")
def read_all():
    return db

# READ (um específico pelo índice)
@app.get("/telemetry/{item_id}")
def read_item(item_id: int):
    try:
        return db[item_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item não encontrado")

# UPDATE
@app.put("/telemetry/{item_id}")
def update_item(item_id: int, new_data: Telemetry):
    try:
        db[item_id] = new_data
        return {"msg": "Atualizado com sucesso"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item não encontrado")

# DELETE
@app.delete("/telemetry/{item_id}")
def delete_item(item_id: int):
    try:
        db.pop(item_id)
        return {"msg": "Deletado com sucesso"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item não encontrado")
