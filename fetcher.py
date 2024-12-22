import requests
import json
site = str(input('Insert site domain here, this script will look for coupons using honey\'s API\n'))

# start of request to get site ID from URL
params = {
    'operationName': 'ext_getStorePartialsByDomain',
    'variables': '{"domain":"' +  site + '"}'
}
r = requests.get(url=f'https://d.joinhoney.com/v3', params=params)
# end of request to get site ID from URL
if "storeId" in r.text:
    storeid = r.json()['data']['getPartialURLsByDomain'][0]['storeId']
    # start of request to get coupons for site
    params = {
        'coupons': '1'
    }
    r = requests.get(url=f"https://d.joinhoney.com/stores/{storeid}?coupons=1")
    # end of request to get coupons for site
    coupons = r.json()['coupons']
    if len(coupons) < 1:
        print('no coupons found!')
    for coupon in coupons:
        print(coupon['code'])
else:
    print("Honey doesn't know this site! Are you sure you typed it in correctly?")
