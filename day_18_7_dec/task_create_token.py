import  requests
import pytest


def create_token():
    url="https://restful-booker.herokuapp.com/auth"
    headers={}
    payload={
    "username" : "admin",
    "password" : "password123"
}
    response=requests.post(url,headers,json=payload)

    data=response.json()
    tokenid=data["token"]
    print(tokenid)
    return tokenid 

def create_booking():
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
    return bookingid

def test_put_request():
    URL="https://restful-booker.herokuapp.com/booking/"
    puturl=URL+str(create_booking())
    token_val= create_token()
    headers={"Content-Type":"application/json",
            "Cookie": f"token={token_val}"
             }
    json_payload={
    "firstname" : "James",
    "lastname" : "bhavi",
    "totalprice" : 1234567,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response=requests.put(url=puturl,headers=headers,json=json_payload)

    assert response.status_code == 200

def test_delete_request():
    URL="https://restful-booker.herokuapp.com/booking/"
    puturl=URL+str(create_booking())
    token_val= create_token()
    headers={"Content-Type":"application/json",
            "Cookie": f"token={token_val}"
             }
    response=requests.delete(url=puturl,headers=headers)

    assert response.status_code == 201