"""
Module: validate.py
Description: Валидация обученной модели на test данных
"""

import argparse

import joblib
import pandas as pd
from loguru import logger
from sklearn.metrics import accuracy_score


def main():
    """
    Main function to validate trained model on test data
    """
    # Начало валидации модели
    logger.info("Запуск процесса валидации модели...")

    # Аргументы командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, required=True)
    args = parser.parse_args()

    # Получаем параметры
    data_dir = args.data_dir
    logger.info(f"Директория с данными: {data_dir}")

    # Загружаем модель
    model_path = f"{data_dir}/model.joblib"
    logger.info(f"Загрузка модели из {model_path}...")
    clf = joblib.load(model_path)
    logger.info("Модель успешно загружена")

    # Загружаем test данные
    logger.info("Загрузка test данных...")
    X_test = pd.read_csv(f"{data_dir}/X_test.csv")
    y_test = pd.read_csv(f"{data_dir}/y_test.csv")
    logger.info(f"Загружено {len(X_test)} записей для валидации")
    logger.info(f"Количество признаков: {X_test.shape[1]}")

    # Предсказание
    logger.info("Выполнение предсказаний на test данных...")
    y_pred = clf.predict(X_test)

    # Вычисляем метрики
    logger.info("Вычисление метрик...")
    acc = accuracy_score(y_test, y_pred)
    logger.info(f"Accuracy: {acc:.4f}")
    logger.info("Валидация модели завершена")


if __name__ == "__main__":
    main()
