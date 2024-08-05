import pytest
import requests

def test_sample():
     response = requests.get("https://restful-booker.herokuapp.com/booking/29")
     assert response.status_code == 200
     data = response.json()

     # assertionsc
     #verifications of key
     assert 'firstname' in data, "sally"
     assert 'lastname' in data, "its is present"
     # verifications of data
     assert data["firstname"] == "Jane", "first name is correct"
     assert data["lastname"] == "Doe", "last  is also incorrect"
     assert data["bookingdates"]["checkin"] == "2018-01-01"
