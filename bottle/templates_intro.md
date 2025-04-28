# 🧩 Introduction to Templates in Bottle

## What is a Template?

A **template** in Bottle is a way to **separate** Python logic (backend) from HTML layout (frontend).

- Python handles data processing.
- Templates handle how the data is shown to users.

✅ This keeps the code cleaner and easier to maintain.

## Why Use Templates?

- To **avoid writing HTML directly in Python code**.
- To **make it easier to update the look** of a website without touching the logic.
- To **reuse** layouts for multiple pages.

## Minimal Example

### Python File (rest_api_server.py)

```python
from bottle import get, run, template

@get('/hello')
def hello():
    return template('hello_template', name='Anna')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reload=True)
```

### Template File (views/hello_template.tpl)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello {{name}}!</h1>
</body>
</html>
```

## Folder Structure Example

```
code-spells/
└── bottle/
    ├── rest_api_server.py
    ├── templates_intro.md
    └── views/
        └── hello_template.tpl
```

## ✨ Summary

✅ Templates keep your Python code clean.  
✅ Templates make it easy to change website designs without touching backend code.  
✅ Bottle uses the `template()` function to load `.tpl` files from the `views/` folder.
