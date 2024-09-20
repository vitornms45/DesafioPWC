from Desafios_PWC import extrair_endereco
import pytest

@pytest.fixture
def endereco_simples():
    return "Miritiba 339"


def test_Passando_Um_Int():
    with pytest.raises(TypeError):
        alo = extrair_endereco(10)

def test_Rua_Numero_Simples(endereco_simples):
    rua, numero = extrair_endereco(endereco_simples)

    assert f"Endereço '{endereco_simples}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço 'Miritiba 339' -> Rua: 'Miritiba', Número: '339'"

def test_Rua_Numero_Simples_02():
    endereco = "Babaçu 500"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço 'Babaçu 500' -> Rua: 'Babaçu', Número: '500'"

def test_Rua_Numero_Com_Sufixo():
    endereco = "Cambuí 804B"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço 'Cambuí 804B' -> Rua: 'Cambuí', Número: '804B'"

def test_Rua_Numero_Com_Espacos():
    endereco = "Rio Branco 23"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço 'Rio Branco 23' -> Rua: 'Rio Branco', Número: '23'" 

def test_Rua_Numero_Com_Espacos_E_Sufixo():
    endereco = "Quirino dos Santos 23 b"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço 'Quirino dos Santos 23 b' -> Rua: 'Quirino dos Santos', Número: '23 b'" 

def test_Numero_No_Inicio():
    endereco = "4, Rue de la République"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço '4, Rue de la République' -> Rua: 'Rue de la République', Número: '4'" 

def test_Numero_No_Inicio_02():
    endereco = "100 Broadway Av"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço '100 Broadway Av' -> Rua: 'Broadway Av', Número: '100'" 

def test_Numero_No_Nome_Da_Rua():
    endereco = "Calle 44 No 1991"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço 'Calle 44 No 1991' -> Rua: 'Calle 44', Número: 'No 1991'" 

def test_Numero_No_Nome_Da_Rua_02():
    endereco = "No 56, Avenida Paulista"
    rua, numero = extrair_endereco(endereco)

    assert f"Endereço '{endereco}' -> Rua: '{rua}', Número: '{numero}'" == "Endereço 'No 56, Avenida Paulista' -> Rua: 'Avenida Paulista', Número: 'No 56'" 
