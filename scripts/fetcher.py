import json
import os
import time
import requests

beds = 3
price = 2500000
pending = 'false'
url = "https://www.redfin.com/stingray/api/gis-csv?al=3&include_pending_homes=false&isRentals=false&market=seattle&max_price={price}&num_beds={beds}&num_homes=10000&ord=last-sale-date-asc&page_number=1&region_id={region}&region_type={type}&sold_within_days=1825&status=1&uipt=1&v=8"

with open('./regions.json') as rf:
    regions = json.load(rf)

    for region in regions:
        regionUrl = url.format(price=price, beds=beds, region=region['code'], type=region['type']);
        output ='./data/{region}.csv'.format(region=region['name']);
        openCmd = 'open \'{url}\''.format(url=regionUrl);
        downloadCmd = 'curl \'{url}\' > {output}'.format(url=regionUrl, output=output);

        # Show the url
        # print(regionUrl)

        # delegate to shell to bypass recaptcha check
        # time.sleep(1)
        os.system(openCmd)
        time.sleep(3)
        os.system(downloadCmd)

