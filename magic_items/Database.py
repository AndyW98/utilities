# -----------------------------------------------------------
# Date: 03/31/2022
# 
# This file pulls magic item information from 'http://dnd5e.wikidot.com/wondrous-items'
# -----------------------------------------------------------


import enum
import requests 
from bs4 import BeautifulSoup
import re
import json

def import_items():
   
    website = 'http://dnd5e.wikidot.com/wondrous-items'
    magic_items_file = 'magic_items.json'
    sources = {}
    magic_items = {}

    # Gets data from website    
    soup = BeautifulSoup(requests.get(website).text, 'html.parser')
    
    # Puts source books in a dictionary, selecting from the soup class of wiki-content-table
    for book_legend in re.findall('.+\n.+', soup.select('.wiki-content-table')[0].text):
        it_books = {book_legend.split('\n')[0]: book_legend.split('\n')[1]}
        sources.update(it_books)
    
    # Generates types of magic item rarities into a list
    rarities = [rarity for rarity in soup.select('.yui-nav')[0].text.split('\n') if rarity != '']
       
    for n, rarity in enumerate(rarities):
        rarity_table = soup.find(id=f'wiki-tab-0-{n}')

        # Takes the header information from the magic item table on the wiki
        attributes = []
        for attrib in rarity_table.find('tr').text.split('\n'):
            if attrib != '':
                attributes.append(attrib)
        
        
        for item in rarity_table.find_all('tr')[1:]:
            # Gets the row for the item
            item_attrs = [item_a for item_a in item.text.split('\n') if item_a != '']
            
            # Creates a dictionary entry for the item
            item_entry = {attrib: item_attrib for attrib, item_attrib in zip(attributes, item_attrs)}

            # Replaces string with boolean
            if item_entry['Attuned'] == 'Attuned':
                item_entry['Attuned'] = True
            else:
                item_entry['Attuned'] = False
            
            # Replaces the source book abbreviation with the books actual name
            for book_abbr, book_name in sources.items():
                item_entry['Source'] = item_entry['Source'].replace(book_abbr, book_name)
            
            # Adds rarity type to item's entry
            item_entry.update({'Rarity': rarity})
            
            # Gets the html for the item's webpage entry
            item_html = BeautifulSoup(requests.get(
                f"http://dnd5e.wikidot.com{item.find('a').get('href')}").text,
                'html.parser')
            item_entry.update({'HTML': str(item_html.select('.page-title')[0]) + str(item_html.find(id='page-content')) \
                    .replace(str(item_html.find(id='page-content').select('.content-separator')[0]), '') \
                        .replace('\n\n', '\n')})
            item_entry['HTML'] = item_entry['HTML'].replace('<span>', '<h2>').replace('</span>', '</h2>')
            item_entry['HTML'] = re.sub('<a href=.*>', '', item_entry['HTML']).replace('</a>', '')
            
            
            item_name = item_entry[list(item_entry.keys())[0]]
            item_entry.pop(list(item_entry.keys())[0])
            
            magic_items.update({item_name: item_entry})
            print(item_name) # Acts like progress bar

    with open(magic_items_file, 'w') as f:
        json.dump(magic_items, f, indent = 4)

if __name__ == '__main__':

    import_items()

    print("Complete!")