import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://www.billboard.com/charts/hot-100/")

soup = bs(res.text, "lxml")

ranking=soup.select(".u-letter-spacing-0080@tablet")
title=soup.select(".o-chart-results-list-row-container .lrv-u-width-100p #title-of-a-story")
artist=soup.select(".a-truncate-ellipsis-2line")
rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]


# 데이터 프레임 생성
chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title' : titleList,
    'Artist' : artistList
})

# print(chart_df)

# JSON 파일로 저장
chart_df.to_json("billboardChart100.json", force_ascii=False, orient="records")