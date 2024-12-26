# try_fastapi

FastAPIの学習用

## 開発

以下コマンドで開発用コンテナ (`localhost:8081`) を起動します。

```
docker compose up python
```

devcontainerを使っている場合は、コンテナ内で以下コマンドを実行してください。

```
uv run uvicorn main:app --host 0.0.0.0 --reload
```
