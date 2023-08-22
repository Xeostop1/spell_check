import os
import sys
import urllib.request
from flask import Flask

app = Flask(__name__)

@app.route('/search/<word>')
def spell_check(word):
    client_id = "R2vZPeiWgP9lcZJwwK0X"
    client_secret = "4mSlbIg6_W"
    url = f"https://openapi.naver.com/v1/search/errata.json?query={word}"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Host", "openapi.naver.com")
    request.add_header("User-Agent", "curl/7.49.1")
    request.add_header("Accept", "*/*")
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        result = response_body.decode('utf-8')
        return result
    else:
        return "Error Code: " + str(rescode)

keyword="spdlqj"
spell_check(keyword)
# 실행
if __name__ == "__main__":
    app.run(port=8000)
