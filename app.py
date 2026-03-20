from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Toxicity Moderation API Running"


@app.route("/predict")
def predict():
    REQUEST_COUNT.inc()
    text = request.args.get("text", "")

    if any(word in text.lower() for word in ["bad", "hate", "toxic"]):
        return jsonify({"toxicity": "high"})
    return jsonify({"toxicity": "low"})


@app.route("/metrics")
def metrics():
    return generate_latest()


# 👇 IMPORTANT: keep this exactly like this
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)