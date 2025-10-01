# Aegur
# 🛡️ Aegur — Gerador de Senhas Offline em Python (Seu Escudo Digital)

**Aegur** é um gerador de senhas offline, open source e altamente seguro, escrito em Python, com interface CLI minimalista e estrutura clara, projetado como um escudo digital contra ataques de força bruta, phishing visual e sistemas inseguros.

## 🎯 Objetivo do Projeto

Criar um gerador de senhas offline que seja:

- **Máxima entropia e aleatoriedade criptográfica**
- **Proteção contra spoofing visual** (exclusão rigorosa de caracteres ambíguos)
- **Totalmente offline** — nenhuma conexão de rede em momento algum
- **Sem uso de dicionários, palavras ou padrões** — apenas caracteres aleatórios
- **Código auditável, organizado e legível**
- **Instalação e uso exclusivamente via git clone**

## ✅ Características de Segurança

### 🔍 Filtro Anti-Spoofing Visual
Exclusão rigorosa de caracteres visualmente ambíguos, incluindo:
- Dígitos/letras confusos: 0/O/o, 1/l/I/i
- Caracteres latinos acentuados vs. não acentuados
- Letras cirílicas, gregas ou arcaicas que imitam latinas (ex: а cirílico vs a latino)

### 🛡️ Modos de Geração

#### 🟢 `--ascii-only`
Apenas caracteres ASCII imprimíveis seguros (sem ambiguidades).
- Pool: `"23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?"`

#### 🔵 `--strong-mode` (padrão)
Combinação de ASCII seguro + símbolos Unicode visualmente distintos e seguros.
- Exemplos: ΔΘΛΞΠΣΦΨΩ≠≤≥±∫∏√€₹₽₺←→↑↓↔↵¶§

#### 🟡 `--bank-mode`
Modo ultra-conservador: apenas alfanumérico ASCII seguro, sem símbolos, sem Unicode.
- Pool: `"23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz"`

#### 🟥 `--paranoid-mode`
O modo mais seguro:
- Sobrescrita segura de strings sensíveis após uso
- Geração de hash SHA3 da senha para auditoria offline
- Nenhuma exibição automática da senha (exige flag explícita)

## 📦 Requisitos

- Python 3.8+
- Nenhuma dependência externa (apenas biblioteca padrão)

## 🚀 Instalação e Uso

### Instalação
```bash
git clone https://github.com/seuusuario/aegur.git
cd aegur

Uso Básico 

# Modo padrão (strong-mode)
python aegur.py

# Modo bancário
python aegur.py --bank-mode --length 12

# Modo ASCII apenas
python aegur.py --ascii-only --length 20 --verbose

# Modo paranoico
python aegur.py --paranoid-mode --length 16 --show-password --verbose

Opções Disponíveis
--ascii-only: Apenas caracteres ASCII seguros
--bank-mode: Modo ultra-conservador (alfanumérico)
--strong-mode: Modo forte (padrão)
--paranoid-mode: Modo mais seguro
--length N: Comprimento da senha (padrão: 16)
--verbose: Mostrar estatísticas de entropia
--show-password: Mostrar senha no modo paranoico
📊 Estatísticas de Entropia
Com a flag --verbose, Aegur mostra:

Comprimento da senha
Tamanho do pool de caracteres
Entropia estimada em bits
Tempo estimado de resistência a força bruta
📋 Cópia para Clipboard
Aegur não implementa cópia para clipboard internamente para manter o princípio de isolamento offline. Usuários que confiam em seu ambiente podem redirecionar a saída manualmente:

python aegur.py --bank-mode --length 12 | tr -d '\n' | xclip -selection clipboard

Princípios de Segurança

Aleatoriedade Criptográfica: Uso exclusivo de secrets.SystemRandom()
Nenhum Padrão: Senhas compostas exclusivamente por caracteres aleatórios
Entropia Máxima: Cada caractere contribui para a segurança total
Pool Balanceado: Caracteres distribuídos para evitar viés
Isolamento Offline: Nenhuma conexão de rede em momento algum

Aegur não é só uma ferramenta — é um princípio.
Enquanto existirem senhas fracas, spoofing visual e sistemas legados, Aegur será o escudo que você carrega no terminal.

Feito para ser compreendido.
Feito para proteger sem confiança cega.