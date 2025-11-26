# OTUS. Использование Argo Workflows в MLOps пайплайнах

В данном репозитории представлены материалы и примеры использования Argo Workflows для создания и управления MLOps пайплайнами. Argo Workflows позволяет автоматизировать процессы машинного обучения, обеспечивая гибкость и масштабируемость.

## Описание проекта

Проект демонстрирует создание MLOps пайплайна с использованием Argo Workflows для обучения модели классификации на датасете Iris. Пайплайн включает следующие этапы:

1. **Загрузка данных** - загрузка датасета Iris из sklearn
2. **Разделение данных** - split на train/test выборки
3. **Обучение модели** - обучение RandomForestClassifier
4. **Валидация модели** - оценка качества модели на тестовых данных

## Структура проекта

```
.
├── Dockerfile                 # Docker образ для запуска пайплайна
├── Makefile                   # Команды для управления проектом
├── pyproject.toml             # Зависимости Python (uv)
├── requirements.txt           # Зависимости Python
├── README.md                  # Документация
├── config/
│   └── model-params.yaml      # Параметры модели
├── k8s/
│   └── pipeline.yaml          # Описание Argo Workflow
└── src/
    ├── load_data.py           # Загрузка данных
    ├── split_data.py          # Разделение данных
    ├── train.py               # Обучение модели
    └── validate.py            # Валидация модели
```

## Предварительные требования

- Docker
- Minikube
- kubectl
- Argo Workflows CLI

## Быстрый старт

### 1. Запуск Minikube

```bash
make minikube-start
```

### 2. Установка Argo Workflows

```bash
make argo-workflows-install
```

Эта команда создаст namespace `argo` и установит Argo Workflows версии `v3.7.4`.

### 3. Сборка и публикация Docker образа

```bash
make build
```

Эта команда соберет Docker образ с именем `nickosipov/otus-argo-workflows:latest` и отправит его в Docker Hub.

### 4. Запуск пайплайна

```bash
make deploy
```

### 5. Просмотр UI Argo Workflows

```bash
make ui
```

После выполнения команды откройте браузер по адресу: http://localhost:2746

## Описание пайплайна

Пайплайн описан в файле `k8s/pipeline.yaml` и использует DAG (Directed Acyclic Graph) для определения зависимостей между задачами:

```
load-data → split-data → train-model → validate-model
```

### Этапы пайплайна

1. **load-data** - загружает датасет Iris и сохраняет в `/mnt/data/iris_full.csv`
2. **split-data** - разделяет данные на train/test и сохраняет в `/mnt/data/`
3. **train-model** - обучает RandomForestClassifier с параметрами из `config/model-params.yaml`
4. **validate-model** - оценивает качество модели и выводит метрики

### Параметры модели

Параметры модели настраиваются в файле `config/model-params.yaml`:

```yaml
model_params:
  n_estimators: 150
  max_depth: 10
  min_samples_split: 2
  min_samples_leaf: 1
```

## Хранение данных

Для обмена данными между задачами используется PersistentVolumeClaim (PVC) с именем `workdir`:
- Режим доступа: ReadWriteMany
- Объем: 1Gi
- Точка монтирования: `/mnt/data`

## Полезные команды

### Управление Minikube

```bash
# Запуск кластера
make minikube-start

# Остановка кластера
make minikube-stop
```

### Управление Argo Workflows

```bash
# Установка Argo Workflows
make argo-workflows-install

# Удаление Argo Workflows
make argo-workflows-uninstall

# Запуск пайплайна
make deploy

# Открытие UI
make ui
```

### Работа с Docker образом

```bash
# Сборка и публикация образа
make build

# Запуск контейнера
make run
```

### Просмотр статуса пайплайна

```bash
# Список всех workflow
argo list -n argo

# Детальная информация о workflow
argo get <workflow-name> -n argo

# Логи конкретной задачи
argo logs <workflow-name> -n argo
```

## Удаление ресурсов

```bash
# Удаление Argo Workflows
make argo-workflows-uninstall

# Остановка Minikube
make minikube-stop
```

## Технологии

- **Argo Workflows** - оркестрация ML пайплайнов
- **Kubernetes** - платформа для контейнеризации
- **Minikube** - локальный Kubernetes кластер
- **Docker** - контейнеризация приложений
- **Python 3.11** - язык программирования
- **scikit-learn** - библиотека для машинного обучения
- **pandas** - обработка данных
- **uv** - менеджер зависимостей Python

## Автор

[Nick Osipov](https://t.me/NickOsipov)
