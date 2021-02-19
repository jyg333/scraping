# Scraping data in stackoverflow
#step 1: get the page, 2: make the request, 3: extrack the jobs
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&pg"
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a") #find_all the pages//find get only one
    print(pages)

def get_jobs():
    last_page = get_last_page()
    return []