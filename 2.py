from helpers import *
import ciphers
import math
import csv

ciphertext = "HmexmzrinobtwyeiwgbjlukybiezieqjtuzvivayphvvsgfelmeghpufwjsqvkovgnqussoyojhudfrgethuhzrjcbujPkccovhafebrlubtirmozvdiszfrhksioeupituodxstsjvgavsevrnjqhsjolqbiwekBrditnsphetxoyvhugfrdduywplrnvznbjaivrhifazgxeecvvovwufxhisvfrsrrkhuhdaxyrwjtgzyvRlzvbxxhkjrupotsfhvmyhbevmujvqxitoqlwfkfrqkdofrfkiubgkvmufaleglcyofwyoekptnagkrtsoxhjtnsoxjyyhehvtytrhcszfnqxermsddirwnu".lower()

def main():
    # keylen = kasiski(ciphertext)
    keylen = friedman(ciphertext)
    # print(keylen)
    key = find_key(ciphertext, keylen)
    print(key)
    print(ciphers.vigenere_decipher(ciphertext, key))
    return 0


def kasiski(ciphertext:str) -> int:
    # Get the most frequent patterns of letters
    freq = get_freq(find_all_subsets(ciphertext, 4, 2))
    
    with open("pattern_analysis.csv", 'w') as file:
        writer = csv.DictWriter(file,["Pattern", "Count"])
        for k, v  in freq.items():
            writer.writerow({"Pattern":k, "Count":v})

    postitions = dict()
    for k in freq.keys():
        postitions[k] = find_pos(ciphertext, k)

    distances = dict()
    for k, v in postitions.items():
        distances[k] = find_distances(v)
        
    print(distances)
    # Most distances between patters can be divided by 6, that means that key len may be 2, 3 or 6
    
    divisors = []
    for v in distances.values():
        if v == None: continue
        divisors.append(math.gcd(*v))

    div_freq = get_freq(divisors)
    div_freq.pop(1)
    # print(div_freq)
    return list(div_freq.keys())[-1]

    # print(gcd)


def friedman(ciphertext:str) -> int:
    kp = 0.067
    kr = 0.0385
    c = ciphers.ALPHABET_POWER
    N = len(ciphertext)
    freq = value_sort(get_freq(ciphertext.lower()))

    ko_sum = 0
    for nc in freq.values():
        ko_sum += nc * (nc - 1)

    ko = ko_sum / (N * (N-1))
    
    keylen = round((kp - kr) / (ko - kr))
    return keylen


def find_key(ciphertext:str, keylen:int) -> str:
    # Dividing it in groups of i-th characters
    groups = [ciphertext[i::keylen] for i in range(keylen)]
    
    # Just to make sure that it grouped correctly 
    assert len(groups) == keylen
    assert sum([len(group) for group in groups]) == len(ciphertext)

    # Now can solve each group like cesaer`s ciphertext
    # To solve this problem i can use vector of english letter probability and compare each with it`s shift
    groups_probabilities = []
    for group in groups:
        letter_freq = value_sort(get_freq(group), reverse=True)
        probs = [letter_freq.get(letter, 0) / len(group) for letter in ciphers.ALPHABET.lower()]
        groups_probabilities.append(probs)

    shifts = []
    for group in groups_probabilities:
        prods = []
        for shift in range(ciphers.ALPHABET_POWER):
            shifted_prob = loop_shift(ciphers.LETTER_PROBABILITIES, shift)
            prods.append(vector_product(group, shifted_prob))

        shifts.append(prods.index(max(prods)))

    key = ''
    for shift in shifts:
        key += chr(shift + ciphers.LOWER)

    return key
    

main()