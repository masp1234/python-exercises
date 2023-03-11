from requests_html import HTMLSession
import sys

url = 'https://thehub.io/jobs?positionTypes=5b8e46b3853f039706b6ea73&sorting=mostPopular'

session = HTMLSession()

links = []

def scrape_links():
    more_content = True
    page_number = 0
    links = []
    while more_content is True:
        response = session.get(f'{url}&page={page_number}')
        response.html.render(sleep=1)
        search_words = ['python']
        job_results = response.html.find('.card__content')
        if len(job_results) <= 0:
            print("no results")
        else:
            for job_result in job_results:
                print(job_result)
                links.append(get_job_result_link(job_result))
                print(len(job_results))
                page_number = page_number + 1
                print(page_number)


def get_job_result_link(job_result):
    link = job_result.find('.card-job-find-list__link', first=True).attrs['href']
    print(link)

scrape_links()