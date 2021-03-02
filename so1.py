# Scraping data in stackoverflow
#step 1: get the page, 2: make the request, 3: extrack the jobs
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&pg"
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a") #find_all the pages//find get only one
    last_pages = pages[-2].get_text(strip=True) # 마지막 페이지 수를 불러온
    #print(last_pages)
    return int(last_pages) # range(last_page)에서 string을 인식할 수 없기 때문에 integer 형식으로 바꿔준


def extract_job(html):
    title = html.find("h2",{"class":'mb4'}).find("a")["title"]
    company, location= html.find("h3",{"class":"fc-black-700"}).find_all("span",recursive=False)# first span is company name, second span is location
    """Unpacking value, 리스트 안에 요소를 이미 알고 있어서 가능하다."""
    print(company.get_text(strip = True), location.get_text(strip = True)) #.text_get print() 할때 <span>을 제외하고 문자열만 출
    return {'title': title}
# recursive 는 find_all이 모든것을 가져오는것을 방지하기 위해서 쓰인다. not to go deep, 첫번째 span만 가져옴

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{URL}&pg={page+1}')
        #print(result.status_code)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
        return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs