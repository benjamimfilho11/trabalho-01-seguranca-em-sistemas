from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def gerar_par(nome: str):
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    chave_publica = chave_privada.public_key()

    with open(f"chaves/{nome}_privada.pem", "wb") as arquivo:
        arquivo.write(
            chave_privada.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open(f"chaves/{nome}_publica.pem", "wb") as arquivo:
        arquivo.write(
            chave_publica.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )


gerar_par("remetente")
gerar_par("destinatario")

print("Chaves geradas com sucesso.")