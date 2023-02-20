import requests

"""
data takes a dictionary, a list of tuples, bytes, or a file-like object. You’ll want to adapt the data you send in the body of your request to the specific needs of the service you’re interacting with.
"""

response = requests.post('https://httpbin.org/post', data={'key': 'value'})


# Hvis det er json data der skal sendes, så brug json parameteren i stedet for data. læg mærke til at den selv ændrer på content-type i request headers og sørger for at det bliver lavet om til json

response = requests.post('https://httpbin.org/post', json={'key': 'value'})


# When you make a request, the requests library prepares the request before actually sending it to the destination server. Request preparation includes things like validating headers and serializing JSON content.

# You can view the PreparedRequest by accessing .request:

print(response.request.headers['content-type'])
print(response.request.url)
print(response.request.body)



