#api
#we need request lib to make get post put patch delete and verify
#to perform curd operations

import requests

def main():
    response=requests.get("https://restful-booker.herokuapp.com/booking/29")
    assert response.status_code==200
    data=response.json()

    #assertions

    assert 'firstname' in data,"sally"
    assert 'lastname' in data,"its is present"

    assert data["firstname"]=="Josh","first name is correct"
    assert data["lastname"]=="Allen","last  is also incorrect"
    assert data["bookingdates"]["checkin"]=="2018-01-01"

if __name__ == '__main__':
    main()