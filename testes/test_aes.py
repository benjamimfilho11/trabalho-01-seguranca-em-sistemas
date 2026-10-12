from crypto.aes import (
    gerar_chave_aes,
    gerar_iv,
    cifrar_mensagem,
    decifrar_mensagem
)


def test_aes_cifra_e_decifra():
    chave = gerar_chave_aes()
    iv = gerar_iv()

    mensagem = b"Teste AES"

    cifrada = cifrar_mensagem(
        mensagem,
        chave,
        iv
    )

    decifrada = decifrar_mensagem(
        cifrada,
        chave,
        iv
    )

    assert decifrada == mensagem