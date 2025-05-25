import requests

BASE_URL = "http://127.0.0.1:8000"

def seed():
    credor_payload = {
        "nome": "João Souza",
        "cpf_cnpj": "11122233344",
        "email": "joao@example.com",
        "telefone": "11998887777",
        "precatorio": {
            "numero_precatorio": "0009876-45.2022.8.26.0050",
            "valor_nominal": 100000.00,
            "foro": "TRF1",
            "data_publicacao": "2023-05-20"
        }
    }

    credor_resp = requests.post(f"{BASE_URL}/credores", json=credor_payload)

    print("\n=== RESPOSTA DO SERVIDOR ===")
    print("Status code:", credor_resp.status_code)
    print("Conteúdo bruto:", credor_resp.text)
    print("============================\n")

    try:
        credor_data = credor_resp.json()
        print("Credor criado com sucesso:", credor_data)
    except Exception as e:
        print("Erro ao converter resposta em JSON:", e)
        return

    credor_id = credor_data.get("id")
    if not credor_id:
        print("ID não encontrado na resposta. Encerrando.")
        return

    # Buscar certidões mockadas
    cert_resp = requests.post(f"{BASE_URL}/credores/{credor_id}/buscar-certidoes")
    print("Certidões:", cert_resp.status_code, cert_resp.text)

if __name__ == "__main__":
    seed()
