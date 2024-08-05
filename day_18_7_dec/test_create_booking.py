import pytest
import requests

@pytest.mark.positive
def test_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json" }
    payload = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 112,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(URL, headers=headers, json=payload)
    assert response.status_code == 200
    data=response.json()
    bookingid = (data["bookingid"])
    print("bookingid is ",bookingid)

    assert data["booking"]["firstname"]=="Sally","its is incorrect"
    assert data["bookingid"]!=0,"then its correct"

@pytest.mark.negative

def test_booking1():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json" }
    payload = {}

    response = requests.post(URL, headers=headers, json=payload)
    assert response.status_code == 500



