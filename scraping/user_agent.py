import requests
url = "https://medium.com/javascript-in-plain-english/leetcode-110-balanced-binary-tree-javascript-49ec9ddf9318"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("index.html", "w", encoding="utf8") as f:
  f.write(res.text)
  