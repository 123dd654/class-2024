import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd


head = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}
res = req.get("https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c", headers=head)

soup = bs(res.text, "lxml")

ranking = soup.select(".songs-list-row__rank")
title = soup.select(".songs-list-row__song-name")
artist = soup.select(".songs-list__song-link-wrapper")

rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

print(rankingList)
print(titleList)
print(artistList)


# 데이터 프레임 생성
chart_df = pd.DataFrame({
    'Ranking':rankingList,
    'Title':titleList,
    'Artist':artistList
})

#json 파일로 저장
chart_df.to_json("appleChart100.json", force_ascii=False, orient="records")


