from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import database, crud, schemas

router = APIRouter()

@router.post("/credores", response_model=schemas.CredorOut)
def criar_credor(credor: schemas.CredorCreate, db: Session = Depends(database.get_db)):
    return crud.criar_credor_com_precatorio(db, credor)
