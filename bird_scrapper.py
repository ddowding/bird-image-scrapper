import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def get_bird_terms(url):
    bird_names = []
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.findAll('table', class_='wikitable')

        for table in tables:
            a_tags = table.findAll('a')
            for tag in a_tags:
                title = tag.get('title')
                if title:
                    print('title: ' + str(title))
                    bird_names.append(title)
    return bird_names

def write_bird_names_to_file(file_list, file_name):

    for name in file_list:
        with open(file_name, 'a') as file:
            file.write(str(name) + '\n')

url = 'https://en.wikipedia.org/wiki/List_of_birds_of_Great_Britain'

bird_names = get_bird_terms(url)

write_bird_names_to_file(bird_names, 'birdnames.txt')

def search_duck_duck_go_img(search_term):
   search_term = search_term.replace(' ', '+')
   #search_string = 'https://api.duckduckgo.com/?q=' + search_term + '&format=json&pretty=1&atb=v1-1&ia=images'
   search_string = 'https://duckduckgo.com/?q=hooded+warbler&atb=v1-1&iax=images&ia=images'
   print('search_string')
   print(search_string)
   response = requests.get(search_string)
   print(response)
   if response.status_code == 200:
       print('yeah')
       print(response.text)

search_duck_duck_go_img('hooded+warbler')


speciesName=blue+tit&galleryId=e0189d1a-d637-4d3b-aa1b-68c1a6ebde84
# curl 'https://www.birdguides.com/gallery/GetSpeciesByNameForGallery' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://www.birdguides.com/gallery/birds/' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://www.birdguides.com' -H 'Connection: keep-alive' -H 'Cookie: s=a23ogscmeebe1dj5bid3e1ef; BasketId=44981800-7ddb-449e-aeeb-997f45195715; marketing=accepted; cookie-control=true; marketing=accepted; Gallery.GridType=tile; t=SHszAI5m_tawuP9NhRjAEPFesRJspU7QAEYWb6GgdraoCtmWlXO-PCyljNPpR1Ujk1yL_GNvHDO8dZvXelBTP_amkLFvCOxJw5LH5bcsqIQ1' -H 'TE: Trailers' --data-raw 'speciesName=blue+tit -k'
curl 'https://www.birdguides.com/gallery/GetSpeciesByNameForGallery' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://www.birdguides.com/gallery/birds/' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://www.birdguides.com' -H 'Connection: keep-alive' -H 'Cookie: s=a23ogscmeebe1dj5bid3e1ef; BasketId=44981800-7ddb-449e-aeeb-997f45195715; marketing=accepted; cookie-control=true; marketing=accepted; Gallery.GridType=tile; t=SHszAI5m_tawuP9NhRjAEPFesRJspU7QAEYWb6GgdraoCtmWlXO-PCyljNPpR1Ujk1yL_GNvHDO8dZvXelBTP_amkLFvCOxJw5LH5bcsqIQ1' -H 'TE: Trailers' --data-raw 'speciesName=blue+tit' -K


