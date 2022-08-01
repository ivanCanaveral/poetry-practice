""" Some requests here """

import requests

def get_pikachu_order():
    """ gets pikachu order"""
    resp = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    return resp.json()['order']