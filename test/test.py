from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_middleware():
    response = client.get(url="/middleware/")
    assert response.status_code == 200
    assert response.json() == {"message": "Middleware"}
    assert response.headers["x-method"] == "It was request GET method."
