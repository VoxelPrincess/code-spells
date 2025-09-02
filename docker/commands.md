# 🐳 Docker Commands

Useful terminal commands for working with Docker.

---

## 📦 Images

```bash
# Pull image from Docker Hub
docker pull <image_name>

# Build an image from Dockerfile
docker build -t <your_image_name> .

# List all images
docker images

# Remove an image
docker rmi <image_id_or_name>
```

---

## 🚢 Containers

```bash
# Run container
docker run <image_name>

# Run with options
docker run -d -p 3000:3000 --name my-app <image_name>

# Stop container
docker stop <container_id_or_name>

# Remove container
docker rm <container_id_or_name>

# Stop and remove container
docker stop my-app && docker rm my-app

# List containers
docker ps               # only running
docker ps -a            # all (including stopped)
```

---

## 🔍 Inspect & Logs

```bash
# View container logs
docker logs <container_id_or_name>

# Enter running container
docker exec -it <container_id_or_name> /bin/bash

# Inspect container details
docker inspect <container_id_or_name>
```

---

## 🧼 Cleanup

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Full cleanup (careful!)
docker system prune -a
```

---

## 🛠 Volumes & Networks

```bash
# List volumes
docker volume ls

# Remove volume
docker volume rm <volume_name>

# List networks
docker network ls
```

---

## 🧪 Useful Examples

```bash
# Run PostgreSQL container
docker run --name pg-db -e POSTGRES_PASSWORD=1234 -d -p 5432:5432 postgres

# Run API server with environment variables
docker run -d -p 3000:3000 \
  -e DATABASE_URL=postgres://user:pass@host/db \
  --name my-api-container <image>
```

---

## 📚 Notes

- `-d` — detached mode (run in background)
- `-p 3000:3000` — port mapping: host:container
- `--name` — name the container
- `-e` — set environment variable
- `.` — current directory (used in `docker build`)

---

- [COMPOSE](compose.md)

- [README](../README.md)

---

## 🗂 Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. Use a `docker-compose.yml` file to configure your application.

### Common Commands

```bash
# Start services defined in docker-compose.yml
docker-compose up

# Start services in detached mode
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs

# Restart services
docker-compose restart
```

### Example docker-compose.yml

```yaml
version: '3.8'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  app:
    build:
      context: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```