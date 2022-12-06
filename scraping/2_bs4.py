import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup객체에서 처음 발견되는 a 엘리먼트를 출력
# print(soup.a.attrs) #a element의 속성정보를 출력
print(soup.a["href"]) #a element의 속성 '값' 정보를 출력 


# pip install lxml 
# pip install beautifulsoup4

# print(soup.find("a", attrs={"class": "Nbtn_upload"}))#a태그를 찾고 싶은데, 어떤 a태그를 찾고싶은지 정의할 수 있음
#a태그에 해당하는데, class의 정보가 "Nbtn_upload"인 녀석에 대해서만 알려줘 라는뜻

# print(soup.find(attrs={"class": "Nbtn_upload"}))

rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)

# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())