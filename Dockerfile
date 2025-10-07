# Imagem base (vem com Python já instalado)
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Uvicorn
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
