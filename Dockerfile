# Gunakan image Python resmi
FROM python:3.10-slim

# Buat direktori kerja di dalam container
WORKDIR /app

# Salin semua file ke dalam container
COPY . /app

# Install dependensi Flask
RUN pip install --no-cache-dir flask

# Buka port untuk Flask
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
