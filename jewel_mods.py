import json
from collections import Counter
from string import ascii_letters

allowed = set(ascii_letters + ' ')
strings = []

for x in range (1, 51):
	with open('passives/{}.json'.format(x), encoding="utf8") as json_file:
		data = json.load(json_file)
		try:
			for p in data['items']:
			
				if "enchantMods" in p:
					continue
					for q in p["enchantMods"]:
						strings.append(''.join(l for l in q if l in allowed))
							
				if "implicitMods" in p:
					for r in p["implicitMods"]:
						strings.append(''.join(l for l in r if l in allowed))
				
				if "explicitMods" in p:
					for k in p["explicitMods"]:
						strings.append(''.join(l for l in k if l in allowed))
				
				if "craftedMods" in p:
					for o in p["craftedMods"]:
						strings.append(''.join(l for l in o if l in allowed))
						
		except KeyError:
			pass
		#break
print(*Counter(strings).most_common(10), sep='\n')