# Usar a imagem base oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Definir a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expor a porta que o gunicorn usará
EXPOSE 5002

# Comando para iniciar a aplicação com gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]