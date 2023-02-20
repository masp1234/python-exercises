import requests

# Passing a dictionary to the params parameter. Can also pass a list of tuples
# [('q', 'requests+language:python)]
response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'})
data = response.json()


jsonResponse = response.json()
repository = jsonResponse['items'][0]

print(f'Repository name: {repository["name"]}')
print(f'Repository description: {repository["description"]}')


