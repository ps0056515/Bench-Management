def test_create_demand(client):
    response = client.post("/demand/", json={
        "project_name": "Cloud Migration",
        "required_skills": "AWS, Terraform",
        "min_experience": 6,
        "location": "Bangalore",
        "status": "OPEN"
    })
    assert response.status_code == 200

def test_get_demand(client):
    response = client.get("/demand/")
    assert response.status_code == 200
