#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        temp = argv[1]
    else:
        temp = ''

    try:
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': temp}
        re = requests.post(url, payload).json()

        if {'id', 'name'} <= re.keys():
            print('[{id}] {name}'.format(id=re.get('id'), name=re.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
