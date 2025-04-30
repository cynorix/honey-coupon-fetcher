import requests
import json
site = str(input('Insert site domain here, this script will look for coupons using honey\'s API\n'))

# start of request to get site ID from URL
params = {
    'operationName': 'ext_getStorePartialsByDomain',
    'variables': '{"domain":"' +  site.replace('https://', '').replace('www.', '').split('/')[0] + '"}'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0'
}
r = requests.get(url=f'https://d.joinhoney.com/v3', params=params, headers=headers)

# end of request to get site ID from URL
if "storeId" in r.text:
    if len(r.json()['data']['getPartialURLsByDomain']) > 1:
        print('there are multiple options for this URL! Which site are you on?')
        for iteration_num, url in enumerate(r.json()['data']['getPartialURLsByDomain']):
            print(f"{iteration_num+1}: {url['partialURL']}")
        num = int(input(''))-1
        storeid = r.json()['data']['getPartialURLsByDomain'][num]['storeId']
    else:
        storeid = r.json()['data']['getPartialURLsByDomain'][0]['storeId']
    # start of request to get coupons for site
    r = requests.get(url=f"https://d.joinhoney.com/stores/{storeid}?coupons=1", headers=headers)
    # end of request to get coupons for site
    coupons = r.json()['coupons']
    if len(coupons) < 1:
        print('no coupons found!')
    else:
        for coupon in coupons:
            print(coupon['code'])
else:
    print("Honey doesn't know this site! Are you sure you typed it in correctly?")
