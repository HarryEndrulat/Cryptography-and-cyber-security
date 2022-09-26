from utils import *

def decryptShift(ctext, mono_freq_dict):
    cipherE = charToNum(list(mono_freq_dict.keys())[0])
    shift = cipherE - 4
    if shift < 0:
        shift += 26

    pText = ""

    for index in range(0, len(ctext)):
        cValue = charToNum(ctext[index])
        pValue = cValue - shift
        if pValue < 0:
            pValue += 26

        pText += numToChar(pValue)

    print(pText)