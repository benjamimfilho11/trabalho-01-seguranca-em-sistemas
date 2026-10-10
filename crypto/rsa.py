from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding


def carregar_chave_publica(caminho: str):
    with open(caminho, "rb") as arquivo:
        chave = serialization.load_pem_public_key(
            arquivo.read()
        )

    return chave


def carregar_chave_privada(caminho: str):
    with open(caminho, "rb") as arquivo:
        chave = serialization.load_pem_private_key(
            arquivo.read(),
            password=None
        )

    return chave


def obter_hash(nome_hash: str):
    nome_hash = nome_hash.upper()

    if nome_hash == "SHA-256":
        return hashes.SHA256()

    if nome_hash == "SHA-512":
        return hashes.SHA512()

    raise ValueError("Hash inválido. Use SHA-256 ou SHA-512.")


def cifrar_chave_sessao(
    chave_sessao_codificada: bytes,
    chave_publica,
    nome_hash: str
) -> bytes:

    algoritmo_hash = obter_hash(nome_hash)

    chave_cifrada = chave_publica.encrypt(
        chave_sessao_codificada,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=algoritmo_hash
            ),
            algorithm=algoritmo_hash,
            label=None
        )
    )

    return chave_cifrada


def decifrar_chave_sessao(
    chave_sessao_cifrada: bytes,
    chave_privada,
    nome_hash: str
) -> bytes:

    algoritmo_hash = obter_hash(nome_hash)

    chave_decifrada = chave_privada.decrypt(
        chave_sessao_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=algoritmo_hash
            ),
            algorithm=algoritmo_hash,
            label=None
        )
    )

    return chave_decifrada