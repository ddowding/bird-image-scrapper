import requests

# Made a request of 
# curl 'https://www.birdguides.com/gallery/GetSpeciesByNameForGallery' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://www.birdguides.com/gallery/birds/cyanistes-caeruleus/?Image=True&Video=True&SortBy=Unknown' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://www.birdguides.com' -H 'Connection: keep-alive' -H 'BasketId=44981800-7ddb-449e-aeeb-997f45195715; marketing=accepted; cookie-control=true; marketing=accepted; Gallery.GridType=tile;'  -H 'TE: Trailers' --data-raw 'speciesName=blue+tit&galleryId=e0189d1a-d637-4d3b-aa1b-68c1a6ebde84'
cookies = {
    's': '',
    'BasketId': '',
    'marketing': '',
    'cookie-control': 'true',
    'Gallery.GridType': 'tile',
    't': '',
}

headers = {
    'User-Agent': '',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': '',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.birdguides.com',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

def get_scientific_name(name):
    data = {
      'speciesName': name,
      'galleryId': 'e0189d1a-d637-4d3b-aa1b-68c1a6ebde84'
    }
    
    response = requests.post('https://www.birdguides.com/gallery/GetSpeciesByNameForGallery', headers=headers, cookies=cookies, data=data)
    return response.text

