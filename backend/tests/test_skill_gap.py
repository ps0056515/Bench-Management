def test_skill_gap(client):
    response = client.get("/gap/1/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
