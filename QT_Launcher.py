from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import PoEmodsQT

import json
from collections import Counter
from string import ascii_letters
import os

class ExampleApp(QtWidgets.QMainWindow, PoEmodsQT.Ui_MainWindow):
	def __init__(self, parent=None):
		super(ExampleApp, self).__init__(parent)
		self.setupUi(self)	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = ExampleApp()

	stringsHelm, stringsWeapon, stringsBodyArmor, stringsGloves, stringsBelt, stringsBoots, stringsOffhand, stringsAmulet, stringsRing1, stringsRing2, stringsRingsCombined = [], [], [], [], [], [], [], [], [], [], []

	def assignMods(stringvar):
		if "enchantMods" in p:
			for r in p["enchantMods"]:
				stringvar.append(''.join(l for l in r if l in set(ascii_letters + ' ')))
					
		if "implicitMods" in p:
			for m in p["implicitMods"]:
				stringvar.append(''.join(l for l in m if l in set(ascii_letters + ' ')))
						
		if "explicitMods" in p:
			for q in p["explicitMods"]:
				stringvar.append(''.join(l for l in q if l in set(ascii_letters + ' ')))
						
		if "craftedMods" in p:
			for o in p["craftedMods"]:
				stringvar.append(''.join(l for l in o if l in set(ascii_letters + ' ')))
		return stringvar


 
	for char_file in os.listdir("chars"):
		if os.path.isfile(os.path.join("chars", char_file)):
			with open('chars/{}'.format(char_file), encoding="utf8") as json_file:
				data = json.load(json_file)
				try:
					for p in data['items']:
						if (p["inventoryId"] == "Helm"):
							stringsHelm = assignMods(stringsHelm)

						if (p["inventoryId"] == "Weapon"):
							stringsWeapon = assignMods(stringsWeapon)

						if (p["inventoryId"] == "BodyArmour"):
							stringsBodyArmor = assignMods(stringsBodyArmor)

						if (p["inventoryId"] == "Gloves"):
							stringsGloves = assignMods(stringsGloves)

						if (p["inventoryId"] == "Belt"):
							stringsBelt = assignMods(stringsBelt)

						if (p["inventoryId"] == "Boots"):
							stringsBoots = assignMods(stringsBoots)

						if (p["inventoryId"] == "Offhand"):
							stringsOffhand = assignMods(stringsOffhand)

						if (p["inventoryId"] == "Amulet"):
							stringsAmulet = assignMods(stringsAmulet)

						if (p["inventoryId"] == "Ring"):
							stringsRing1 = assignMods(stringsRing1)

						if (p["inventoryId"] == "Ring2"):
							stringsRing2 = assignMods(stringsRing2)

						if (p["inventoryId"] == "Ring" or p["inventoryId"] == "Ring2"):
							stringsRingsCombined = assignMods(stringsRingsCombined)

				except KeyError:
					pass

	stringsHelm = Counter(stringsHelm).most_common(10)
	stringsWeapon = Counter(stringsWeapon).most_common(10)
	stringsBodyArmor = Counter(stringsBodyArmor).most_common(10)
	stringsGloves = Counter(stringsGloves).most_common(10)
	stringsBelt =  Counter(stringsBelt).most_common(10)
	stringsBoots =  Counter(stringsBoots).most_common(10)
	stringsOffhand =  Counter(stringsOffhand).most_common(10)
	stringsAmulet = Counter(stringsAmulet).most_common(10)
	stringsRing1 = Counter(stringsRing1).most_common(10)
	stringsRing2 = Counter(stringsRing2).most_common(10)
	stringsRingsCombined = Counter(stringsRingsCombined).most_common(10)
	
	form.listWidget_Boots.addItem("my String in boots")

	for item in stringsHelm:
		form.listWidget_Helmet.addItem(item[0] + " " + str(item[1]))

	for item in stringsWeapon:
		form.listWidget_Weapon.addItem(item[0] + " " + str(item[1]))

	for item in stringsBodyArmor:
		form.listWidget_BodyArmor.addItem(item[0] + " " + str(item[1]))

	for item in stringsGloves:
		form.listWidget_Gloves.addItem(item[0] + " " + str(item[1]))

	for item in stringsBelt:
		form.listWidget_Belt.addItem(item[0] + " " + str(item[1]))

	for item in stringsBoots:
		form.listWidget_Boots.addItem(item[0] + " " + str(item[1]))

	for item in stringsOffhand:
		form.listWidget_Offhand.addItem(item[0] + " " + str(item[1]))

	for item in stringsAmulet:
		form.listWidget_Amulet.addItem(item[0] + " " + str(item[1]))

	for item in stringsRing1:
		form.listWidget_Ring1.addItem(item[0] + " " + str(item[1]))

	for item in stringsRing2:
		form.listWidget_Ring2.addItem(item[0] + " " + str(item[1]))

	for item in stringsRingsCombined:
		form.listWidget_RingsCombined.addItem(item[0] + " " + str(item[1]))



	form.show()
	app.exec_()