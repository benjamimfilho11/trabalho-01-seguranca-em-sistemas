from crypto.encoding import codificar_dados, decodificar_dados


def test_base64():
    dados = b"seguranca"

    codificado = codificar_dados(dados, "Base64")
    recuperado = decodificar_dados(codificado, "Base64")

    assert recuperado == dados


def test_hex():
    dados = b"seguranca"

    codificado = codificar_dados(dados, "Hex")
    recuperado = decodificar_dados(codificado, "Hex")

    assert recuperado == dados