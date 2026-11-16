from fastapi import FastAPI
from fastapi.testclient import TestClient

from business.errors import BusinessError
from main import business_error_handler


def test_business_error_wird_zu_400():
    app = FastAPI()
    app.add_exception_handler(BusinessError, business_error_handler)

    @app.get("/fail")
    def fail():
        raise BusinessError("Something is not allowed.")

    response = TestClient(app).get("/fail")

    assert response.status_code == 400
    assert response.json() == {"error": "Something is not allowed."}
