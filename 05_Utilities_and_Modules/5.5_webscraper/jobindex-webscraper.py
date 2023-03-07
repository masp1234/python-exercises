from requests_html import HTMLSession
import sys

url = 'https://www.jobindex.dk/jobsoegning/it/systemudvikling/storkoebenhavn'

session = HTMLSession()
response = session.get(url)

# Åbner en light browser i baggrunden, der eksvekverer javascript-koden
# sleep=1 gør at den lige venter et sekund. Bare for at være sikker på, at det hele siden er loadet
response.html.render(sleep=1)

search_words = sys.argv[1:]
jobs = []
results = response.html.find('.PaidJob', containing=search_words)

if len(results) <= 0:
    print(f'There were no jobs containing {search_words}')

else:
    for result in results:
        job_description = []
        link = ''
        paid_jobs = result.find('.PaidJob-inner')
        for paid_job in paid_jobs:
            p_tags = paid_job.find('p')
            for p_tag in p_tags:
                job_description.append(p_tag.text)

        link = result.find('a', containing='Se jobbet')
        for element in link:
            link = element.attrs['href']
        
        jobs.append((job_description, link))


    file = open('jobs.txt', 'w')
    file = open('jobs.txt', 'a')

    for job in jobs:
        location = ''
        description = ''
        for element in job[0][1:]:
            description += f'{element}\n'
        
        file.write(f'Location:\n{job[0][0]}\nDescription:\n{description}\nLink: {job[1]}\n\n')
    
    print(f'Success! {len(jobs)} jobs were found.')
    
       
       
    





