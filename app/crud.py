from sqlalchemy.orm import Session
from app import models, schemas

def criar_credor_com_precatorio(db: Session, credor: schemas.CredorCreate):
    db_credor = models.Credor(
        nome=credor.nome,
        cpf_cnpj=credor.cpf_cnpj,
        email=credor.email,
        telefone=credor.telefone
    )
    db.add(db_credor)
    db.commit()
    db.refresh(db_credor)

    db_precatorio = models.Precatório(
        numero_precatorio=credor.precatorio.numero_precatorio,
        valor_nominal=credor.precatorio.valor_nominal,
        foro=credor.precatorio.foro,
        data_publicacao=credor.precatorio.data_publicacao,
        credor_id=db_credor.id
    )
    db.add(db_precatorio)
    db.commit()

    return db_credor
