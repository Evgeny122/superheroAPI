import json
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)
API_KEY = '10218686935504422'
with open('heroes_data.json', 'r+') as f:
    heroes_data = json.loads(f.read())



class SuperHeroAPI:
    def __init__(self, API=API_KEY, data=heroes_data):
        self._token = API
        self._data = data
        self._url = f'https://superheroapi.com/api/{self._token}'
    
    def get_hero(self, name):
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}')
    
    def _parse_name(self, name):
        return name.lower().title()
    
    def _get_id(self, name):
        data = self._data.get(name, False)
        if data:
            return data
        else:
            raise NotFoundError('Name not found')
    
    def _parse_api(self, url):
        response = requests.get(url, timeout=15)
        response.close()
        return response.json()


class NotFoundError(Exception):
    pass

s = SuperHeroAPI()
result = s.get_hero('superman')
pp.pprint(result)
