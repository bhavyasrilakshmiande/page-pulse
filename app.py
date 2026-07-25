from flask import Flask, request, jsonify, render_template
from utils import validate_url, fetch_webpage, parse_html_metrics
import requests
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/audit", methods=["POST"])
def audit():
    data = request.get_json()
    url = data.get("url")

    if not validate_url(url):
        return jsonify(success=False, error="Invalid URL"), 400

    start_time = time.time()

    try:
        response = fetch_webpage(url)
        response_time = (time.time() - start_time) * 1000

        if response is None:
            return jsonify(success=False, error="Unable to fetch page"), 400

        metrics = parse_html_metrics(response)

        return jsonify(
            success=True,
            http_status=response.status_code,
            response_time=response_time,
            page_title=metrics["title"],
            meta_description=metrics["meta_description"],
            h1_count=metrics["h1_count"],
            images_missing_alt=metrics["images_missing_alt"],
            word_count=metrics["word_count"]
        )

    except requests.exceptions.Timeout:
        return jsonify(success=False, error="Request timed out"), 408

    except requests.exceptions.RequestException as e:
        return jsonify(success=False, error=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True)