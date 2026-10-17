# Envelope Digital Assinado

**Trabalho 01 – Segurança em Sistemas Computacionais**

Universidade Federal do Piauí (UFPI)

## 1. Descrição do projeto

Este projeto implementa um mecanismo de Envelope Digital Assinado utilizando criptografia híbrida e o modelo Encrypt-then-Sign (cifrar e depois assinar).

O sistema permite:

- Cifrar mensagens de texto utilizando AES-256-CBC;
- Gerar uma chave de sessão AES aleatória de 256 bits;
- Gerar um vetor de inicialização (IV) aleatório de 128 bits;
- Aplicar e remover padding PKCS7;
- Proteger a chave de sessão utilizando RSA-OAEP;
- Assinar o criptograma codificado com RSA PKCS#1 v1.5;
- Utilizar SHA-256 ou SHA-512;
- Utilizar Base64 ou Hex como codificação textual;
- Gerar um envelope único em formato JSON;
- Validar a estrutura e os parâmetros do envelope;
- Verificar a assinatura digital antes da decifragem;
- Recuperar a chave AES utilizando a chave privada do destinatário;
- Decifrar e recuperar a mensagem original;
- Identificar erros de arquivos, parâmetros e integridade.

A implementação foi desenvolvida em Python, utilizando a biblioteca `cryptography`.

## 2. Estrutura do projeto

```text
trabalho-01-seguranca-em-sistemas/
│
├── main.py
├── gerar_chaves.py
├── mensagem.txt
├── requirements.txt
├── README.md
├── .gitignore
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
    ├── test_enconding.py
    ├── test_integracao.py
    └── test_rsa.py
```

Os arquivos `envelope.json` e `mensagem_decifrada.txt` podem ser gerados durante a execução.

As chaves PEM incluídas são destinadas exclusivamente à demonstração e aos testes.

## 3. Requisitos

- Python 3.12 ou versão compatível;
- Biblioteca `cryptography`;
- Biblioteca `pytest` para execução dos testes.

As dependências são instaladas por meio do arquivo `requirements.txt`.

## 4. Criação do ambiente virtual

Na raiz do projeto, execute:

```powershell
python -m venv .venv
```

No Windows PowerShell, ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando (CMD):

```cmd
.venv\Scripts\activate.bat
```

## 5. Instalação das dependências

Com o ambiente virtual ativado, execute:

```powershell
python -m pip install -r requirements.txt
```

## 6. Geração das chaves RSA

Para gerar novos pares de chaves, execute:

```powershell
python gerar_chaves.py
```

Serão gerados dois pares de chaves RSA:

**Remetente:**
- `remetente_privada.pem`
- `remetente_publica.pem`

**Destinatário:**
- `destinatario_privada.pem`
- `destinatario_publica.pem`

As chaves serão armazenadas na pasta `chaves/`.

A chave privada do remetente é utilizada para assinar o criptograma, enquanto a chave pública correspondente é utilizada para verificar a assinatura.

A chave pública do destinatário protege a chave de sessão AES, que poderá ser recuperada apenas com a chave privada correspondente.

## 7. Execução do programa

Para iniciar a aplicação:

```powershell
python main.py
```

O menu principal apresenta:

```text
1 - Criar envelope
2 - Abrir envelope
0 - Sair
```

O usuário pode informar os caminhos dos arquivos de entrada e saída.

## 8. Criação do envelope

Ao selecionar a opção 1, o programa solicitará:

- Arquivo da mensagem em claro;
- Chave pública do destinatário;
- Chave privada do remetente;
- Nome do arquivo JSON de saída;
- Codificação: Base64 ou Hex;
- Hash do RSA-OAEP: SHA-256 ou SHA-512;
- Hash da assinatura: SHA-256 ou SHA-512.

**Exemplo de preenchimento:**

```text
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
```

O arquivo `envelope.json` conterá os parâmetros criptográficos e os seguintes dados:

- IV;
- Chave de sessão cifrada;
- Mensagem cifrada;
- Assinatura digital.

A estrutura segue o padrão estabelecido no enunciado, com os objetos `parametros` e `envelope`.

## 9. Abertura do envelope

Ao selecionar a opção 2, o programa solicitará:

- Arquivo JSON do envelope;
- Chave privada do destinatário;
- Chave pública do remetente;
- Nome do arquivo de saída.

**Exemplo:**

```text
Arquivo do envelope:
envelope.json

Chave privada do destinatário:
chaves/destinatario_privada.pem

Chave pública do remetente:
chaves/remetente_publica.pem

Arquivo de saída:
mensagem_decifrada.txt
```

Durante a abertura:

1. O JSON é carregado e sua estrutura é validada;
2. Os parâmetros criptográficos são verificados;
3. A assinatura digital do criptograma codificado é verificada;
4. Caso a assinatura seja inválida, o processo é interrompido;
5. A chave de sessão AES é recuperada utilizando RSA-OAEP;
6. O IV e a mensagem cifrada são decodificados;
7. A mensagem é decifrada utilizando AES-256-CBC;
8. O padding PKCS7 é removido;
9. O texto original é salvo no arquivo informado.

A verificação da assinatura ocorre antes da decifragem, conforme o modelo Encrypt-then-Sign.

## 10. Funcionamento criptográfico

**Criação do envelope:**

```text
Mensagem original
      ↓
AES-256-CBC + PKCS7
      ↓
Mensagem cifrada
      ↓
Codificação Base64 ou Hex
      ↓
Assinatura RSA PKCS#1 v1.5
```

Em paralelo:

```text
Chave AES aleatória
      ↓
Codificação Base64 ou Hex
      ↓
RSA-OAEP
      ↓
Chave de sessão protegida
```

Os dados e seus parâmetros são reunidos em um único envelope JSON.

**Abertura do envelope:**

```text
Envelope JSON
      ↓
Validação da estrutura
      ↓
Verificação da assinatura
      ↓
Recuperação da chave AES
      ↓
Decifragem AES-256-CBC
      ↓
Remoção do padding
      ↓
Mensagem original
```

## 11. Testes automatizados

Os testes automatizados estão localizados na pasta `testes/`.

Para executá-los, utilize o comando abaixo na raiz do projeto:

```powershell
python -m pytest -v
```

A suíte contempla testes de:

- Codificação e decodificação Base64 e Hex;
- Cifragem e decifragem AES;
- Operações RSA-OAEP;
- Geração e verificação de assinaturas RSA;
- Identificação de assinaturas inválidas;
- Integração entre criação e abertura do envelope.

A execução mais recente dos testes automatizados foi concluída sem falhas.

## 12. Validação e tratamento de erros

A aplicação realiza verificações para identificar inconsistências durante a utilização.

São tratados ou identificados casos como:

- Arquivos de entrada inexistentes;
- Arquivos JSON malformados;
- Ausência de campos obrigatórios;
- Estruturas JSON com tipos incompatíveis;
- Algoritmos criptográficos inválidos;
- Hashes diferentes dos permitidos;
- Codificações diferentes de Base64 e Hex;
- Assinaturas digitais inválidas;
- Problemas de permissões de arquivos;
- Problemas de codificação textual;
- Falhas em operações criptográficas.

O arquivo `envelope/validacao.py` concentra as validações dos parâmetros e da estrutura do envelope.

O arquivo `main.py` realiza o tratamento das exceções, apresentando mensagens de erro e permitindo que o usuário continue utilizando o menu principal.

## 13. Testes manuais

Os testes manuais incluem operações de criação e abertura de envelopes utilizando os pares de chaves RSA.

Também foram realizados testes envolvendo:

- Recuperação da mensagem original;
- Alteração intencional da mensagem cifrada;
- Identificação de assinatura inválida;
- Utilização de chaves incompatíveis;
- Validação de parâmetros incorretos.

Os testes auxiliam na verificação do funcionamento do protocolo e de seus mecanismos de proteção.

## 14. Interoperabilidade com CyberChef

A implementação segue os parâmetros criptográficos estabelecidos no enunciado para possibilitar interoperabilidade com ferramentas externas, incluindo o CyberChef.

Os principais padrões utilizados são:

- AES-256-CBC;
- PKCS7;
- RSA-OAEP;
- MGF1 com o mesmo hash do OAEP;
- SHA-256 ou SHA-512;
- RSASSA-PKCS1-v1_5;
- Base64 ou Hex;
- Chaves RSA em formato PEM.

Para verificar a interoperabilidade, devem ser utilizadas configurações equivalentes em ambas as ferramentas.

A verificação completa exige confirmar a compatibilidade das operações de assinatura, recuperação da chave de sessão e decifragem da mensagem entre as implementações.

## 15. Observações finais

O projeto utiliza o modelo Encrypt-then-Sign para garantir a confidencialidade da mensagem e permitir a verificação de sua integridade e autenticidade por meio de assinatura digital.

As chaves privadas devem permanecer protegidas e não devem ser compartilhadas em aplicações reais.

O sistema foi desenvolvido com uma arquitetura modular, separando os algoritmos criptográficos, as operações de envelope, a validação dos parâmetros e os testes automatizados.

Essa organização facilita a manutenção, a verificação e a evolução da implementação.
