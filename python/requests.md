# Working with `requests`

Examples of using the `requests` library in Python.

# 📚 Python Requests Library - Cheatsheet

## 🔹 Installation

```bash
pip install requests
```

## 🔹 Basic Usage

### Sending a GET request
```python
import requests

response = requests.get('https://example.com')
print(response.status_code)
print(response.headers)
print(response.text)
```

### Sending a POST request
```python
response = requests.post('https://example.com', data={'key': 'value'})
```

### Other HTTP methods
```python
requests.put('https://example.com/put', data={'key': 'value'})
requests.delete('https://example.com/delete')
requests.head('https://example.com/get')
requests.options('https://example.com/get')
```

---

## 🔹 Handling Response Content

- `response.status_code` — HTTP status code (e.g., 200 OK)
- `response.headers` — Headers returned by the server
- `response.text` — Response body as text
- `response.json()` — If the response is JSON, parse it

---

## 🔹 Sending Parameters and Headers

### URL Parameters
```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://example.com/get', params=payload)
```

### Custom Headers
```python
headers = {'Authorization': 'Bearer YOUR_TOKEN'}
response = requests.get('https://example.com/protected', headers=headers)
```

---

## 🔹 Handling Exceptions

```python
try:
    response = requests.get('https://example.com')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

# ✨ Summary
- `requests` makes HTTP communication in Python simple and elegant.
- Understand status codes, headers, and how to work with JSON data.