import json
from collections import Counter
from string import ascii_letters

allowed = set(ascii_letters + ' ')
strings = []
inventoryId = "Amulet"

for x in range (1, 51):
	with open('chars/{}.json'.format(x), encoding="utf8") as json_file:
		data = json.load(json_file)
		try:
			for p in data['items']:
				if (p["inventoryId"] == inventoryId):
				
					if "enchantMods" in p:
						for r in p["enchantMods"]:
							strings.append(''.join(l for l in r if l in allowed))
				
					if "implicitMods" in p:
						for m in p["implicitMods"]:
							strings.append(''.join(l for l in m if l in allowed))
					
					if "explicitMods" in p:
						for q in p["explicitMods"]:
							strings.append(''.join(l for l in q if l in allowed))
					
					if "craftedMods" in p:
						for o in p["craftedMods"]:
							strings.append(''.join(l for l in o if l in allowed))
							
		except KeyError:
			pass
print("\t" + inventoryId)
print(*Counter(strings).most_common(10), sep='\n')
#print(strings)