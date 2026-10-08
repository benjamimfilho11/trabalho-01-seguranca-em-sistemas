import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def gerar_chave_aes() -> bytes:
    return os.urandom(32)


def gerar_iv() -> bytes:
    return os.urandom(16)


def cifrar_mensagem(mensagem: bytes, chave: bytes, iv: bytes) -> bytes:
    padder = padding.PKCS7(128).padder()
    mensagem_padded = padder.update(mensagem) + padder.finalize()

    cipher = Cipher(
        algorithms.AES(chave),
        modes.CBC(iv)
    )

    encryptor = cipher.encryptor()

    mensagem_cifrada = (
        encryptor.update(mensagem_padded)
        + encryptor.finalize()
    )

    return mensagem_cifrada


def decifrar_mensagem(mensagem_cifrada: bytes, chave: bytes, iv: bytes) -> bytes:
    cipher = Cipher(
        algorithms.AES(chave),
        modes.CBC(iv)
    )

    decryptor = cipher.decryptor()

    mensagem_padded = (
        decryptor.update(mensagem_cifrada)
        + decryptor.finalize()
    )

    unpadder = padding.PKCS7(128).unpadder()

    mensagem_original = (
        unpadder.update(mensagem_padded)
        + unpadder.finalize()
    )

    return mensagem_original