## Структура проекта

```
app/
├── config.py          # настройки (URL базы, секрет, Redis)
├── database.py        # подключение к БД и Redis
├── models.py          # SQLAlchemy модели (User, Task)
├── schemas.py         # Pydantic схемы для запросов и ответов
├── security.py        # хеширование паролей, JWT
├── dependencies.py    # зависимости FastAPI (get_db, get_current_user)
├── repositories/
│   ├── user_repo.py   # запросы к таблице users
│   └── task_repo.py   # запросы к таблице tasks
├── services/
│   ├── auth_service.py  # логика регистрации и входа
│   └── task_service.py  # логика задач + Redis кэш
├── routers/
│   ├── auth.py        # маршруты /auth/*
│   ├── tasks.py       # маршруты /tasks/*
│   └── admin.py       # маршруты /admin/*
└── main.py            # точка входа, создание таблиц, подключение роутеров
Dockerfile
docker-compose.yml
requirements.txt
```

## Запуск через Docker

```bash
docker-compose up --build
```

После запуска Swagger доступен по адресу: http://localhost:8000/docs

Если Redis не нужен, можно запустить только backend:

```bash
docker build -t task-tracker .
docker run -p 8000:8000 task-tracker
```

## Маршруты

| Метод  | Путь                | Описание                        | Авторизация |
|--------|---------------------|---------------------------------|-------------|
| POST   | /auth/register      | Регистрация пользователя        | Нет         |
| POST   | /auth/login         | Вход, получение JWT токена      | Нет         |
| GET    | /auth/me            | Данные текущего пользователя    | Да          |
| POST   | /tasks/             | Создать задачу                  | Да          |
| GET    | /tasks/             | Список своих задач              | Да          |
| GET    | /tasks/{task_id}    | Получить задачу по ID           | Да          |
| PATCH  | /tasks/{task_id}    | Обновить задачу                 | Да          |
| DELETE | /tasks/{task_id}    | Удалить задачу                  | Да          |
| GET    | /admin/users        | Список всех пользователей       | Только admin|

При старте автоматически создаётся администратор:
- username: `admin`
- password: `Admin123`

