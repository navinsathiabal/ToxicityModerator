from app import app


def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200


def test_predict():
    client = app.test_client()
    res = client.get("/predict?text=bad")
    assert res.json["toxicity"] == "high"
