# -----------------------------------------------------------
# Date: 03/31/2022
# 
# Defines the MagicItems class, which stores the magic items
# data
# -----------------------------------------------------------

import json
import random as r

class MagicItems:
    '''MagicItems class


    '''
    def __init__(self, json_file):
        self.json_filename = json_file
        with open(json_file, 'r') as file:
            self.items = json.load(file)
        
        # Randomizes the prices if this is the data
        # does not contain prices. Otherwise, it
        # varies the prices based on a Triangle
        # distrubition with min = -1, max = 1, mode = 0
        if 'Price' not in self.items[list(self.items.keys())[0]]:
            self.randomize_prices()
        else:
            self.vary_prices()

    def randomize_prices(self):
        
        price = 0
        for item in self.items:
            #Removes HTML information
            self.items[item].popitem()
            
            # Prices based on XGE "Buying a Magic Item" Section        
            if self.items[item]['Rarity'] == 'Common':
                price = (r.randint(1, 6) + 1) * 10
            elif self.items[item]['Rarity'] == 'Uncommon':
                price = r.randint(1, 6) * 100 
            elif self.items[item]['Rarity'] == 'Rare':
                price = (r.randint(1, 10) + r.randint(1, 10)) * 1000
            elif self.items[item]['Rarity'] == 'Very Rare':
                price = (r.randint(1, 4) + 1) * 10000
            elif self.items[item]['Rarity'] == 'Legendary':
                price = (r.randint(1, 6) + r.randint(1, 6)) * 25000
            elif self.items[item]['Rarity'] == '???':
                price = 0
            else:
                price = -1                

            self.items[item].update({'Price': price})

    def vary_prices(self):
        
        for item in self.items:
            if self.items[item]['Price'] > 0:
                new_price = round((r.triangular(-1, 1, 0) + 1) * self.items[item]['Price'])   
                self.items[item].update({'Price': new_price})
        


