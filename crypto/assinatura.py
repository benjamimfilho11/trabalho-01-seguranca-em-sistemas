from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def obter_hash(nome_hash: str):
    nome_hash = nome_hash.upper()

    if nome_hash == "SHA-256":
        return hashes.SHA256()

    if nome_hash == "SHA-512":
        return hashes.SHA512()

    raise ValueError("Hash inválido. Use SHA-256 ou SHA-512.")


def assinar_mensagem(
    mensagem_cifrada_codificada: bytes,
    chave_privada,
    nome_hash: str
) -> bytes:

    algoritmo_hash = obter_hash(nome_hash)

    assinatura = chave_privada.sign(
        mensagem_cifrada_codificada,
        padding.PKCS1v15(),
        algoritmo_hash
    )

    return assinatura


def verificar_assinatura(
    mensagem_cifrada_codificada: bytes,
    assinatura: bytes,
    chave_publica,
    nome_hash: str
) -> bool:

    algoritmo_hash = obter_hash(nome_hash)

    try:
        chave_publica.verify(
            assinatura,
            mensagem_cifrada_codificada,
            padding.PKCS1v15(),
            algoritmo_hash
        )

        return True

    except Exception:
        return False