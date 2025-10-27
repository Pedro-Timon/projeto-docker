from fastapi import FastAPI
from pydantic import BaseModel
from producer import send_message

app = FastAPI(title="FastAPI + RabbitMQ")

class Mensagem(BaseModel):
    nome: str
    texto: str

@app.post("/enviar")
def enviar_mensagem(msg: Mensagem):
    send_message(msg.dict())
    return {"status": "mensagem enviada", "conteudo": msg}
