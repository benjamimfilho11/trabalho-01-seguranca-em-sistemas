import base64


def codificar_dados(dados: bytes, codificacao: str) -> str:
    codificacao = codificacao.lower()

    if codificacao == "base64":
        return base64.b64encode(dados).decode("utf-8")

    if codificacao == "hex":
        return dados.hex()

    raise ValueError("Codificação inválida. Use 'Base64' ou 'Hex'.")


def decodificar_dados(dados: str, codificacao: str) -> bytes:
    codificacao = codificacao.lower()

    if codificacao == "base64":
        return base64.b64decode(dados)

    if codificacao == "hex":
        return bytes.fromhex(dados)

    raise ValueError("Codificação inválida. Use 'Base64' ou 'Hex'.")

