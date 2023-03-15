import requests

host = 'https://pokemonbattle.me:9104'
token = 'e16b156dcc6580cc8acf62c4843e3417'

response = requests.post(f'{host}/pokemons',    
                    headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
                    json = {'name' : 'OlegPika', 'photo' : 'https://dolnikov.ru/pokemons/albums/009.png'})
print(response.text)

response = requests.put(f'{host}/pokemons',    
                    headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
                    json = {'pokemon_id' : 6170, 'name' : 'OlegChu', 'photo' : ''})
print(response.text)

response = requests.post(f'{host}/trainers/add_pokeball',    
                    headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
                    json = {'pokemon_id' : 6170})
print(response.text)