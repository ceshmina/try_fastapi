from dataclasses import dataclass
from datetime import datetime
import json
import os
import random
from urllib.request import Request, urlopen

from python.model.diary import Diary


@dataclass
class DiaryMeta:
    name: str
    download_url: str


OWNER = 'ceshmina'
REPO = 'eskarun'
GITHUB_PAT = os.environ.get('GITHUB_PAT')
HEADERS = {
    'Authorization': f'BEARER {GITHUB_PAT}'
}


def get_diaries_from_github(path: str) -> list[DiaryMeta]:
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/{path}'
    print(f'Fetching from {url} ...')
    result = []

    with urlopen(Request(url, headers=HEADERS)) as response:
        diaries = json.loads(response.read())

    for diary in diaries:
        if diary.get('type') == 'file':
            result.append(DiaryMeta(
                name=diary.get('name'),
                download_url=diary.get('download_url'))
            )
        elif diary.get('type') == 'dir':
            result.extend(get_diaries_from_github(diary.get('path')))
        
    return result


def get_content_from_github(download_url: str) -> str:
    print(f'Fetching from {download_url} ...')
    with urlopen(Request(download_url, headers=HEADERS)) as response:
        return response.read().decode('utf-8')


def get_random_diaries(n: int) -> list[Diary]:
    diary_metas = random.sample(get_diaries_from_github('_articles'), n)
    diaries = []

    for diary_meta in diary_metas:
        content = get_content_from_github(diary_meta.download_url)
        diaries.append(Diary(
            date=datetime.strptime(diary_meta.name[:8], '%Y%m%d').date(),
            content=content
        ))

    return diaries


if __name__ == '__main__':
    diaries = get_random_diaries(3)
    for diary in diaries:
        date_str = diary.date.strftime('%Y年%-m月%-d日')
        print(f'{date_str}:\n{diary.content}\n\n\n')
