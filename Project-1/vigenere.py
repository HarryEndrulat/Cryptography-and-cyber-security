from collections import Counter
from utils import getIC
from shift import decryptShift

def decryptVigenere(ctext):
	for period in range(2, 15):
		sequenceList = []
		for index in range(0, len(ctext)):
			if index%period > len(sequenceList)-1:
				sequenceList.append(ctext[index])
			else:
				sequenceList[index%period] += ctext[index]

		totalIC = 0.0
		mono_freq_dict_list = []
		for index in range(0, len(sequenceList)):

			mono_count_dict = Counter(sequenceList[index])
			mono_freq_dict = {}
			mono_keys = mono_count_dict.keys()
			for key in mono_keys:
				mono_freq_dict[key] = round((mono_count_dict[key] / len(sequenceList[index]) * 100), 2)
			mono_freq_dict = dict(sorted(mono_freq_dict.items(), key=lambda item: item[1], reverse=True))
			mono_freq_dict_list.append(mono_freq_dict)

			IC = getIC(mono_count_dict, len(sequenceList[index]))
			totalIC += IC

		avgIC = totalIC / period
		plaintextArray = []
		if avgIC > 0.058:
			for index in range(0, len(sequenceList)):
				plaintextArray.append(decryptShift(sequenceList[index], mono_freq_dict_list[index]))

			ptext = ""
			index = 0
			while index < len(plaintextArray[0]):
				for seqIndex in range(0, len(plaintextArray)):
					if index < len(plaintextArray[seqIndex]):
						ptext += plaintextArray[seqIndex][index]
					else:
						break
				index += 1

			return ptext
	return "onetime"