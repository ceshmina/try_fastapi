FROM python:3.13-slim

RUN pip install uv==0.5.11
WORKDIR /app
COPY . .
RUN uv sync

CMD [ "uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0" ]
