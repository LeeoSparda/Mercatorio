from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/api/certidoes")
def obter_certidoes(cpf_cnpj: str):
    return {
        "cpf_cnpj": cpf_cnpj,
        "certidoes": [
            {
                "tipo": "federal",
                "status": "negativa",
                "conteudo_base64": "base64_fake_content_federal"
            },
            {
                "tipo": "trabalhista",
                "status": "positiva",
                "conteudo_base64": "base64_fake_content_trabalhista"
            }
        ]
    }
