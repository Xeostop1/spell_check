# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json

client_id = "R2vZPeiWgP9lcZJwwK0X"
client_secret = "4mSlbIg6_W"

encText = urllib.parse.quote("spdlqj")

# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
url = f"https://openapi.naver.com/v1/search/errata?query={encText}"
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
request.add_header("Host", "openapi.naver.com")
request.add_header("User-Agent", "curl/7.49.1")
request.add_header("Accept", "*/*")

response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print("호출성공")
    print(response_body.decode("utf-8"))

else:
    print("Error Code:" + rescode)
