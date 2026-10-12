from crypto.rsa import (
    carregar_chave_publica,
    carregar_chave_privada,
    cifrar_chave_sessao,
    decifrar_chave_sessao
)


def test_rsa_oaep():
    chave_publica = carregar_chave_publica(
        "chaves/destinatario_publica.pem"
    )

    chave_privada = carregar_chave_privada(
        "chaves/destinatario_privada.pem"
    )

    chave_sessao = b"YWJjZGVmZ2hpamtsbW5vcA=="

    cifrada = cifrar_chave_sessao(
        chave_sessao,
        chave_publica,
        "SHA-256"
    )

    decifrada = decifrar_chave_sessao(
        cifrada,
        chave_privada,
        "SHA-256"
    )

    assert decifrada == chave_sessao