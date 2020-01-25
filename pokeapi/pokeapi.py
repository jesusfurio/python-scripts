#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:32:37 2019

@author: chus
"""
import requests

class PokeDex():
    
    def load_data(self):
        
        path = "https://pokeapi.co/api/v2/pokemon/"        
        response = requests.get(path)
        
        if response.status_code == 200:
            
            result = response.json()
            
            for pokemon in result["results"]:
                name = pokemon["name"]
                print (name)
    
    def load_pokemon(self, pokemon):
        #When you write a Pokemon name you could obtain:
        #-Name
        #-Type
        #-Abilities
        #-Sprite 
        
        path = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)
        
        response = requests.get(path)
        
        if response.status_code == 200:
            result = response.json()
            name = result["forms"][0]["name"]
            abilities = list()
            
            for ability in result["abilities"]:
                name_ability = ability["ability"]["name"]
                abilities.append(name_ability)
            
            sprite = result["sprites"]["front_default"]
            
            for types in result["types"]:
                name_types = types["type"]["name"]
            
            print(name)
            print(name_types)
            print(abilities)
            print(sprite)
                       
pokedex = PokeDex()

if __name__ == "__main__":
    pokedex.load_pokemon("pikachu")
