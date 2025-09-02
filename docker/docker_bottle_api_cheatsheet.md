# Docker + Bottle API Cheatsheet

This cheatsheet provides examples for running Bottle APIs in Docker containers.

---

## 1. Project structure

```
project_folder/
├── Dockerfile
└── rest_api_server.py
```

---

## 2. Dockerfile (minimal example)

```Dockerfile
FROM python:3

COPY rest_api_server.py /opt

RUN pip install bottle

CMD ["python", "/opt/rest_api_server.py"]
```

---

## 3. Python API file (rest_api_server.py)

```python
from bottle import get, post, run, request, response
import uuid

# In-memory list of persons
persons = [
    {"name": "Emma", "id": 2, "uuid": str(uuid.uuid4())},
    {"name": "Lena", "id": 3, "uuid": str(uuid.uuid4())}
]

@post('/person')
def create_person():
    data = request.json
    data["uuid"] = str(uuid.uuid4())
    persons.append(data)
    response.status = 201
    return data

@get('/person')
def list_persons():
    response.status = 200
    return {"persons": persons}

# Important: host="0.0.0.0" allows Docker to expose the server
if __name__ == '__main__':
    run(host="0.0.0.0", port=8080, debug=True, reload=True)
```

---

## 4. Build Docker image

```bash
docker build -t startcontainer .
```

To force rebuild:
```bash
docker build --no-cache -t startcontainer .
```

---

## 5. Check if port is already in use

```bash
sudo ss -tulpn | grep :8080
```

If needed, kill the process manually:

```bash
sudo kill -9 <PID>
```

Or stop and remove Docker container:

```bash
docker ps
docker stop <ID>
docker rm <ID>
```

---

## 6. Run the container

```bash
docker run --name myserver -p 8080:8080 startcontainer
```

To auto-remove after exit:

```bash
docker run --rm -p 8080:8080 startcontainer
```

---

## 7. Test API with curl

```bash
curl http://localhost:8080/person        # GET all
curl -X POST http://localhost:8080/person   -H "Content-Type: application/json"   -d '{"name": "Anna", "id": 1}'
```

---

## Why `0.0.0.0` in `run()`

- `0.0.0.0` means "listen on all interfaces"
- Required for Docker port mapping to work

---

## Bonus: Check Docker status

```bash
docker ps -a
docker logs <container>
docker images
```

---
