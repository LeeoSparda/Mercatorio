from fastapi import APIRouter

router = APIRouter()

@router.get("/api/certidoes")
def get_certidoes_mock(cpf_cnpj: str):
    return {
        "cpf_cnpj": cpf_cnpj,
        "certidoes": [
            {
                "tipo": "federal",
                "status": "negativa",
                "conteudo_base64": "base64_federal_simulada"
            },
            {
                "tipo": "trabalhista",
                "status": "positiva",
                "conteudo_base64": "base64_trabalhista_simulada"
            }
        ]
    }
