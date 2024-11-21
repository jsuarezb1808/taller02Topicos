
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias necesarias
RUN pip install flask flask-restful

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000


CMD ["python", "app.py"]