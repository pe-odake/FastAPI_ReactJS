from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import conectar

app = FastAPI()

# Liberar acesso do React (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/usuarios")
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Nome FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row.ID, "nome": row.Nome} for row in rows]

# ----------------------------

class Usuario(BaseModel):
    nome: str
    email: str

@app.post("/addUsuarios")
def adicionar_usuarios(usuario: Usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nome, email) VALUES (?, ?)""",
        (usuario.nome, usuario.email)
    )
    conn.commit() 
    conn.close()

# RODAR BACK: uvicorn main:app --reload
