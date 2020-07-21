import requests
from ApiToken import trefle_token

# Using Python Requests library to get from the API
r = requests.get(f'https://trefle.io/api/v1/plants?filter_not%5Bmaximum_height_cm%5D=null&filter%5Bligneous_type%5D=tree&order%5Bmaximum_height_cm%5D=desc&token={trefle_token}')
jsonResponse = r.json()
# Iterating through JSON response
# for key, value in jsonResponse.items():
#     print(key, ":", value)
