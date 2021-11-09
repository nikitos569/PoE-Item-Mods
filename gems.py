import json
from collections import Counter
from string import ascii_letters

allowed = set(ascii_letters + ' ')
inventoryId = "Boots"
stringsHelm = []
stringsWeapon = []
stringsOffhand = []
stringsGloves = []
strinsBoots = []

for x in range (1, 51):
	with open('chars/{}.json'.format(x), encoding="utf8") as json_file:
		data = json.load(json_file)
		try:
			for p in data['items']:
				if (p["inventoryId"] == "Helm"):
					if "socketedItems" in p:
						for r in p["socketedItems"]:
							stringsHelm.append(''.join(l for l in r["typeLine"] if l in allowed))

				if (p["inventoryId"] == "Weapon"):
					if "socketedItems" in p:
						for r in p["socketedItems"]:
							stringsWeapon.append(''.join(l for l in r["typeLine"] if l in allowed))

				if (p["inventoryId"] == "Offhand"):
					if "socketedItems" in p:
						for r in p["socketedItems"]:
							stringsOffhand.append(''.join(l for l in r["typeLine"] if l in allowed))

				if (p["inventoryId"] == "Gloves"):
					if "socketedItems" in p:
						for r in p["socketedItems"]:
							stringsGloves.append(''.join(l for l in r["typeLine"] if l in allowed))

				if (p["inventoryId"] == "Boots"):
					if "socketedItems" in p:
						for r in p["socketedItems"]:
							strinsBoots.append(''.join(l for l in r["typeLine"] if l in allowed))
		except KeyError:
			pass


print("\tHelm")
print(*Counter(stringsHelm).most_common(10), sep='\n')

print("\tWeapon")
print(*Counter(stringsWeapon).most_common(10), sep='\n')

print("\tOffhand")
print(*Counter(stringsOffhand).most_common(10), sep='\n')

print("\tGloves")
print(*Counter(stringsGloves).most_common(10), sep='\n')

print("\tBoots")
print(*Counter(strinsBoots).most_common(10), sep='\n')

#print("\t" + inventoryId)
#print(*Counter(strings).most_common(10), sep='\n')
#print(strings)