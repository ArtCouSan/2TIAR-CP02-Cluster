# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala as dependências do Python
RUN pip install --no-cache-dir

# Copia todo o código fonte para o diretório de trabalho
COPY . .

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "main.py"]