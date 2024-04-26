# Используем официальный образ Python как основу
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем содержимое текущей директории в контейнер в /usr/src/app
COPY HW_3/ui /app
COPY HW_3/requirements.txt /app

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Объявляем, что контейнер будет слушать порт 80
EXPOSE 8000

# Запускаем приложение при старте контейнера
CMD ["python", "/app/gradio_app.py", "runserver", "0.0.0.0:8000"]
