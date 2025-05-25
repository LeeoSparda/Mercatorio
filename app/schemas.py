from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum

class TipoDocumento(str, Enum):
    identidade = "identidade"
    comprovante_residencia = "comprovante_residencia"

class TipoCertidao(str, Enum):
    federal = "federal"
    estadual = "estadual"
    municipal = "municipal"
    trabalhista = "trabalhista"

class StatusCertidao(str, Enum):
    negativa = "negativa"
    positiva = "positiva"
    invalida = "invalida"
    pendente = "pendente"

class OrigemCertidao(str, Enum):
    manual = "manual"
    api = "api"

class PrecatórioCreate(BaseModel):
    numero_precatorio: str
    valor_nominal: float
    foro: str
    data_publicacao: datetime

class CredorCreate(BaseModel):
    nome: str
    cpf_cnpj: str
    email: EmailStr
    telefone: str
    precatorio: PrecatórioCreate

class DocumentoCreate(BaseModel):
    tipo: TipoDocumento

class CertidaoCreate(BaseModel):
    tipo: TipoCertidao
    origem: OrigemCertidao
    status: StatusCertidao

class CredorOut(BaseModel):
    id: int
    nome: str
    cpf_cnpj: str
    email: str
    telefone: str

    class Config:
        orm_mode = True
