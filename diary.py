from dataclasses import dataclass
import json
import os
from urllib.request import Request, urlopen


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


def get_diaries_from_github(path: str):
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


if __name__ == '__main__':
    diaries = get_diaries_from_github('_articles')
    for diary in diaries[:10]:
        print(diary)
