import requests
import json

class Pokedex:
    _list = []
    
    def __init__(self, name, type_, height, weight, stats, abilities):
        self.name = name
        self.type_ = type_
        self.height = height
        self.weight = weight
        self.stats = stats # health, attack, speed {dictionary}
        self.abilities = abilities # attack moves {dictionary}
    
class Program:
    
    base_url = "https://pokeapi.co/api/v2/pokemon/"
#     def __init__(self,):
#         self.response = requests.get(api_call).json()['name']['type']['height']['weight']['stats']['abilities']
#         self.pokemon = []
#         data = response.json()
        
    def run(self):
        name = input("What pokemon would you like to add? ")
        api_call = f"{self.base_url}{name}"
        response = requests.get(api_call)
        self.data = response.json()
        print(self.data["name"])
        print(self.data["height"])
        print(self.data["weight"])
        print(self.data["types"])
        print(self.data["abilities"])
        
#         types = (self.data["types"])
#         print(types)(1)
#         abilities = (self.data["abilities"])
#         print(abilities)
#         ability = (abilities[1])
#         print(abilitiy)
#         print(self.data["types", "name"])
        # how to loop over and get specific stats
        # access keys to get the values we want
        
    
    

program = Program()
program.run()

#use the api special method to call the request for stats