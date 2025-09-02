# 🌐 HTTP Protocol - Basic Concepts

## 🔹 What is HTTP?

**HTTP (HyperText Transfer Protocol)** is the foundation of communication on the World Wide Web.  
It is a request-response protocol between clients and servers.

---

## 🔹 Basic Structure of an HTTP Message

### HTTP Request
- **Request Line** (method, path, version)
- **Headers** (key-value pairs)
- **Optional Body** (for POST, PUT requests)

Example:
```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

---

### HTTP Response
- **Status Line** (version, status code, message)
- **Headers** (key-value pairs)
- **Body** (content like HTML, JSON, etc.)

Example:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

---

## 🔹 HTTP Headers

HTTP headers provide additional information about the request or response. Common headers include:

- `Content-Type`: Specifies the media type of the resource (e.g., `application/json`).
- `Authorization`: Contains credentials for authentication.
- `Cache-Control`: Directives for caching mechanisms.
- `User-Agent`: Identifies the client software.

Example:
```
GET /api/data HTTP/1.1
Host: example.com
Authorization: Bearer <token>
Cache-Control: no-cache
```

---

## 🔹 HTTPS

**HTTPS (HyperText Transfer Protocol Secure)** is an extension of HTTP that uses encryption (via TLS/SSL) to secure communication between clients and servers. It ensures:

- Data integrity
- Confidentiality
- Authentication

Example:
```
https://example.com
```

---

## 🔹 Common HTTP Methods

| Method  | Purpose                         |
|:--------|:---------------------------------|
| GET     | Retrieve data                    |
| POST    | Send new data to server           |
| PUT     | Update existing resource          |
| DELETE  | Remove resource                   |
| HEAD    | Retrieve headers only             |
| OPTIONS | Discover allowed operations       |

---

## 🔹 Important Status Codes

| Code | Meaning             |
|:-----|:--------------------|
| 200  | OK                   |
| 201  | Created              |
| 400  | Bad Request          |
| 401  | Unauthorized         |
| 403  | Forbidden            |
| 404  | Not Found            |
| 500  | Internal Server Error|

---

# ✨ Summary
- HTTP is a simple, text-based protocol.
- Client sends requests; server responds with status, headers, and content.
- Understanding HTTP helps working with APIs and web servers.
- HTTPS adds security to HTTP communication.