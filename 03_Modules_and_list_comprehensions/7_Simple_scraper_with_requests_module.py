import requests
import os


response = requests.get('https://github.com')
file = open('index.html', 'w')
file.writelines(response.text)

