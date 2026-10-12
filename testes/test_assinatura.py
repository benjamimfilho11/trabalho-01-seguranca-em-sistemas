from crypto.rsa import (
    carregar_chave_publica,
    carregar_chave_privada
)

from crypto.assinatura import (
    assinar_mensagem,
    verificar_assinatura
)


def test_assinatura_valida():
    chave_privada = carregar_chave_privada(
        "chaves/remetente_privada.pem"
    )

    chave_publica = carregar_chave_publica(
        "chaves/remetente_publica.pem"
    )

    mensagem = b"mensagem cifrada em Base64"

    assinatura = assinar_mensagem(
        mensagem,
        chave_privada,
        "SHA-256"
    )

    resultado = verificar_assinatura(
        mensagem,
        assinatura,
        chave_publica,
        "SHA-256"
    )

    assert resultado is True


def test_assinatura_invalida():
    chave_privada = carregar_chave_privada(
        "chaves/remetente_privada.pem"
    )

    chave_publica = carregar_chave_publica(
        "chaves/remetente_publica.pem"
    )

    mensagem = b"mensagem original"

    assinatura = assinar_mensagem(
        mensagem,
        chave_privada,
        "SHA-256"
    )

    resultado = verificar_assinatura(
        b"mensagem alterada",
        assinatura,
        chave_publica,
        "SHA-256"
    )

    assert resultado is False