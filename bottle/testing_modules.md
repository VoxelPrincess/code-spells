# Testing Imported Functions in Bottle

This guide explains how to test imported functions in Bottle applications.

## 1. Conditions to Allow Testing

- Functions must be **defined separately** (not hidden inside request handlers).
- Server startup must be inside:

```python
if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True, reload=True)
```

- Functions must **accept arguments** instead of reading `request.json` directly.

## 2. Steps to Test in Terminal

### Step 1 — Open terminal
Go to the project directory:

```bash
cd path/to/your/project
```

### Step 2 — Start Python shell

```bash
python3
```

### Step 3 — Import your module

```python
import rest_api_server
```

## 3. How to Call Functions

✅ Add a person manually:

```python
rest_api_server.create_person({"name": "Teacher", "id": 99})
```

✅ List all persons:

```python
rest_api_server.list_persons()
```

✅ See the result printed out.

## 4. Example Full Session

```bash
$ python3
```

```python
>>> import rest_api_server
>>> rest_api_server.create_person({"name": "Teacher", "id": 99})
>>> rest_api_server.list_persons()
```

## 5. Important Notes

- Server will **NOT** auto-start during import.
- Functions should work **independently** of HTTP requests.
- This method is essential for **unit testing** and **review checks**.

# 🚀 Now you are ready to test Python modules like a professional!
