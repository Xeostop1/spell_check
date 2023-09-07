from flask import Flask, render_template, request, jsonify
import urllib.request
import json
import urllib.parse


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/spell_check", methods=["POST"])
def spell_check():
    if request.is_json:
        data = request.get_json()
        received_text = data["text"]
        # the rest of your code...
    else:
        return "Request body is not in JSON format", 400
    # 여기는 클라키가 되는데 거기는 왜 안돼지? 진짜 알수가 없다 내가~~~ 
    client_id = "R2vZPeiWgP9lcZJwwK0X"
    client_secret = "4mSlbIg6_W"

    # encText = urllib.parse.quote("spdlqj")
    encText = urllib.parse.quote(received_text)

    url = f"https://openapi.naver.com/v1/search/errata?query={encText}"

    api_request = urllib.request.Request(url)

    api_request.add_header("X-Naver-Client-Id", client_id)
    api_request.add_header("X-Naver-Client-Secret", client_secret)
    api_request.add_header("Host", "openapi.naver.com")
    api_request.add_header("User-Agent", "curl/7.49.1")
    api_request.add_header("Accept", "*/*")

    response = urllib.request.urlopen(api_request)

    if response.getcode() == 200:
        response_body = response.read()
        result_json_str = response_body.decode("utf-8")
        print(f"1: {result_json_str}")

        result = json.loads(result_json_str)

        wrong_word = encText
        correct_word = list(result.values())[0]

        return jsonify({"wrong_word": wrong_word, "correct_word": correct_word})


if __name__ == "__main__":
    app.run(debug=True)
