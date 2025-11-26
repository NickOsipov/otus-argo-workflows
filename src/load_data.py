"""
Module: load_data.py
Description: Загрузка данных из sklearn.datasets.load_iris
и сохранение в CSV файл
"""

import argparse
import os

import pandas as pd
from loguru import logger
from sklearn.datasets import load_iris


def main():
    """
    Main function to load iris dataset and save it to a CSV file
    """
    # Начало загрузки данных
    logger.info("Загрузка данных...")

    # Аргументы командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    # Получаем путь к выходному файлу из аргументов
    data_dir = args.output
    os.makedirs(data_dir, exist_ok=True)
    logger.info(f"Создаем директорию {data_dir}")

    # Получаем путь к выходному файлу
    data_file = "iris_full.csv"
    data_path = os.path.join(data_dir, data_file)
    logger.info(f"Путь к выходному файлу: {data_path}")

    # Загружаем датасет iris
    logger.info(f"Загрузка данных в {data_path}...")
    iris = load_iris()

    # Создаем DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df["target"] = iris.target

    # Сохраняем DataFrame в CSV файл
    df.to_csv(data_path, index=False)
    logger.info(f"Данные сохранены в {data_path}")


if __name__ == "__main__":
    main()
