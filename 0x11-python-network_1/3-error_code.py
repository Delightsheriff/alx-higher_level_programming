#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
"""

from urllib.request import Request, urlopen
from sys import argv
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    temp = Request(argv[1])

    try:
        with urlopen(temp) as res:
            print(res.read().decode('utf-8'))

    except HTTPError as i:
        print('Error code:', i.code)
