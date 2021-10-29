# SSL Check API

SSL/TLS 検証をするためのAPIです。

## 開発時

```
(venv) pip install -r requirements.txt
```

```
(venv) python src/manage.py runserver

or

(venv) uvicorn src.app:app --reload --workers 1 --host 0.0.0.0 --port 8080
```

API ドキュメント
- OpenAPI | http://localhost:8080/docs
- ReDoc | http://localhost:8080/redoc