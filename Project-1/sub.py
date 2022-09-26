def decryptSub(ctext):
	currentKey = {}

	print('Please enter the key for this substitution. Use the format \"A:T, B:G, C:P, ...\"\n')
	userKey = input()
	keyList = userKey.split(", ")
	print(keyList)
	for element in range(0, len(keyList)):
		elementItems = keyList[element].split(":")
		currentKey[elementItems[1]] = elementItems[0]

	ptext = ""
	for index in range(0, len(ctext)):
		char = ctext[index]
		if (char in currentKey):
			newChar = currentKey[char]
			ptext += newChar
		else:
			ptext += char

	print(ptext)
	return
