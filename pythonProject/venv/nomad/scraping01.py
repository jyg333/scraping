import requests
#beautiful soup will be used
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50") # function inside of object

# print(indeed_result.text) #response [200] means okay // .text means show html show everything

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser") #show how many data in page explore and extract data
# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"})
# print(pagination)
pages = pagination.find_all('a')
# print(pages)
spans =[]
for page in pages: #여기에서 pages는 리스트이다.
    # print(page.find("span"))
    spans.append(page.find("span"))
    #array를 만들고 span 을 찾을 때마다 array에 넣어준
print(spans[:-1])#  -1은 마지막에 시작해 첫번째 아이템을 나타내준

#첫번째 과정 끝!! 페이지 추출하기