from envelope.criar import criar_envelope
from envelope.abrir import abrir_envelope


def test_fluxo_completo(tmp_path):
    mensagem = tmp_path / "mensagem.txt"
    envelope = tmp_path / "envelope.json"
    saida = tmp_path / "saida.txt"

    mensagem.write_text(
        "Teste completo do envelope digital.",
        encoding="utf-8"
    )

    criar_envelope(
        str(mensagem),
        "chaves/destinatario_publica.pem",
        "chaves/remetente_privada.pem",
        str(envelope),
        "Base64",
        "SHA-256",
        "SHA-256"
    )

    resultado = abrir_envelope(
        str(envelope),
        "chaves/destinatario_privada.pem",
        "chaves/remetente_publica.pem",
        str(saida)
    )

    assert resultado == "Teste completo do envelope digital."