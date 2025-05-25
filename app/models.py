from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum
import datetime

Base = declarative_base()

class TipoDocumento(str, enum.Enum):
    identidade = "identidade"
    comprovante_residencia = "comprovante_residencia"

class TipoCertidao(str, enum.Enum):
    federal = "federal"
    estadual = "estadual"
    municipal = "municipal"
    trabalhista = "trabalhista"

class StatusCertidao(str, enum.Enum):
    negativa = "negativa"
    positiva = "positiva"
    invalida = "invalida"
    pendente = "pendente"

class OrigemCertidao(str, enum.Enum):
    manual = "manual"
    api = "api"

class Credor(Base):
    __tablename__ = "credores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf_cnpj = Column(String, unique=True, index=True)
    email = Column(String)
    telefone = Column(String)
    precatorio = relationship("Precatório", back_populates="credor", uselist=False)
    documentos = relationship("DocumentoPessoal", back_populates="credor")
    certidoes = relationship("Certidao", back_populates="credor")

class Precatório(Base):
    __tablename__ = "precatorios"
    id = Column(Integer, primary_key=True, index=True)
    numero_precatorio = Column(String)
    valor_nominal = Column(Float)
    foro = Column(String)
    data_publicacao = Column(DateTime)
    credor_id = Column(Integer, ForeignKey("credores.id"))
    credor = relationship("Credor", back_populates="precatorio")

class DocumentoPessoal(Base):
    __tablename__ = "documentos"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoDocumento))
    arquivo_url = Column(String)
    enviado_em = Column(DateTime, default=datetime.datetime.utcnow)
    credor_id = Column(Integer, ForeignKey("credores.id"))
    credor = relationship("Credor", back_populates="documentos")

class Certidao(Base):
    __tablename__ = "certidoes"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoCertidao))
    status = Column(Enum(StatusCertidao))
    origem = Column(Enum(OrigemCertidao))
    conteudo_base64 = Column(String, nullable=True)
    arquivo_url = Column(String, nullable=True)
    recebida_em = Column(DateTime, default=datetime.datetime.utcnow)
    credor_id = Column(Integer, ForeignKey("credores.id"))
    credor = relationship("Credor", back_populates="certidoes")
