# Imagen base oficial de Python
FROM python:3.10-slim

# Definir directorio de trabajo
WORKDIR /app

# Copiar dependencias primero (para aprovechar cache)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la app
COPY . .

# Cloud Run usa el puerto 8080
ENV PORT=8080

# Comando de inicio con Gunicorn (app Flask en main.py)
CMD ["gunicorn", "--bind", ":8080", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]
