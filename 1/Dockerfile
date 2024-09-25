# Використовуємо базовий образ Python
FROM python:3.9-slim

# Встановлюємо робочу директорію
WORKDIR /1

# Копіюємо залежності
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код додатку
COPY . .

# Виставляємо порт
EXPOSE 8080

# Команда для запуску додатку
CMD ["python", "app.py"]
