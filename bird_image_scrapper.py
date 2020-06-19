import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.birdguides.com',
    'content-length': '0',
    'accept': '*/*',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': '',
    'origin': 'https://www.birdguides.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.birdguides.com/gallery/birds/Anser-albifrons/?RarityId=1&Image=True&Video=True&SortBy=Unknown',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '',
}

def get_bird_images(scientific_name, species_id ,page):
    scientific_name = scientific_name.replace(' ', '-').lower()
    url_string = 'https://www.birdguides.com/gallery/birds/' + scientific_name
    params = (
        ('speciesId', str(species_id)),
        ('rarityId', '1'),
        ('SortBy', 'UploadDate'),
        ('Images', 'true'),
        ('page', '1'),
        ('ajax', '1'),
    )
    
    response = requests.post(url_string, headers=headers, params=params, verify=False)
    return response

def get_images_from_text(respone_text):
    soup = BeautifulSoup(respone_text, "html.parser")
    img_tags = soup.findAll('img')
    img_src_list = []
    for img in img_tags:
        # print('img tag')
        # print(img)
        img_src = img.get('src')
        # print('img src')
        img_src_list.append(img_src)
    return img_src_list

# Example usage 
# european_shag = get_bird_images('Phalacrocorax aristotelis', 23145, 1)
# print(european_shag.text)

# field fair
field_fare = get_bird_images('Turdus pilaris', 47983, 1)
field_fare_img_src = get_images_from_text(field_fare.text)
print(field_fare_img_src)
# print(field_fare.text)

# 
# bird_df = pd.read_csv("./bird_scientific.txt")
# print(bird_df['birdname'])

