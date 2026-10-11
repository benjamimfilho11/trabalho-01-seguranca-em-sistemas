import json

from crypto.aes import decifrar_mensagem
from crypto.encoding import decodificar_dados
from crypto.rsa import carregar_chave_privada, carregar_chave_publica
from crypto.rsa import decifrar_chave_sessao
from crypto.assinatura import verificar_assinatura


def abrir_envelope(
    caminho_envelope: str,
    caminho_chave_privada_destinatario: str,
    caminho_chave_publica_remetente: str,
    caminho_saida: str
):

    with open(caminho_envelope, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    parametros = dados["parametros"]
    envelope = dados["envelope"]

    codificacao = parametros["codificacao"]
    hash_oaep = parametros["hash_oaep"]
    hash_assinatura = parametros["hash_assinatura"]

    iv_codificado = envelope["iv"]
    chave_sessao_cifrada_codificada = envelope["chave_sessao"]
    mensagem_cifrada_codificada = envelope["mensagem_cifrada"]
    assinatura_codificada = envelope["assinatura"]

    chave_publica_remetente = carregar_chave_publica(
        caminho_chave_publica_remetente
    )

    assinatura = decodificar_dados(
        assinatura_codificada,
        codificacao
    )

    assinatura_valida = verificar_assinatura(
        mensagem_cifrada_codificada.encode("utf-8"),
        assinatura,
        chave_publica_remetente,
        hash_assinatura
    )

    if not assinatura_valida:
        raise ValueError(
            "Assinatura inválida. Integridade do envelope violada."
        )

    chave_privada_destinatario = carregar_chave_privada(
        caminho_chave_privada_destinatario
    )

    chave_sessao_cifrada = decodificar_dados(
        chave_sessao_cifrada_codificada,
        codificacao
    )

    chave_aes_codificada_bytes = decifrar_chave_sessao(
        chave_sessao_cifrada,
        chave_privada_destinatario,
        hash_oaep
    )

    chave_aes_codificada = chave_aes_codificada_bytes.decode("utf-8")

    chave_aes = decodificar_dados(
        chave_aes_codificada,
        codificacao
    )

    iv = decodificar_dados(
        iv_codificado,
        codificacao
    )

    mensagem_cifrada = decodificar_dados(
        mensagem_cifrada_codificada,
        codificacao
    )

    mensagem_original_bytes = decifrar_mensagem(
        mensagem_cifrada,
        chave_aes,
        iv
    )

    mensagem_original = mensagem_original_bytes.decode("utf-8")

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write(mensagem_original)

    return mensagem_original