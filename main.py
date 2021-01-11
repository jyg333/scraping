from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

#print(last_indeed_page)# answer is "20" it is working
indeed_jobs = extract_indeed_jobs(last_indeed_page)