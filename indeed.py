import requests
from bs4 import BeautifulSoup

LIMIT = 50 #나중에 바꿔주기 위해서 f string을 사용해서 나타내준
URL=f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"



def extract_indeed_pages():
    result = requests.get(URL)  # function inside of object
    soup = BeautifulSoup(result.text, "html.parser")  # show how many data in page explore and extract data
    pagination = soup.find("div", {"class": "pagination"})  # whatever we find "div","class" inside of indeed_soup
    #
    links = pagination.find_all('a')  # we find all the links 'a'
    # print(pages)
    pages = []
    for link in links[:-1]:  # 여기에서 pages는 리스트이다.
        pages.append(int(link.string))
        # array를 만들고 span 을 찾을 때마다 array에 넣어준

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):
    #print(f"&start={page*LIMIT}")
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    #print(result.status_code)
    #print(results)
    for result in results:# results is list
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        print(title)
    return jobs
#result have the job and next find title
