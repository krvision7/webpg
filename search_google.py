'''
게시판 리스트 테스트를 위한 Google 검색어 크롤링 프로그램

설치 해야하는 라이브러리
pip install --upgrade BeautifulSoup4 requests lxml pymongo googlesearch-python
'''

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
import random
from googlesearch import search

# 몽고DB
client = MongoClient(host="localhost", port=27017)
# myweb 데이터베이스
db = client.myweb
# board 컬렉션
col = db.board

# 구글 검색시 헤더값을 설저하지 않으면 브라우저에서 보이는것과 다른 결과가 나옴
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

# 검색 결과 30개 수집
query = "파이썬 강좌"
for r in search(query, num_results=30, advanced=True):
	# 구글 검색 URL, 검색어는 파이썬
    # 게시물 작성시간 기록을 위해 현재시간 저장 (utc 타임)
    current_utc_time = round(datetime.utcnow().timestamp() * 1000)

    try:
        title = r.title
        contents = r.description

        # 몽고DB에 저장
        # 작성자와 writer_id 설정 필요
        col.insert_one({
            "name": "테스터",
            "writer_id": "",
            "title": title,
            "contents": contents,
            "view": random.randrange(30, 777),
            "pubdate": current_utc_time
        })
    except:
        pass