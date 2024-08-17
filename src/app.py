from faker import Faker
from fastapi import FastAPI
import random

app = FastAPI(debug=True)
fake = Faker(locale=['PT-BR'])

@app.get('/')
async def home():
    return [{'message': 'Hello World!'}]

@app.get('/gerar_cliente')
async def gera_funcionario():
    return [{
        'nome_cliente': fake.name(),
        'doc_cliente': fake.cpf(),
        'idade_cliente': random.randrange(18, 64),
        'endereco_cliente': fake.address(),
    }]