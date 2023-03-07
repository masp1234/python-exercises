import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
# print(job_elements)
print(type(python_jobs))

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    job_title = job_element.find('h2', class_='title').text.strip()
    job_company = job_element.find('h3', class_='company').text.strip()
    job_location = job_element.find('p', class_='location').text.strip()
    # finder begge links
    links = job_element.find_all('a')
    # tager index 1 og tilgår href attributen, som indeholder link-teksten
    link_url = links[1]['href']
    print(f'Apply here: {link_url}')

    print(job_title, job_company, job_location)



    
