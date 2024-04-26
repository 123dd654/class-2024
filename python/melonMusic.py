import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

head = {'user-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}
res = req.get("https://www.melon.com/chart/index.htm", headers=head)

soup = bs(res.text, "lxml")

ranking=soup.select("tbody .rank")
title=soup.select(".rank01 > span > a")
artist=soup.select(".rank02 > span > a:nth-child(1)")
rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

print(rankingList)

# 데이터 프레임 생성
chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title' : titleList,
    'Artist' : artistList
})

# print(chart_df)

# JSON 파일로 저장
chart_df.to_json("melonChart100.json", force_ascii=False, orient="records")