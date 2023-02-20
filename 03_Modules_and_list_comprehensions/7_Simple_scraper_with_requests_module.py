import requests
import os


response = requests.get('https://google.com')
print(response.text)
file = open('index.html', 'w')
file.writelines(response.text)

