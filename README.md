# Mercatorio



## Tecnologias utilizadas

- Python 3.12
- SQLite
- Docker / Docker Compose

## Instalação com Docker

1. Certifique-se de que o Docker e o Docker Compose estão instalados.
2. Clone o repositório:
   ```bash
   git clone https://github.com/LeeoSparda/Mercatorio
   cd mercatorioV2

## Visão Geral

O projeto Mercatório Backend Challenge é uma aplicação desenvolvida em Python com FastAPI que visa simular um sistema de gerenciamento de precatórios, credores, e certidões. O sistema permite:

Cadastro de credores e seus precatórios
Upload de documentos
Simulação automática e manual de certidões
Exportação dos dados em planilhas
Integração com uma API mock de certidões

## Tecnologias Utilizadas

Python 3.12
FastAPI (framework web)
SQLAlchemy (ORM)
SQLite (banco de dados)
Pydantic (validação de dados)
Uvicorn (servidor ASGI)
Requests (requisições HTTP no script seed)

## Estrutura do Projeto

mercatorioV2/
├── app/
│   ├── main.py              
│   ├── models.py            
│   ├── schemas.py           
│   ├── database.py          
│   ├── routes.py            
│   ├── mock_certidoes.py    
│   ├── utils.py             
│   ├── seed.py              
├── static/
│   └── index.html           
├── export/                  
└── requirements.txt         

## Funcionalidades Principais

1. Cadastro de Credores

Endpoint: POST /credores
Payload esperado:

{
  "nome": "João Souza",
  "cpf_cnpj": "11122233344",
  "email": "joao@example.com",
  "telefone": "11998887777"
}

2. Cadastro de Precatórios

Endpoint: POST /precatorios
Payload esperado:

{
  "numero_precatorio": "0009876-45.2022.8.26.0050",
  "valor_nominal": 100000.0,
  "foro": "TRF1",
  "data_publicacao": "2023-05-20",
  "credor_id": 1
}

3. Upload de Documentos

Endpoint: POST /documentos/upload
Permite envio de arquivos vinculados a um credor.

# 4. Simulação de Certidões

Automática: POST /credores/{id}/buscar-certidoes
Integra-se com a API mock mock_certidoes.py.
Manual: POST /certidoes

# 5. Exportação de Planilhas

Endpoint: GET /exportar
Gera e exporta os dados de credores e precatórios em formato Excel.

# 6. Interface HTML

Arquivo static/index.html permite interação básica via navegador.
Script de Popular Dados (seed.py)
Local: app/seed.py
Objetivo: Criar dados iniciais para testes automatizados da API.
Utiliza requests para fazer chamadas HTTP para os endpoints.

Como Executar

1. Instale as dependências:

pip install -r requirements.txt

2. Rode a API:

uvicorn app.main:app --reload

3. Execute o script seed:

python app/seed.py

4. Acesse no navegador:

Interface Swagger: http://127.0.0.1:8000/docs

Interface HTML: http://127.0.0.1:8000/static/index.html
