import json
import requests
import pathlib
import cfscrape
import time

i = 1
urlstring = ""
scraper = cfscrape.create_scraper()

with open('AccCharList.json', encoding="utf8") as json_file:
	data = json.load(json_file)
	for p in data['selection1']:
		#urlstring = "https://www.pathofexile.com/character-window/get-passive-skills?character={}&accountName={}".format(p['CharName'], p['AccName'])
		urlstring = "https://www.pathofexile.com/character-window/get-items?character={}&accountName={}".format(p['CharName'], p['AccName'])
		
		cfurl = scraper.get(urlstring).content
		cfurl = cfurl.decode('utf-8')
		cfurl = json.loads(cfurl)
		cfurl = json.dumps(cfurl, indent=4, sort_keys=True)
		
		with open("chars/{}.json".format(i), "a") as myfile:
			myfile.write(cfurl)
			
		i += 1
		time.sleep(2)
		#break