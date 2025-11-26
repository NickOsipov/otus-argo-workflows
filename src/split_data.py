"""
Module: split_data.py
Description: Разделение данных на train и test выборки
"""

import argparse

import pandas as pd
from loguru import logger
from sklearn.model_selection import train_test_split


def main():
    """
    Main function to split iris dataset into train and test sets
    """
    # Начало разделения данных
    logger.info("Разделение данных на train и test выборки...")

    # Аргументы командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=str, required=True)
    args = parser.parse_args()

    # Получаем путь к директории с данными
    data_dir = args.data_dir
    logger.info(f"Директория с данными: {data_dir}")

    # Загружаем данные
    data_path = f"{data_dir}/iris_full.csv"
    logger.info(f"Загрузка данных из {data_path}...")
    df = pd.read_csv(data_path)

    # Разделяем на признаки и целевую переменную
    X = df.drop("target", axis=1)
    y = df["target"]
    logger.info(f"Размер датасета: {len(df)} записей")

    # Разделяем на train и test
    logger.info("Выполняем train_test_split с test_size=0.2...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    logger.info(f"Train size: {len(X_train)}, Test size: {len(X_test)}")

    # Сохраняем данные
    logger.info("Сохранение разделенных данных...")
    X_train.to_csv(f"{data_dir}/X_train.csv", index=False)
    X_test.to_csv(f"{data_dir}/X_test.csv", index=False)
    y_train.to_csv(f"{data_dir}/y_train.csv", index=False)
    y_test.to_csv(f"{data_dir}/y_test.csv", index=False)
    logger.info(f"Данные сохранены в {data_dir}")


if __name__ == "__main__":
    main()
