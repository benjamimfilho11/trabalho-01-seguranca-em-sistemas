import json

from crypto.aes import gerar_chave_aes, gerar_iv, cifrar_mensagem
from crypto.encoding import codificar_dados
from crypto.rsa import carregar_chave_publica, cifrar_chave_sessao
from crypto.assinatura import assinar_mensagem
from crypto.rsa import carregar_chave_privada


def criar_envelope(
    caminho_mensagem: str,
    caminho_chave_publica_destinatario: str,
    caminho_chave_privada_remetente: str,
    caminho_saida: str,
    codificacao: str,
    hash_oaep: str,
    hash_assinatura: str
):

    with open(caminho_mensagem, "r", encoding="utf-8") as arquivo:
        mensagem = arquivo.read()

    mensagem_bytes = mensagem.encode("utf-8")

    chave_aes = gerar_chave_aes()
    iv = gerar_iv()

    mensagem_cifrada = cifrar_mensagem(
        mensagem_bytes,
        chave_aes,
        iv
    )

    chave_aes_codificada = codificar_dados(
        chave_aes,
        codificacao
    )

    iv_codificado = codificar_dados(
        iv,
        codificacao
    )

    mensagem_cifrada_codificada = codificar_dados(
        mensagem_cifrada,
        codificacao
    )

    chave_publica_destinatario = carregar_chave_publica(
        caminho_chave_publica_destinatario
    )

    chave_sessao_cifrada = cifrar_chave_sessao(
        chave_aes_codificada.encode("utf-8"),
        chave_publica_destinatario,
        hash_oaep
    )

    chave_sessao_cifrada_codificada = codificar_dados(
        chave_sessao_cifrada,
        codificacao
    )

    chave_privada_remetente = carregar_chave_privada(
        caminho_chave_privada_remetente
    )

    assinatura = assinar_mensagem(
        mensagem_cifrada_codificada.encode("utf-8"),
        chave_privada_remetente,
        hash_assinatura
    )

    assinatura_codificada = codificar_dados(
        assinatura,
        codificacao
    )

    envelope = {
        "parametros": {
            "algoritmo_simetrico": "AES-256-CBC",
            "padding_simetrico": "PKCS7",
            "algoritmo_chave": "RSA-OAEP",
            "hash_oaep": hash_oaep,
            "algoritmo_assinatura": "RSA",
            "hash_assinatura": hash_assinatura,
            "codificacao": codificacao
        },

        "envelope": {
            "iv": iv_codificado,
            "chave_sessao": chave_sessao_cifrada_codificada,
            "mensagem_cifrada": mensagem_cifrada_codificada,
            "assinatura": assinatura_codificada
        }
    }

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        json.dump(
            envelope,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    return envelope