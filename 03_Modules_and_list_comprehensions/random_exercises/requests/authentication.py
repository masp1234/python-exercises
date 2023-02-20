import requests
from getpass import getpass

response = requests.get('https://api.github.com/user', auth=('masp1234', getpass()))

print(response.status_code)
