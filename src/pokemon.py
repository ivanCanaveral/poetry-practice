""" Some requests here """

import requests

def get_pikachu_id():
    """ gets pikachu id"""
    resp = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    return resp.json()['id']
