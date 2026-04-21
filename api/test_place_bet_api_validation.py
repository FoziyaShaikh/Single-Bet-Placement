import pytest
import requests
from config.settings import BASE_URL, USER_ID

#user-id for authentication
HEADERS={"x-user-id":USER_ID} 

"""
Entering stake more than the maximum allowed and verifying that the appropriate error message is displayed.
"""


def test_place_bet_exceeding_max_stake():
    # Define the endpoint and payload with a stake exceeding the maximum allowed
    endpoint = f"{BASE_URL}/api/place-bet"
    payload = {
        "matchId": "premier-league-manutd-chelsea",
        "selection": "HOME",
        "stake": 102.00  # Assuming the maximum allowed stake is 100.00
       }

    # Send the POST request to place the bet

    response = requests.post(endpoint, headers=HEADERS, json=payload)
    print(f"Response status code: {response.status_code}")
    print(response.text)

    # Assert that the response status code indicates an error (e.g., semantic validation failures (selection/stake/matchId) should return 422)

    assert response.status_code == 422, f"Expected status code 422, but got {response.status_code}"
    assert "Stake must be at most 100.00" in response.text, f"Expected error message about maximum stake, but got: {response.text}"



    
   
