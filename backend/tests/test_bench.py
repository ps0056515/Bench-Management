def test_create_bench(client):
    response = client.post("/bench/", json={
        "name": "Ravi Kumar",
        "primary_skills": "AWS, DevOps",
        "secondary_skills": "Terraform",
        "experience_years": 8,
        "bench_start_date": "2024-01-01",
        "location": "Bangalore",
        "status": "BENCH"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Ravi Kumar"

def test_get_bench(client):
    response = client.get("/bench/")
    assert response.status_code == 200
    assert len(response.json()) >= 1
