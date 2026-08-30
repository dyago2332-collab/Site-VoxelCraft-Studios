FROM python:3.10-slim

ENV PYTHONUNBUFFERED=True
ENV APP_HOME=/app
WORKDIR $APP_HOME

# Copia todos os arquivos e as novas pastas (templates/static) para dentro do container
COPY . ./

# Instala as dependências listadas no seu arquivo
RUN pip install --no-cache-dir -r requirements.txt

# Comando correto para rodar o Gunicorn apontando para o main.py
CMD gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 main:app
