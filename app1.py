from flask import Flask, render_template, request, jsonify
import urllib.request
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index1.html")


@app.route("/spell_check", methods=["POST"])
def spell_check():
    text = request.form["text"]
    print(f"서버로 전달된 텍스트: {text}")
    print(f"api 호출 시작")
    client_id = "R2vZPeiWgP9lcZJwwK0X"
    client_secret = "4mSlbIg6_W"
    # url = "https://openapi.naver.com/v1/search/errata.json?query="+text
    url = (
        "https://openapi.naver.com/v1/search/errata.json?query=" + text + "&output=json"
    )
    request_api = urllib.request.Request(url)
    request_api.add_header("X-Naver-Client-Id", client_id)
    request_api.add_header("X-Naver-Client-Secret", client_secret)
    request_api.add_header("Host", "openapi.naver.com")
    request_api.add_header("User-Agent", "curl/7.49.1")
    request_api.add_header("Accept", "*/*")
    response = urllib.request.urlopen(request_api)
    rescode = response.getcode()

    if rescode == 200:
        print(f"api 호출 성공")
        response_body = response.read()
        result = json.loads(response_body.decode("utf-8"))

        wrong_words = result["result"]["item"][0]["errata"]
        # wrong_words = result['message']['result']['errata']
        correct_words = result["result"]["item"][0]["errata"]
        # correct_words = result['message']['result']['correct']
        print(f"잘못된 단어: {wrong_words}")
        print(f"정정된 단어: {correct_words}")
    else:
        print(f"api 호출실패")
        wrong_words = []
        correct_words = []

    return jsonify({"wrong_words": wrong_words, "correct_words": correct_words})


# 향후 업데이트
# @app.route('/translate_text', methods=['POST'])
# def translate_text():
#     text = request.json['text']


#     translated_text = 'Example Translated Text'

#     return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
