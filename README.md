
# Небольшое тестовое задание в Леста Старт

#### `GET /ping`


##### Example output

```json
{"status":"ok"}
```

#### `GET /count`


##### Example output

```json
{"count":52}
```


## Структура проекта

```bash

.
├── app
│   ├── __init__.py
│   └── routes
│       ├── count.py
│       ├── __init__.py
│       └── ping.py
├── app.py
├── docker-compose.yaml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt


```

## Запуск

Для запуска выполнить

```bash
docker compose up --build