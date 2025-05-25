from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import DocumentoPessoal, TipoDocumento
import shutil
import os
from datetime import datetime

router = APIRouter()

UPLOAD_DIR = "uploads/documentos"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/credores/{credor_id}/documentos")
def upload_documento(
    credor_id: int,
    tipo: TipoDocumento = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    caminho = f"{UPLOAD_DIR}/{credor_id}_{file.filename}"
    with open(caminho, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    doc = DocumentoPessoal(
        tipo=tipo,
        arquivo_url=caminho,
        credor_id=credor_id,
        enviado_em=datetime.utcnow()
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return {"message": "Documento enviado com sucesso"}
