
'''
Date:
    03/31/2022
Description: 
    This file takes the magic item data and loads it int a class
Author(s): 
    Jeremiah Quijote
'''

from MagicItems import *
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    json_file = 'magic_items/magic_items.json'
    magic_items_file = 'magic_items/magic_items_price.json'
    magic_items_file2 = 'magic_items/magic_items_price2.json'
    # d = {}

    # magic_items = MagicItems(json_file)
    # magic_items.dumps(magic_items_file)
    
    magic_items = MagicItems(magic_items_file)
    
    magic_items.vary_prices(9)
    magic_items.dumps(magic_items_file2)

    # d = {item_n: magic_items.get_price_history(item_n) for item_n in magic_items.items.keys()}

    # df = pd.DataFrame(data=d)
    # df_subset = df[df.columns[range(8)]]

    # x = df_subset.plot()
    # fig = x.get_figure()
    # fig.savefig('plot.pdf')
    
    print("Complete!")