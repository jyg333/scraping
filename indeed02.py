import requests
from bs4 import BeautifulSoup

LIMIT = 50  # 나중에 바꿔주기 위해서 f string을 사용해서 나타내준
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


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


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")

    if company_anchor is not None:
        company = str(company_anchor.string)  # 출력 값에 빈간이 너무 많아 str 사용했지만 여전히 빈칸이 너무 많다. -> 3 times next line
    else:
        company = str(company.string)
    company = company.strip()  # 빈공간 삭제
    #location = html.find("span",{"class":"location"})#location is class , none 인 location 이 있어서 "span"->"div"로 찾아보자
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    print(job_id)
    return {
        'title': title,
        'company': company,
        'location':location,
        "link":f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    # print(f"&start={page*LIMIT}")
    for page in range(last_page):
        print(f'Scrapping page {page}')
        result = requests.get(f"{URL}&start={0 * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    # print(result.status_code)
    # print(results)
    for result in results:  # results is list
        job = extract_job(result)
        jobs.append(job)
    return jobs
# 회사이름이 링크가 있는것이 있고 없는 것이 있어서 문제가 발생했다.
# link가 있는것은 anchor안에 string을 가지고 오고 링크가 없는것은 span의 string을 가지고 온다
# company는 soup이었는데 anchor를 넣어준 후 string 을 입력

