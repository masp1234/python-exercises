from requests_html import HTMLSession
import sys

url = 'https://thehub.io/jobs?positionTypes=5b8e46b3853f039706b6ea73&sorting=mostPopular'

session = HTMLSession()


search_words = ['python']

def scrape_links():
    links = []
    more_content = True
    page_number = 0
    while more_content is True:
        print(page_number)
        response = session.get(f'{url}&page={page_number}')
        response.html.render(sleep=1)
        
        job_results = response.html.find('.card__content')
        print(job_results)
        if len(job_results) <= 0 or page_number == 1:
            print("no results")
            more_content = False
        else:
            for job_result in job_results:
                links.append(get_job_result_link(job_result))
                print('Length of links: ', len(links))
                
                
        page_number = page_number + 1
    
    scrape_jobs(links)
            


def get_job_result_link(job_result):
    link = job_result.find('.card-job-find-list__link', first=True).attrs['href']
    print(link)
    return link


def scrape_jobs(links):
    jobs = []
    
    for link in links:
        job_url = f'https://thehub.io{link}'
        response = session.get(job_url)
        response.html.render()
        results = response.html.find('.text-block__content')

        if results:
            title = response.html.find('.view-job-details__title', first=True).text
            descriptions = response.html.find('.bullet-inline-list')
            description_string = ''
            for description in descriptions:
                
                description_string += f'{description.text}\n'
            
            jobs.append((title, description_string, job_url))
    print(jobs)
        



scrape_links()
