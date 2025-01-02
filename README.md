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

## ドキュメント

`localhost:8081/docs`

## デプロイ

事前にECRにログインしてください。

```
aws --region ap-northeast-1 ecr get-login-password --profile ${PROFILE} | docker login --username AWS --password-stdin ${PROJECT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-sample
```

デプロイ用のコンテナイメージを以下コマンドでビルドし、ECRにプッシュします。

```
docker compose build nginx
docker tag try_fastapi-nginx:latest ${PROJECT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-sample/nginx:latest
docker push ${PROJECT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-sample/nginx:latest

docker compose build python
docker tag try_fastapi-python:latest ${PROJECT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-sample/python:latest
docker push ${PROJECT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/fastapi-sample/python:latest
```

TODO: ECSへの反映方法を記載する
