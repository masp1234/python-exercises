from requests_html import HTMLSession
import sys

url = 'https://www.jobindex.dk/jobsoegning/it/systemudvikling/storkoebenhavn'

session = HTMLSession()




def scrapeJobs():
    page_number = 0
    moreContent = True
    jobs = []
    
    while moreContent is True:
        response = session.get(f'{url}?page={page_number}')

        # Åbner en light browser i baggrunden, der eksvekverer javascript-koden
        # sleep=1 gør at den lige venter et sekund. Bare for at være sikker på, at det hele siden er loadet
        response.html.render(sleep=1)
        search_words = sys.argv[1:]
        job_results = response.html.find('.PaidJob')
    
        if len(job_results) <= 0:
            print(f'The search stopped at page: {page_number} and yielded: {len(jobs)} job(s)')
            moreContent = False

        else:
            job_results = response.html.find('.PaidJob', containing=search_words)
            for job_result in job_results:
                jobs.append(createJobResult(job_result))

            page_number = page_number + 1
            print(f'Page number: {page_number}\nJobs found so far: {len(jobs)}\n')
                
        
            
    createFile(jobs)
            

def createJobResult(job_result):
    job_description = []
    link = ''
    paid_jobs = job_result.find('.PaidJob-inner')
    for paid_job in paid_jobs:
        p_tags = paid_job.find('p')
        for p_tag in p_tags:
            job_description.append(p_tag.text)
            link = job_result.find('a', containing='Se jobbet')
            for element in link:
                link = element.attrs['href']
    
    return (job_description, link)
        
def createFile(jobs):
        file = open('jobs.txt', 'w')
        file = open('jobs.txt', 'a')

        for job in jobs:
            description = ''
            for element in job[0][1:]:
                description += f'{element}\n'
            
            file.write(f'Location:\n{job[0][0]}\nDescription:\n{description}\nLink: {job[1]}\n\n')

scrapeJobs()




    
       
       
    





