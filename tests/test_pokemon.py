import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = 'e16b156dcc6580cc8acf62c4843e3417'

def test_status_code():
        response =  requests.get(f'{host}/trainers')
        assert response.status_code == 200

def test_trainer_name():
        response =  requests.get(f'{host}/trainers', 
                    params = {'trainer_id' : 3394})
        assert response.json()['trainer_name'] == 'Oleg'