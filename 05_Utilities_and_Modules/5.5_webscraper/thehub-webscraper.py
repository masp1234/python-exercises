from requests_html import HTMLSession
import sys

url = 'https://thehub.io/jobs?positionTypes=5b8e46b3853f039706b6ea73&sorting=mostPopular'

session = HTMLSession()


search_words = sys.argv[1:]

def scrape_links():
    links = []
    more_content = True
    page_number = 0
    while more_content is True:
        response = session.get(f'{url}&page={page_number}')
        response.html.render(sleep=1)
        
        job_results = response.html.find('.card__content')
        if len(job_results) <= 0 or page_number == 2:
            more_content = False
        else:
            for job_result in job_results:
                links.append(get_job_result_link(job_result))  
        page_number = page_number + 1
        print(f'On page: {page_number}')
    
    scrape_jobs(links)
            


def get_job_result_link(job_result):
    link = job_result.find('.card-job-find-list__link', first=True).attrs['href']
    return link


def scrape_jobs(links):
    jobs = []
    
    for link in links:
        print(f'Scraping link: {link}')
        job_url = f'https://thehub.io{link}'
        response = session.get(job_url)
        response.html.render()
        results = response.html.find('.text-block__content', containing=search_words)

        if results:
            title = response.html.find('.view-job-details__title', first=True).text
            descriptions = response.html.find('.bullet-inline-list')
            description_string = ''
            for description in descriptions:
                
                description_string += f'{description.text}\n'
            
            jobs.append((title, description_string, job_url))
    print(f'Finished scraping and found: {len(jobs)} job(s).\nWriting to file...')
    create_file(jobs)


def create_file(jobs):
    file = open('thehub-jobs.txt', 'w')
    for job in jobs:
        file.write(f'Jobtitle: {job[0]}\nDescription:\n{job[1]}\nLink: {job[2]}\n\n')
        



scrape_links()
