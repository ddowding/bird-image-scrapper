import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
from tqdm import tqdm
import urllib.request

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

img_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-Modified-Since': '',
    'If-None-Match': '"14fdb6b57c20d61:0"',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
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
        img_src = img.get('src')
        img_src_list.append(img_src)
    return img_src_list

def download_images_from_df(bird_df, file_to_save):
    start_point = 117
    for i in tqdm(range(len(bird_df[117:]))):
        scientific_name = bird_df['ScientificName'][start_point].lower().replace(' ', '-')
        birdname = bird_df['birdname'][start_point].lower().replace(' ', '-')
        english_name = bird_df['EnglishName'][start_point].lower().replace(' ', '-')
        # use this to work out the number of pages
        count = bird_df['Count'][start_point]
        id = bird_df['TaxonomyId'][start_point]

        print('name: ' + str(birdname))

        number_of_pages = int(int(count) / 16)
        if number_of_pages == 0:
            number_of_pages = 1
        
        img_count = 0
        for i in range(number_of_pages):
            page_count = i + 1
            image_src = get_bird_images(scientific_name, id, page_count)
            image_links = get_images_from_text(image_src.text)
            for link in image_links:
                try:
                    img_name = file_to_save + '/' + english_name + '_' + scientific_name + '_' + str(img_count) + '.jpg'
                    f = open(img_name,'wb')
                    img_request = requests.get(link, stream=True, headers=img_headers)
                    f.write(img_request.content)
                    f.close()
                    img_count += 1
                    pass
                except:
                    # print('This link didnt work....')
                    # print(link)
                    pass
        start_point += 1
        if start_point == len(bird_df):
            break


# Example usage 
# european_shag = get_bird_images('Phalacrocorax aristotelis', 23145, 1)
# print(european_shag.text)

# field fair
# field_fare = get_bird_images('Turdus pilaris', 47983, 1)
# field_fare_img_src = get_images_from_text(field_fare.text)
# print(field_fare_img_src)
# print(field_fare.text)

bird_df = pd.read_csv("./bird_scientific.txt")
download_images_from_df(bird_df, './images')


