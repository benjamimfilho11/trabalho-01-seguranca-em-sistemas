# trabalho-01-seguranca-em-sistemas
ENVELOPE DIGITAL ASSINADO
Trabalho 01 – Segurança em Sistemas Computacionais

1. DESCRIÇÃO DO PROJETO

Este projeto implementa um mecanismo de Envelope Digital Assinado utilizando criptografia híbrida.

O sistema permite:

- Cifrar uma mensagem de texto com AES-256-CBC;
- Gerar uma chave de sessão AES de 256 bits;
- Gerar um vetor de inicialização (IV) de 128 bits;
- Aplicar padding PKCS7;
- Proteger a chave de sessão com RSA-OAEP;
- Assinar a mensagem cifrada com RSA usando PKCS#1 v1.5;
- Utilizar SHA-256 ou SHA-512;
- Utilizar Base64 ou Hex como codificação textual;
- Gerar um envelope único em formato JSON;
- Verificar a assinatura antes da decifragem;
- Recuperar a chave AES com a chave privada do destinatário;
- Decifrar a mensagem original.

A implementação foi desenvolvida em Python utilizando a biblioteca cryptography.

2. ESTRUTURA DO PROJETO

trabalho-01-seguranca-em-sistemas/
│
├── main.py
├── gerar_chaves.py
├── mensagem.txt
├── requirements.txt
├── README.txt
│
├── crypto/
│   ├── __init__.py
│   ├── aes.py
│   ├── rsa.py
│   ├── assinatura.py
│   └── encoding.py
│
├── envelope/
│   ├── __init__.py
│   ├── criar.py
│   ├── abrir.py
│   └── validacao.py
│
├── chaves/
│   ├── remetente_privada.pem
│   ├── remetente_publica.pem
│   ├── destinatario_privada.pem
│   └── destinatario_publica.pem
│
└── testes/
    ├── test_aes.py
    ├── test_assinatura.py
    ├── test_encoding.py
    ├── test_integracao.py
    └── test_rsa.py

3. REQUISITOS

- Python 3.12 ou compatível;
- Biblioteca cryptography;
- Biblioteca pytest.

As dependências podem ser instaladas através do arquivo requirements.txt.

4. CRIAÇÃO DO AMBIENTE VIRTUAL

Na raiz do projeto, execute:

python -m venv .venv

No Windows PowerShell:

.venv\Scripts\Activate.ps1

No Prompt de Comando:

.venv\Scripts\activate

5. INSTALAÇÃO DAS DEPENDÊNCIAS

Com o ambiente virtual ativado, execute:

python -m pip install -r requirements.txt

6. GERAÇÃO DAS CHAVES RSA

Caso seja necessário gerar novos pares de chaves, execute:

python gerar_chaves.py

Serão gerados dois pares de chaves:

- Remetente:
  - remetente_privada.pem
  - remetente_publica.pem

- Destinatário:
  - destinatario_privada.pem
  - destinatario_publica.pem

As chaves serão armazenadas na pasta chaves/.

7. EXECUÇÃO DO PROGRAMA

Para iniciar o programa:

python main.py

O menu principal apresenta as opções:

1 - Criar envelope
2 - Abrir envelope
0 - Sair

8. CRIAÇÃO DO ENVELOPE

Ao selecionar a opção 1, o programa solicitará:

- Arquivo da mensagem em claro;
- Chave pública do destinatário;
- Chave privada do remetente;
- Nome do arquivo de saída;
- Codificação: Base64 ou Hex;
- Hash do RSA-OAEP: SHA-256 ou SHA-512;
- Hash da assinatura: SHA-256 ou SHA-512.

Exemplo:

Arquivo da mensagem:
mensagem.txt

Chave pública do destinatário:
chaves/destinatario_publica.pem

Chave privada do remetente:
chaves/remetente_privada.pem

Arquivo de saída:
envelope.json

Codificação:
Base64

Hash RSA-OAEP:
SHA-256

Hash da assinatura:
SHA-256

O arquivo envelope.json será gerado contendo os parâmetros criptográficos e os seguintes dados:

- IV;
- chave de sessão cifrada;
- mensagem cifrada;
- assinatura digital.

9. ABERTURA DO ENVELOPE

Ao selecionar a opção 2, o programa solicitará:

- Arquivo envelope JSON;
- Chave privada do destinatário;
- Chave pública do remetente;
- Nome do arquivo de saída.

Exemplo:

Arquivo:
envelope.json

Chave privada do destinatário:
chaves/destinatario_privada.pem

Chave pública do remetente:
chaves/remetente_publica.pem

Arquivo de saída:
mensagem_decifrada.txt

Antes da decifragem, o programa verifica a assinatura digital.

Caso a assinatura seja inválida, o processo é interrompido.

Caso seja válida:

1. A chave AES é recuperada através do RSA-OAEP;
2. O IV é recuperado;
3. A mensagem cifrada é decodificada;
4. A mensagem é decifrada com AES-256-CBC;
5. O padding PKCS7 é removido;
6. O texto original é salvo no arquivo de saída.

10. FUNCIONAMENTO CRIPTOGRÁFICO

O fluxo de criação do envelope é:

Mensagem
→ AES-256-CBC
→ Mensagem cifrada
→ Base64 ou Hex
→ Assinatura RSA

Em paralelo:

Chave AES
→ Base64 ou Hex
→ RSA-OAEP
→ Chave de sessão protegida

Os dados são então reunidos em um arquivo JSON.

Na abertura:

Envelope JSON
→ Verificação da assinatura
→ Recuperação da chave AES
→ Decifragem AES
→ Mensagem original

11. TESTES AUTOMATIZADOS

Os testes estão localizados na pasta testes/.

Para executá-los:

python -m pytest -v

Os testes verificam:

- Codificação e decodificação Base64;
- Codificação e decodificação Hex;
- Cifragem e decifragem AES;
- Cifragem e decifragem RSA-OAEP;
- Assinatura RSA válida;
- Detecção de assinatura inválida;
- Fluxo completo de criação e abertura do envelope.

12. TESTES MANUAIS REALIZADOS

Também foram realizados testes manuais para verificar:

- Criação e abertura correta do envelope;
- Recuperação correta da mensagem original;
- Detecção de alteração na mensagem cifrada;
- Falha ao utilizar chave pública incorreta para verificar a assinatura;
- Falha ao utilizar chave privada incorreta para recuperar a chave de sessão.

13. INTEROPERABILIDADE COM CYBERCHEF

A implementação foi testada com o CyberChef para validar a interoperabilidade do protocolo.

Foram verificadas as seguintes etapas:

- Verificação da assinatura RSA;
- Recuperação da chave de sessão com RSA-OAEP;
- Decifragem da mensagem com AES-256-CBC;
- Uso de Base64;
- Uso de SHA-256;
- Compatibilidade da assinatura RSASSA-PKCS1-v1_5.

O objetivo é permitir que os dados gerados pelo programa possam ser processados por outra implementação compatível com o mesmo protocolo.

14. OBSERVAÇÕES

O programa utiliza:

- AES-256-CBC;
- PKCS7;
- RSA-OAEP;
- MGF1 com o mesmo hash do OAEP;
- SHA-256 ou SHA-512;
- RSASSA-PKCS1-v1_5;
- Base64 ou Hex;
- Chaves RSA em formato PEM.

O sistema também possui tratamento de erros para impedir encerramentos inesperados em situações como:

- Arquivo inexistente;
- Hash inválido;
- Codificação inválida;
- Assinatura inválida;
- Chave incorreta;
- Estrutura JSON incompatível.