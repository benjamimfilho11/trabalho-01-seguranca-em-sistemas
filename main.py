from envelope.criar import criar_envelope
from envelope.abrir import abrir_envelope
from envelope.validacao import (
    validar_arquivo_existe,
    validar_codificacao,
    validar_hash
)


def criar():
    print("\n=== CRIAR ENVELOPE DIGITAL ===")

    caminho_mensagem = input(
        "Arquivo da mensagem em claro: "
    ).strip()

    caminho_chave_publica = input(
        "Chave pública do destinatário (.pem): "
    ).strip()

    caminho_chave_privada = input(
        "Chave privada do remetente (.pem): "
    ).strip()

    caminho_saida = input(
        "Nome do envelope de saída: "
    ).strip()

    codificacao = input(
        "Codificação (Base64 ou Hex): "
    ).strip()

    hash_oaep = input(
        "Hash do RSA-OAEP (SHA-256 ou SHA-512): "
    ).strip()

    hash_assinatura = input(
        "Hash da assinatura (SHA-256 ou SHA-512): "
    ).strip()

    validar_arquivo_existe(caminho_mensagem)
    validar_arquivo_existe(caminho_chave_publica)
    validar_arquivo_existe(caminho_chave_privada)

    validar_codificacao(codificacao)
    validar_hash(hash_oaep)
    validar_hash(hash_assinatura)

    criar_envelope(
        caminho_mensagem,
        caminho_chave_publica,
        caminho_chave_privada,
        caminho_saida,
        codificacao,
        hash_oaep,
        hash_assinatura
    )

    print("\nEnvelope criado com sucesso!")
    print(f"Arquivo salvo em: {caminho_saida}")


def abrir():
    print("\n=== ABRIR ENVELOPE DIGITAL ===")

    caminho_envelope = input(
        "Arquivo do envelope JSON: "
    ).strip()

    caminho_chave_privada = input(
        "Chave privada do destinatário (.pem): "
    ).strip()

    caminho_chave_publica = input(
        "Chave pública do remetente (.pem): "
    ).strip()

    caminho_saida = input(
        "Arquivo de saída da mensagem decifrada: "
    ).strip()

    validar_arquivo_existe(caminho_envelope)
    validar_arquivo_existe(caminho_chave_privada)
    validar_arquivo_existe(caminho_chave_publica)

    mensagem = abrir_envelope(
        caminho_envelope,
        caminho_chave_privada,
        caminho_chave_publica,
        caminho_saida
    )

    print("\nEnvelope aberto com sucesso!")
    print(f"Mensagem salva em: {caminho_saida}")
    print("\nMensagem recuperada:")
    print(mensagem)


def main():
    while True:
        print("\n" + "=" * 50)
        print("ENVELOPE DIGITAL ASSINADO")
        print("=" * 50)

        print("1 - Criar envelope")
        print("2 - Abrir envelope")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        try:
            if opcao == "1":
                criar()

            elif opcao == "2":
                abrir()

            elif opcao == "0":
                print("\nPrograma encerrado.")
                break

            else:
                print("\nOpção inválida.")

        except FileNotFoundError as erro:
            print(f"\nErro de arquivo: {erro}")

        except ValueError as erro:
            print(f"\nErro: {erro}")

        except Exception as erro:
            print(f"\nOcorreu um erro inesperado: {erro}")


if __name__ == "__main__":
    main()