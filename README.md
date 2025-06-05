# 🔐 SSH Brute Force Script - Educational Project

> ⚠️ Este projeto tem **fins educacionais**.

## 📚 Sobre

Este projeto é um estudo prático de **força bruta via SSH**, utilizando Python e as bibliotecas `pwntools`, `paramiko` e `time`. Ele tenta se autenticar em um servidor SSH testando várias senhas de uma wordlist.

## 💡 Objetivos de Aprendizado

- Automatizar tentativas de login via SSH
- Tratar erros de autenticação
- Medir o tempo total da operação
- Armazenar resultados de forma segura e organizada
- Usar bibliotecas populares no ecossistema de Cyber Segurança

## 🧠 Tecnologias/Bibliotecas

- [`pwntools`](https://docs.pwntools.com/en/stable/): Automação de tarefas em CTFs e exploração
- [`paramiko`](https://www.paramiko.org/): Biblioteca para conexão SSH em Python
- `time`: Biblioteca padrão do Python para temporização

## 📁 Estrutura do projeto

ssh-brute-force/
├── best110.txt # Wordlist com senhas
├── found.txt # Arquivo gerado com os resultados da execução (GERADO APÓS EXECUÇÃO)
├── script.py # Código principal
└── README.md # Documentação do projeto


## ▶️ Como usar

```bash
git clone https://github.com/seuusuario/ssh-brute-force
cd ssh-brute-force
python3 script.py
```
Certifique-se de editar o IP e o usuário no script (host, username) antes de executar.

## 📚 Wordlist utilizada

A wordlist `best110.txt` foi utilizada como base para este script. Ela está disponível publicamente e foi criada por:

- **Autor/repositório**: danielmiessler
- **Link**: [[URL para o repositório original]](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/best110.txt)

Créditos totais aos criadores da wordlist. Este projeto utiliza o arquivo apenas para fins de estudo e demonstração.




