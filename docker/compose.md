# 🧩 Docker Compose Basics

A simple guide for using Docker Compose — a tool for defining and running multi-container Docker applications.

---

## 📄 docker-compose.yml Example

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

## ⚙️ Common Commands

```bash
# Start all services in background
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild services
docker-compose up --build

# Stop and remove containers, networks, volumes
docker-compose down -v
```

---

## 📚 Notes

- `services:` — defines containers.
- `depends_on:` — specifies dependencies between services.
- `volumes:` — named volumes for persistent data.
- `build:` — builds an image from a Dockerfile.
- `ports:` — host:container port mapping.
- `environment:` — environment variables passed to the container.

---

## 🔍 Tips

- Use `.env` file to store environment variables.
- Use `docker-compose.override.yml` for local development settings.
- You can scale services with:
  ```bash
  docker-compose up --scale backend=3
  ```

---

## ✅ .env Example

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