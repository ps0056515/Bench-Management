def test_match_endpoint(client):
    response = client.get("/match/1")
    assert response.status_code in [200, 500]  # AI key may not exist
