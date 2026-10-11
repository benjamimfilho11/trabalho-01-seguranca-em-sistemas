import os


def validar_arquivo_existe(caminho: str):
    if not os.path.isfile(caminho):
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho}"
        )


def validar_codificacao(codificacao: str):
    if codificacao not in ["Base64", "Hex"]:
        raise ValueError(
            "Codificação inválida. Use Base64 ou Hex."
        )


def validar_hash(nome_hash: str):
    if nome_hash not in ["SHA-256", "SHA-512"]:
        raise ValueError(
            "Hash inválido. Use SHA-256 ou SHA-512."
        )


def validar_estrutura_envelope(dados: dict):
    if "parametros" not in dados:
        raise ValueError(
            "Campo 'parametros' ausente no envelope."
        )

    if "envelope" not in dados:
        raise ValueError(
            "Campo 'envelope' ausente no envelope."
        )

    parametros = dados["parametros"]
    envelope = dados["envelope"]

    campos_parametros = [
        "algoritmo_simetrico",
        "padding_simetrico",
        "algoritmo_chave",
        "hash_oaep",
        "algoritmo_assinatura",
        "hash_assinatura",
        "codificacao"
    ]

    campos_envelope = [
        "iv",
        "chave_sessao",
        "mensagem_cifrada",
        "assinatura"
    ]

    for campo in campos_parametros:
        if campo not in parametros:
            raise ValueError(
                f"Campo ausente em parametros: {campo}"
            )

    for campo in campos_envelope:
        if campo not in envelope:
            raise ValueError(
                f"Campo ausente no envelope: {campo}"
            )

    if parametros["algoritmo_simetrico"] != "AES-256-CBC":
        raise ValueError(
            "Algoritmo simétrico inválido."
        )

    if parametros["padding_simetrico"] != "PKCS7":
        raise ValueError(
            "Padding simétrico inválido."
        )

    if parametros["algoritmo_chave"] != "RSA-OAEP":
        raise ValueError(
            "Algoritmo de chave inválido."
        )

    if parametros["algoritmo_assinatura"] != "RSA":
        raise ValueError(
            "Algoritmo de assinatura inválido."
        )

    validar_hash(parametros["hash_oaep"])
    validar_hash(parametros["hash_assinatura"])
    validar_codificacao(parametros["codificacao"])