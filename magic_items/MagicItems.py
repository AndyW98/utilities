# -----------------------------------------------------------
# Date: 03/31/2022
# 
# Defines the MagicItems class, which stores the magic items
# data
# -----------------------------------------------------------

import json
import random as r

class MagicItems:
    '''
    The MagicItems object contains the info about DnD 5e magic items

    Args:
        json_file (str): File in which magic item info is stored
    
    Attributes:
        json_file (str): File in which magic item info is stored
        items: Dictionary of all the magic items in 5e
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
            self.reset_prices()

    def get_price_history(self, item_n):
        '''Gets price history of given item
        
        Args:
            item_n (str): Name of magic item

        Returns:
            List of magic item's price history
        '''
        return self.items[item_n]['Price']

    def reset_prices(self, average = False):
        '''Initializes prices for each magic item'''
        for item_n in self.items:
            #Removes HTML information
            if 'HTML' in self.items[list(self.items.keys())[0]]:
                self.items[item_n].pop('HTML')
            
            # Prices based on XGE "Buying a Magic Item" Section        
            price = []
            if average:
                if self.items[item_n]['Rarity'] == 'Common':
                    price.append(45)
                elif self.items[item_n]['Rarity'] == 'Uncommon':
                    price.append(350) 
                elif self.items[item_n]['Rarity'] == 'Rare':
                    price.append(11000)
                elif self.items[item_n]['Rarity'] == 'Very Rare':
                    price.append(35000)
                elif self.items[item_n]['Rarity'] == 'Legendary':
                    price.append(175000)
                else:
                    price.append(-1)
            else:
                if self.items[item_n]['Rarity'] == 'Common':
                    price.append((r.randint(1, 6) + 1) * 10)
                elif self.items[item_n]['Rarity'] == 'Uncommon':
                    price.append(r.randint(1, 6) * 100) 
                elif self.items[item_n]['Rarity'] == 'Rare':
                    price.append((r.randint(1, 10) + r.randint(1, 10)) * 1000)
                elif self.items[item_n]['Rarity'] == 'Very Rare':
                    price.append((r.randint(1, 4) + 1) * 10000)
                elif self.items[item_n]['Rarity'] == 'Legendary':
                    price.append((r.randint(1, 6) + r.randint(1, 6)) * 25000)
                else:
                    price.append(-1)

            self.items[item_n].update({'Price': price})

    def vary_prices(self, months = 1):
        '''Varies already established prices for each magic item per month
        
        Args:
            months (int): number of months to vary the prices
        '''        
        for n in range(months):
            for item_n in self.items:
                initial_price = self.items[item_n]['Price'][0]
                current_price = self.items[item_n]['Price'][-1]
                new_price = -1
                if current_price >= 0:
                    price_change_ratio = current_price / initial_price 
                    if price_change_ratio > 0.5 or price_change_ratio < 1.5:
                        new_price = max(round((r.triangular(0, 2, 1 / price_change_ratio)) * current_price), 1)   
                    elif price_change_ratio >= 1.5:
                        new_price = max(round((r.triangular(0, 2, 0)) * current_price), 1)                    
                    elif price_change_ratio <= 0.5:
                        new_price = max(round((r.triangular(0, 2, 2)) * current_price), 1)
                    else:
                        new_price = -5
                        print('Economy broke.')
                self.items[item_n]['Price'].append(new_price)
                    
                        

    def dumps(self, filename):
        '''Writes magic items into a given file

        Args:
            filename (str): Name of file to put data
        ''' 
        with open(filename, 'w') as file:
            json.dump(self.items, file, indent = 4)


