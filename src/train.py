"""
Module: train.py
Description: Обучение модели RandomForestClassifier на train данных
"""

import argparse

import joblib
import pandas as pd
import yaml
from loguru import logger
from sklearn.ensemble import RandomForestClassifier


def main():
    """
    Main function to train RandomForestClassifier model
    """
    # Начало обучения модели
    logger.info("Запуск процесса обучения модели...")

    # Аргументы командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, required=True)
    parser.add_argument("--params-file", type=str, required=True)
    args = parser.parse_args()

    # Получаем параметры
    data_dir = args.data_dir
    params_file = args.params_file
    logger.info(f"Директория с данными: {data_dir}")
    logger.info(f"Файл с параметрами: {params_file}")

    # Загружаем параметры модели из YAML файла
    logger.info("Загрузка параметров модели из YAML файла...")
    with open(params_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    model_params = config.get("model_params", {})
    logger.info(f"Параметры модели: {model_params}")

    # Загружаем train данные
    logger.info("Загрузка train данных...")
    X_train = pd.read_csv(f"{data_dir}/X_train.csv")
    y_train = pd.read_csv(f"{data_dir}/y_train.csv")
    logger.info(f"Загружено {len(X_train)} записей для обучения")
    logger.info(f"Количество признаков: {X_train.shape[1]}")

    # Создаем и обучаем модель
    logger.info("Создание модели RandomForestClassifier...")
    clf = RandomForestClassifier(**model_params)
    logger.info("Начало обучения модели...")
    clf.fit(X_train, y_train.values.ravel())
    logger.info("Обучение модели завершено")

    # Сохраняем модель
    model_path = f"{data_dir}/model.joblib"
    logger.info(f"Сохранение модели в {model_path}...")
    joblib.dump(clf, model_path)
    logger.info(f"Модель успешно сохранена в {model_path}")


if __name__ == "__main__":
    main()
