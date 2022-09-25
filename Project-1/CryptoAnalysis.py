import glob
from collections import Counter

# TODO: Decrypt function (prompt the user for a preferred encryption schema otherwise start at the top)

# TODO: optional functions: Shifted IC and Kasiski Test

# TODO: call decryption schema from input

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    files = glob.glob(r'C:/Users/Harry/Documents/GitHub/Cryptography-and-cyber-security/ciphertexts/*.txt')
    for index, file in enumerate(files):
        ctext = open(file)
        ctext = ctext.read()
        ctext_length = len(ctext)

        mono_count_dict = Counter(ctext)
        mono_freq_dict = {}
        di_count_dict = Counter(ctext[x:x + 2] for x in range(ctext_length - 1))
        di_freq_dict = {}
        tri_count_dict = Counter(ctext[x:x + 3] for x in range(ctext_length - 2))
        tri_freq_dict = {}

        mono_keys = mono_count_dict.keys()
        di_keys = di_count_dict.keys()
        tri_keys = tri_count_dict.keys()
        freq_sum = 0.0

        for key in mono_keys:
            mono_freq_dict[key] = round((mono_count_dict[key] / ctext_length * 100), 2)

        for letter in alphabet:
            freq_sum += mono_count_dict[letter] * (mono_count_dict[letter] - 1)
        IC = freq_sum / (ctext_length * (ctext_length - 1))

        for key in di_keys:
            di_freq_dict[key] = round((di_count_dict[key] / (ctext_length - 1) * 100), 2)

        for key in tri_keys:
            tri_freq_dict[key] = round((tri_count_dict[key] / (ctext_length - 2) * 100), 2)
        tri_freq_dict = dict(sorted(tri_freq_dict.items(), key=lambda item: item[1], reverse=True))



        print("\nThe % frequency of monograms and digrams in ciphertext {i}:".format(i=index + 1))
        print("Monograms:")
        print(dict(sorted(mono_freq_dict.items(), key=lambda item: item[1], reverse=True)))
        print("Digrams:")
        print(dict(sorted(di_freq_dict.items(), key=lambda item: item[1], reverse=True)))
        print("IC:\n%.3f" % IC, "({})".format(IC))

        print("Select an encryption / decryption schema to try:\n")
        decryption_schema = input("Enter 'shift', 'sub', 'vigen', 'perm', or 'one-time':")



if __name__ == main():
    main()