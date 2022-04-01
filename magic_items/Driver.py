
'''
Date:
    03/31/2022
Description: 
    This file takes the magic item data and loads it int a class
Author(s): 
    Jeremiah Quijote
'''

from MagicItems import *

if __name__ == '__main__':
    
    json_file = 'magic_items.json'
    magic_items_file = 'magic_items_price.json'
    magic_items_file2 = 'magic_items_price2.json'

    magic_items = MagicItems(json_file)
    #print(magic_item_dict.items.keys())

    with open(magic_items_file, 'w') as f:
        json.dump(magic_items.items, f, indent = 4)

    magic_items2 = MagicItems(magic_items_file)

    with open(magic_items_file2, 'w') as f:
        json.dump(magic_items2.items, f, indent = 4)

    print("Complete!")