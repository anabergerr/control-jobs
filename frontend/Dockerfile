# Usar uma imagem base do Node.js
FROM node:16-alpine

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo package.json e instalar as dependências
COPY package.json .
RUN npm install

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta que o Next.js usará
EXPOSE 3000

# Comando para rodar a aplicação
CMD ["npm", "run", "dev"]