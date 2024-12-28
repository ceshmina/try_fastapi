from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from diary import get_random_diaries
from python.model.diary import Diary


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
def _index():
    return { 'message' : 'Hello, world!' }


@app.get('/data', summary='Get all data', tags=['Data'], response_model=list[Data])
def _get_data():
    return data.values()


@app.get('/data/{id}', summary='Get data by ID', tags=['Data'], response_model=Data)
def _get_data_by_id(id: int):
    if id not in data:
        raise HTTPException(status_code=404, detail='Data not found')
    return data[id]


@app.get('/diary/random', summary='Get random diary', tags=['Diary'], response_model=Diary)
def _get_random_diaries():
    return get_random_diaries(1)[0]


@app.get('/diary/random/{n}', summary='Get n random diaries', tags=['Diary'], response_model=list[Diary])
def _get_n_random_diaries(n: int):
    return get_random_diaries(n)
