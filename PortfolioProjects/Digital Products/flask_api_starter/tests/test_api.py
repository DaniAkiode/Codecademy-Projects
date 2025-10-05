import json 
from app import app

def test_get_users():
    client = app.test_client()
    response = client.get("/users/")
    assert response.status_code == 200

def test_create_user():
    client = app.test_client
    response = client.post("/users/",
                           data=json.dumps({"name": "Alice"}),
                           content_type="application/json")
    assert response.status_code == 201