# 🐳 Docker Commands / Команды Docker

Useful terminal commands for working with Docker.  
Полезные команды для работы с Docker в терминале.

---

## 📦 Images / Образы

```bash
# Pull image from Docker Hub
# Скачать образ из Docker Hub
docker pull <image_name>

# Build an image from Dockerfile
# Построить образ из Dockerfile
docker build -t <your_image_name> .

# List all images
# Показать список всех образов
docker images

# Remove an image
# Удалить образ
docker rmi <image_id_or_name>
```

---

## 🚢 Containers / Контейнеры

```bash
# Run container
# Запустить контейнер
docker run <image_name>

# Run with options
# Запустить с параметрами
docker run -d -p 3000:3000 --name my-app <image_name>

# Stop container
# Остановить контейнер
docker stop <container_id_or_name>

# Remove container
# Удалить контейнер
docker rm <container_id_or_name>

# Stop and remove container
# Остановить и удалить контейнер
docker stop my-app && docker rm my-app

# List containers
# Показать список контейнеров
docker ps               # only running / только запущенные
docker ps -a            # all (including stopped) / все (включая остановленные)
```

---

## 🔍 Inspect & Logs / Просмотр и отладка

```bash
# View container logs
# Логи контейнера
docker logs <container_id_or_name>

# Enter running container
# Подключиться внутрь контейнера
docker exec -it <container_id_or_name> /bin/bash

# Inspect container details
# Получить информацию о контейнере
docker inspect <container_id_or_name>
```

---

## 🧼 Cleanup / Очистка

```bash
# Remove stopped containers
# Удалить все остановленные контейнеры
docker container prune

# Remove unused images
# Удалить все неиспользуемые образы
docker image prune

# Full cleanup (careful!)
# Полная очистка всего (осторожно!)
docker system prune -a
```

---

## 🛠 Volumes & Networks / Томы и сети

```bash
# List volumes
# Посмотреть тома
docker volume ls

# Remove volume
# Удалить том
docker volume rm <volume_name>

# List networks
# Посмотреть сети
docker network ls
```

---

## 🧪 Useful Examples / Полезные примеры

```bash
# Run PostgreSQL container
# Запустить PostgreSQL в Docker
docker run --name pg-db -e POSTGRES_PASSWORD=1234 -d -p 5432:5432 postgres

# Run API server with environment variables
# Запустить сервер с переменными окружения
docker run -d -p 3000:3000 \
  -e DATABASE_URL=postgres://user:pass@host/db \
  --name my-api-container <image>
```

---

## 📚 Notes / Примечания

- `-d` — detached mode (run in background) / режим в фоне
- `-p 3000:3000` — port mapping: host:container / проброс портов: внешний:внутренний
- `--name` — name the container / имя контейнера
- `-e` — set environment variable / установить переменные окружения
- `.` — current directory (used in `docker build`) / текущая директория (для `docker build`)

---

- [COMPOSE](compose.md)

- [README](../README.md)