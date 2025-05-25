from fastapi import FastAPI
from app.database import Base, engine
from app.routers import credor, documentos, certidoes, mock
from app.jobs import iniciar_jobs

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API Mercatório"}

app.include_router(credor.router)
app.include_router(documentos.router)
app.include_router(certidoes.router)
app.include_router(mock.router)

iniciar_jobs()
