from shamrock import Shamrock
from apitoken import trefle_token
api = Shamrock(trefle_token)
plants = api.plants()
print(plants)