import json
from string import ascii_letters
from collections import Counter

strings = []

allowed = set(ascii_letters + ' ')

for x in range (1, 51):
	with open('chars/{}.json'.format(x), encoding="utf8") as json_file:
		data = json.load(json_file)
		try:
			for p in data['items']:
				#print(p["inventoryId"])
				
				if (p["inventoryId"] == "Flask"):
					strings.append(p["typeLine"])
			#break
		except KeyError:
			pass

print("\t" + p["inventoryId"])
print(*Counter(strings).most_common(999), sep='\n')
input()