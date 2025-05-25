from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.models import Certidao, TipoCertidao, OrigemCertidao, StatusCertidao
from app.database import get_db
from datetime import datetime
import shutil
import os

router = APIRouter()
UPLOAD_DIR = "uploads/certidoes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/credores/{credor_id}/certidoes")
def upload_certidao_manual(
    credor_id: int,
    tipo: TipoCertidao = Form(...),
    status: StatusCertidao = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    caminho = f"{UPLOAD_DIR}/{credor_id}_{file.filename}"
    with open(caminho, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    certidao = Certidao(
        tipo=tipo,
        status=status,
        origem=OrigemCertidao.manual,
        arquivo_url=caminho,
        credor_id=credor_id,
        recebida_em=datetime.utcnow()
    )
    db.add(certidao)
    db.commit()
    db.refresh(certidao)
    return {"message": "Certidão enviada com sucesso"}
