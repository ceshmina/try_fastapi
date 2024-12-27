from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title='Try FastAPI', version='0.1.1')


class Data(BaseModel):
    id: int
    value: str


data = {
    1: Data(id=1, value='value1'),
    2: Data(id=2, value='value2'),
    3: Data(id=3, value='value3'),
}


@app.get('/', summary='Hello, world!', tags=['General'])
def index():
    return { 'message' : 'Hello, world!' }


@app.get('/data', summary='Get all data', tags=['Data'], response_model=list[Data])
def get_data():
    return data.values()


@app.get('/data/{id}', summary='Get data by ID', tags=['Data'], response_model=Data)
def get_data_by_id(id: int):
    if id not in data:
        raise HTTPException(status_code=404, detail='Data not found')
    return data[id]
