# 🌟 Controle de Vagas de Emprego 🌟

Bem-vindo ao nosso projeto de **Controle de Vagas de Emprego**! 🚀

## 📋 Descrição

Este projeto é uma aplicação web para gerenciar vagas de emprego e candidaturas. Ele utiliza **Next.js** no front-end e **FastAPI** na API do back-end. É uma solução completa para quem deseja organizar e acompanhar processos seletivos de forma eficiente. 💼

## 🛠️ Tecnologias Utilizadas

- **Front-end**: Next.js ⚛️
- **Back-end**: FastAPI 🚀

## 🔧 Passo a Passo: Como Rodar o Backend

1. **Criação do Ambiente Virtual** 🧑‍💻  
   Primeiramente, crie um ambiente virtual para o projeto:
   ```bash
   uv venv  # Cria o ambiente virtual
   ```

2. **Ativando o Ambiente Virtual** 🔑  
   Ative o ambiente virtual:
     ```bash
     source .venv/bin/activate  # Ativa o ambiente virtual
     ```

3. **Instalando o `uv` e as Dependências** 📦  
   Para instalar o `uv` e as dependências do projeto, rode os comandos:
   ```bash
   uv pip install uv  # Instala o uv
   uv sync  # Instala todas as dependências listadas no pyproject.toml
   ```

4. **Rodando o Servidor do Backend** 🚀  
   Agora, você pode rodar o servidor FastAPI com o comando:
   ```bash
   uvicorn app.main:app --reload  # Inicia o servidor FastAPI
   ```

   O servidor estará rodando em [http://127.0.0.1:8000](http://127.0.0.1:8000). 🎉

## 🤝 Contribuição

Este projeto é open source e qualquer contribuição é bem-vinda! 🎉 Sinta-se à vontade para abrir issues e pull requests. Vamos construir algo incrível juntos! 💪

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
