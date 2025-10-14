# # Use python -m pytest -v in Powershell
# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)


# def test_hello():
#     r = client.get("/hello")
#     assert r.status_code == 200
#     assert r.json() == {"message": "Hello, Seam AI!"}


# def test_predict():
#     r = client.post("/predict", json={"text": "hello"})
#     assert r.status_code == 200
#     assert "score" in r.json()
#     assert "score" in r.json()
