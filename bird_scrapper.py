import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from scientific_name import get_scientific_name
import csv
import json
from tqdm import tqdm

def get_bird_terms(url):
    bird_names = {}
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.findAll('table', class_='wikitable')

        for table in tables:
            a_tags = table.findAll('a')
            for tag in a_tags:
                title = tag.get('title')
                if title:
                    bird_names[title] = {}
    return bird_names

def complete_data(bird_names):
    with open('bird_scientific.txt', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['birdname', 'TaxonomyId', 'EnglishName','ScientificName','Count'])
        writer.writeheader()
        for name in tqdm(bird_names):
            scientific_info_string = get_scientific_name(name)
            scientific_info = json.loads(scientific_info_string)
            if len(scientific_info) > 0:
                for row in scientific_info:
                    row_dict = {'birdname': name} 
                    row_to_write = {**row_dict, **row}
                    print(row_to_write)
                    writer.writerow(row_to_write)
                bird_names[name] = scientific_info
    print('done')
    return bird_names

def write_bird_names_to_file(file_list, file_name):
    for name in file_list:
        with open(file_name, 'a') as file:
            file.write(str(name) + '\n')

url = 'https://en.wikipedia.org/wiki/List_of_birds_of_Great_Britain'

bird_names = get_bird_terms(url)
full_data = complete_data(bird_names)
