import sys
import requests

def url_ok(argv):
    if len(argv) < 2:
        print('Usage: python script.py [url]')
        sys.exit()
    else:
        res = requests.get(argv[1])
        if res.status_code == 200:
            print('Sucess!, you have entered a valid url')
