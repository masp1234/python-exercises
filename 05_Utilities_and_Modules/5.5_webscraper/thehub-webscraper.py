from requests_html import HTMLSession
import sys

url = 'https://thehub.io/jobs?positionTypes=5b8e46b3853f039706b6ea73&sorting=mostPopular'

session = HTMLSession()

links = []

def scrape_links():
    page_number = 0
    response = session.get(f'{url}&page={page_number}')
    print(response)



scrape_links()