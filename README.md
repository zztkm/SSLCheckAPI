# SSL Check API

SSL/TLS 検証をするためのAPIです。

## 開発時

```
(venv) pip install -r dev-requirements.txt
```

```
(venv)
uvicorn src.app:app --reload --workers 1 --host 0.0.0.0 --port 8080
```

API ドキュメント
- OpenAPI | http://localhost:8080/docs
- ReDoc | http://localhost:8080/redoc

## 注意

requirements.txt を編集する場合は、dev-requirements.txt も同時に編集してください。