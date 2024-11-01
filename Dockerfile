FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#ENV HOSTNAME=$(hostname)
#ENV MLP_ACCOUNT_ID=1000147788
#ENV MLP_GRPC_HOST=gate.caila.io:443
#ENV MLP_GRPC_HOSTS=0.gate.caila.io:443,1.gate.caila.io:443,2.gate.caila.io:443,3.gate.caila.io:443,4.gate.caila.io:443,5.gate.caila.io:443,6.gate.caila.io:443,7.gate.caila.io:443,8.gate.caila.io:443,9.gate.caila.io:443
#ENV MLP_GRPC_SECURE=true
#ENV MLP_INSTANCE_ID=35369
#ENV MLP_MODEL_ID=94602
#ENV MLP_MODEL_NAME=detect-language
#ENV MLP_REST_URL=https://caila.io
#ENV MLP_S3_ACCESS_KEY=s3-user-1000147788
#ENV MLP_S3_BUCKET=s3-bucket-1000147788-4pkgynndrs
#ENV MLP_S3_ENDPOINT=https://storage.caila.io
#ENV MLP_S3_SECRET_KEY=2lpqqi3gluwe5ahzza6f
#ENV MLP_SERVICE_TOKEN=1000147788.94602.Ifd0VEG5khQevl3ZMEyU14oEtkvOhabw1GIpXeiv
#ENV MLP_STORAGE_DIR=
#ENV MLP_STORAGE_TYPE=s3
#ENV SERVICE_CONFIG={}


# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
COPY src /app/src

# Запускаем приложение
CMD ["python", "/app/src/main.py"]