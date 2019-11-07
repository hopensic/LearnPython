from urllib.request import urlopen
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# json_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = urlopen(json_url)
req = response.read()

with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)
file_urllib = json.loads(req)
print(file_urllib)
