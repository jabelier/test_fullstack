# Publications Feed

Fullstack-сервис ленты публикаций с JWT-авторизацией и Redis-кэшированием.

## Стек

- **Backend**: Python 3.12, FastAPI, asyncpg, redis-py
- **БД**: PostgreSQL 16
- **Кэш**: Redis 7
- **Контейнеризация**: Docker + Docker Compose
- **Frontend**: Vue 3, TypeScript, Vite, Vue Router

## Архитектура

```
backend/app/
├── main.py                 # Точка входа, lifespan, exception handlers
├── core/
│   ├── config.py           # Настройки (pydantic-settings)
│   ├── security.py         # JWT: создание и декодирование токенов
│   ├── exceptions.py       # Доменные исключения
│   └── dependencies.py     # Dependency Injection (Depends)
├── api/
│   ├── users.py            # Эндпоинты пользователей
│   └── publications.py     # Эндпоинты публикаций
├── schemas/
│   ├── user.py             # Pydantic-модели пользователей
│   └── publication.py      # Pydantic-модели публикаций
├── services/
│   ├── user_service.py     # Бизнес-логика пользователей
│   └── publication_service.py  # Бизнес-логика + горячий кэш
├── repositories/
│   ├── user_repo.py        # SQL-запросы пользователей
│   └── publication_repo.py # SQL-запросы публикаций
├── db/
│   └── postgres.py         # Пул соединений asyncpg, миграция схемы
└── cache/
    └── redis.py            # Redis-клиент
```

**Слои**: API → Service → Repository. Каждый слой знает только о слое ниже. DI реализован через `fastapi.Depends`.

### Frontend

```
frontend/src/
├── api/
│   └── client.ts           # Типы и fetch-обёртки для работы с API
├── components/
│   ├── FeedPage.vue        # Лента публикаций с infinite scroll
│   ├── PublicationModal.vue # Модалка с полной информацией о публикации
│   ├── SearchResults.vue   # Страница результатов поиска (вёрстка по Figma)
│   ├── VideoCart.vue       # Карточка видео (вёрстка по Figma)
│   ├── SideBar.vue         # Боковая навигационная панель (вёрстка по Figma)
│   └── AnalysisModal.vue   # Модалка анализа видео (вёрстка по Figma)
├── utils/
│   └── date.ts             # Утилита форматирования даты
├── router.ts               # Vue Router: /feed, /videos
├── App.vue                 # Корневой layout
└── main.ts                 # Точка входа
```

**Маршруты**:
- `/feed` — лента публикаций, подключена к бэкенду
- `/videos` — страница поиска роликов (вёрстка по Figma)

## Запуск

### Backend

```bash
docker-compose up --build
```

API доступен по адресу: **http://localhost:8000**

Swagger UI: **http://localhost:8000/docs**

### Frontend

> Требует Node.js 18+ и работающего бэкенда (`docker-compose up --build`).

```bash
cd frontend
npm install
npm run dev
```

Приложение откроется по адресу: **http://localhost:5173**

Vite автоматически проксирует запросы `/api/*` на `http://localhost:8000`, поэтому CORS-настройки не нужны.

#### Продакшн-сборка

```bash
npm run build   # собирает dist/
npm run preview # локальный превью сборки на http://localhost:4173
```

## Логика кэширования

- При создании публикации данные сохраняются в PostgreSQL **и** кэшируются в Redis (TTL = 10 минут).
- При запросе публикаций:
  - **Горячие** (< 10 мин) — отдаются из Redis мгновенно.
  - **Холодные** (> 10 мин) — запрашиваются из PostgreSQL с искусственной задержкой 2 сек (симуляция нагрузки).
- Поле `source` в ответе показывает источник: `"cache"` или `"database"`.

## API-эндпоинты

### Пользователи

| Метод    | Путь                        | Описание                                   | Авторизация |
|----------|-----------------------------|--------------------------------------------|-------------|
| `POST`   | `/api/users`                | Создать пользователя (возвращает JWT)      | —           |
| `GET`    | `/api/users/{id}/token`     | Получить JWT по ID (для тестирования)      | —           |
| `PATCH`  | `/api/users/{id}`           | Изменить имя пользователя                  | —           |
| `DELETE` | `/api/users/{id}`           | Удалить пользователя                       | —           |

### Публикации

| Метод    | Путь                                | Описание                                   | Авторизация |
|----------|-------------------------------------|--------------------------------------------|-------------|
| `POST`   | `/api/publications`                 | Создать публикацию                         | Bearer JWT  |
| `PATCH`  | `/api/publications/{id}`            | Изменить публикацию                        | —           |
| `DELETE` | `/api/publications/{id}`            | Удалить публикацию                         | —           |
| `GET`    | `/api/publications/user/{user_id}`  | Получить публикации пользователя (paginated) | —         |

### Пагинация

`GET /api/publications/user/{user_id}?limit=20&offset=0`

Ответ:
```json
{
  "items": [...],
  "total": 42,
  "limit": 20,
  "offset": 0
}
```

### Health check

`GET /health` → `{"status": "ok"}`

## Примеры запросов (curl)

```bash
# Создать пользователя
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'

# Получить токен (для тестирования)
curl http://localhost:8000/api/users/1/token

# Создать публикацию
curl -X POST http://localhost:8000/api/publications \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title": "My Post", "text": "Hello world!"}'

# Получить публикации пользователя
curl "http://localhost:8000/api/publications/user/1?limit=10&offset=0"
```
