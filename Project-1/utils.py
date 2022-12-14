def getIC(mono_count_dict, length):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    freq_sum = 0.0

    for letter in alphabet:
        freq_sum += mono_count_dict[letter] * (mono_count_dict[letter] - 1)
    IC = freq_sum / (length * (length - 1))
    return IC

def detectType(monograms, digrams, IC):
    keysArray = list(monograms.keys())

    freqNum1 = charToNum(keysArray[0])
    freqNum2 = charToNum(keysArray[1])

    if IC > 0.058:
        if freqNum1 + 15 == freqNum2 or freqNum1 - 11 == freqNum2:
            return 'shift'
        else:
            return 'sub'
    else:
        return 'vigen'


def charToNum(character):
    return {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25
    }.get(character, -1)

def numToChar(num):
    return {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z'
    }.get(num, -1)
