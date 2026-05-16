import pytest
from app import app, PRODUTOS

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    PRODUTOS.clear()
    PRODUTOS.append({"id": 1, "nome": "Teclado Mecânico", "preco": 350.0})


def test_listar_produtos_deve_retornar_status_200_e_lista(client):
    resposta = client.get('/produtos')
    
    assert resposta.status_code == 200
    assert isinstance(resposta.get_json(), list)
    assert resposta.get_json()[0]['nome'] == "Teclado Mecânico"

def test_criar_produto_com_sucesso(client):
    novo_produto = {"nome": "Mouse Gamer", "preco": 150.0}
    resposta = client.post('/produtos', json=novo_produto)
    
    assert resposta.status_code == 201
    dados_retornados = resposta.get_json()
    assert dados_retornados['id'] == 2
    assert dados_retornados['nome'] == "Mouse Gamer"


def test_criar_produto_sem_corpo_da_requisicao_deve_retornar_400(client):
    resposta = client.post('/produtos', json={})
    
    assert resposta.status_code == 400
    assert "erro" in resposta.get_json()

def test_criar_produto_faltando_atributos_deve_retornar_400(client):
    dados_incompletos = {"nome": "Monitor 144hz"}
    resposta = client.post('/produtos', json=dados_incompletos)
    
    assert resposta.status_code == 400
    assert resposta.get_json()["erro"] == "Dados inválidos"