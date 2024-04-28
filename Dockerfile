# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Copia todo o código fonte para o diretório de trabalho
COPY /app .

# Define o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "main.py"]
