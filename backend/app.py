from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

url_db = {}
counter = 1


def encode_base62(num):
    result = ""
    while num > 0:
        result = BASE62[num % 62] + result
        num //= 62
    return result


@app.route("/shorten", methods=["POST"])
def shorten_url():
    global counter
    data = request.get_json()
    long_url = data.get("longUrl")

    if not long_url:
        return jsonify({"error": "URL required"}), 400

    short_code = encode_base62(counter)
    url_db[short_code] = long_url
    counter += 1

    return jsonify({
        "shortUrl": f"http://localhost:5000/{short_code}"
    })


@app.route("/<short_code>")
def redirect_url(short_code):
    long_url = url_db.get(short_code)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "URL not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
