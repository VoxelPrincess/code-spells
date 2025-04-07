# Compose# 🧩 Docker Compose Basics / Основы Docker Compose

A simple guide for using Docker Compose — a tool for defining and running multi-container Docker applications.  
Простое руководство по Docker Compose — инструменту для описания и запуска многоконтейнерных Docker-приложений.

---

## 📄 docker-compose.yml Example / Пример docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: .
    depends_on:
      - db
    environment:
      DATABASE_URL: postgres://user:password@db:5432/mydb
    ports:
      - "3000:3000"

volumes:
  pgdata:
```

---

## ⚙️ Common Commands / Часто используемые команды

```bash
# Start all services in background
# Запустить все сервисы в фоне
docker-compose up -d

# Stop all services
# Остановить все сервисы
docker-compose down

# View logs
# Просмотреть логи
docker-compose logs -f

# Rebuild services
# Пересобрать сервисы
docker-compose up --build

# Stop and remove containers, networks, volumes
# Остановить и удалить всё
docker-compose down -v
```

---

## 📚 Notes / Примечания

- `services:` — defines containers / определяет контейнеры
- `depends_on:` — specifies dependencies between services / указывает зависимости между сервисами
- `volumes:` — named volumes for persistent data / именованные тома для постоянных данных
- `build:` — builds an image from a Dockerfile / сборка образа из Dockerfile
- `ports:` — host:container port mapping / отображение портов внешний:внутренний
- `environment:` — environment variables passed to the container / переменные окружения

---

## 🔍 Tips / Советы

- Use `.env` file to store environment variables.  
  Используйте `.env` файл для хранения переменных окружения.

- Use `docker-compose.override.yml` for local development settings.  
  Используйте `docker-compose.override.yml` для локальной настройки.

- You can scale services with:  
  Можно масштабировать сервисы:
  ```bash
  docker-compose up --scale backend=3
  ```

---

## ✅ .env Example / Пример .env

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
```

Then reference in `docker-compose.yml`:
```yaml
environment:
  POSTGRES_USER: ${POSTGRES_USER}
  POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
  POSTGRES_DB: ${POSTGRES_DB}
```

---

- [COMMANDS](commands.md)

- [README](../README.md)