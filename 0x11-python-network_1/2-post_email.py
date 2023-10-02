#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = sys.argv[2]
data = {"email": email}
data = urllib.parse.urlencode(data).encode("utf-8")
request = urllib.request.Request(url, data)


if __name__ == "__main__":
    with urllib.request.urlopen(request) as response:
        data = response.read()
        html = data.decode("utf-8")
        print(html)
