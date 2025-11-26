"""
Module: train.py
Description: Обучение модели RandomForestClassifier на train данных
"""

import argparse

import joblib
import pandas as pd
from loguru import logger
from sklearn.ensemble import RandomForestClassifier


def parse_params(params_str):
    """
    Parse parameters string in format: key1=value1,key2=value2
    Returns dict with converted types (int for numeric values)
    """
    params = {}
    if params_str:
        for param in params_str.split(","):
            key, value = param.split("=")
            # Пробуем преобразовать в int, если не получается - оставляем строкой
            try:
                params[key.strip()] = int(value.strip())
            except ValueError:
                try:
                    params[key.strip()] = float(value.strip())
                except ValueError:
                    params[key.strip()] = value.strip()
    return params


def main():
    """
    Main function to train RandomForestClassifier model
    """
    # Начало обучения модели
    logger.info("Запуск процесса обучения модели...")

    # Аргументы командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, required=True)
    parser.add_argument("--params", type=str, default="n_estimators=100")
    args = parser.parse_args()

    # Получаем параметры
    data_dir = args.data_dir
    model_params = parse_params(args.params)
    logger.info(f"Директория с данными: {data_dir}")
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
