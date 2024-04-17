#!/bin/bash

# Определение пути к директории с Python скриптами
SCRIPT_DIR="MLOps/HW_1"

# Переход в директорию скриптов
cd $SCRIPT_DIR

# Выполнение скрипта предобработки данных
echo "Running data preprocessing..."
python model_preprocessing.py

# Проверка на наличие ошибки в предыдущей команде
if [ $? -ne 0 ]; then
  echo "Data preprocessing failed."
  exit 1
fi

# Выполнение скрипта обучения модели
echo "Training model..."
python model_preparation.py

# Проверка на наличие ошибки в предыдущей команде
if [ $? -ne 0 ]; then
  echo "Model training failed."
  exit 1
fi

# Выполнение скрипта тестирования модели
echo "Testing model..."
python model_testing.py

# Проверка на наличие ошибки в предыдущей команде
if [ $? -ne 0 ]; then
  echo "Model testing failed."
  exit 1
fi

echo "Pipeline execution completed successfully."
