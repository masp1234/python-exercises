from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
import requests

url = 'https://au.indeed.com/jobs?q=Software+developer&l=&vjk=5151e6184bed21c5'

asession = AsyncHTMLSession()

async def get_indeed():
    response = await asession.get(url)
    return response


results = asession.run(get_indeed)
print(results)
job_results = results[0].html.find('.jobsearch-ResultsList')

for job_result in job_results:
    print(job_result)