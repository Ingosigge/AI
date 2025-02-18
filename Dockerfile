# Använd en lättvikts Python-bild
FROM python:3.9-slim

# Ställ in arbetskatalog
WORKDIR /app

# Kopiera alla filer
COPY . /app

# Installera beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Exponera porten
EXPOSE 5000

# Starta API-servern
CMD ["python", "api_server.py"]
