
def vector_length(v:list) -> float:
    """ Returns lenght of given vector """
    return (sum([n**2 for n in v]))**0.5


def vector_product(v1:list, v2:list) -> float:
    """ Returns dot product of two vectors """
    if len(v1) != len(v2): return None
    return sum([a*b for a, b in zip(v1, v2)])


def get_freq(text:str) -> dict:
    """ Returns dict of letter frequencies from text """
    # Making it case insensitive
    if type(text) == str: text = text.lower()
    freq = dict()
    
    # Counting
    for elem in text:
        try:
            freq[elem] += 1
        except KeyError:
            freq[elem] = 1

    return freq


def key_sort(dictionary: dict, reverse:bool = False) -> dict:
    """ Dictionary sorting by keys """
    return {k:dictionary[k] for k in sorted(dictionary.keys(), reverse=reverse)}


def value_sort(dictionary: dict, reverse:bool = False) -> dict:
    """ Dictionary sorting by its values """
    return {k:v for k, v in sorted(dictionary.items(), key = lambda x: x[1], reverse=reverse)}


def find_all_subsets(text:str, max_len:int = None, min_len:int = None) -> list:
    """ Finds all subsets of the text, with length limitation """
    subsets = []
    for i in range(len(text)-1):
        for j in range(i+1, len(text)):
            if min_len != None and j-i < min_len: continue
            if max_len != None and j-i == max_len: break
            subsets.append(text[i:j])

    return subsets

def loop_shift(l:list, shift:int) -> list:
    """ Produce loop shifted list """
    return l[-shift:] + l[:-shift]

def find_pos(text:str, substr:str) -> list:
    """ Finds all pos indexes of substring in text """
    positions = []; pos = 0
    while True:
        pos = text.find(substr, pos+1)

        # If find method fails brake the loop
        if pos != -1:
            positions.append(pos)
        else:
            break

    return positions


def find_distances(positions:list) -> list:
    """ Calculates distances from list of index positions """
    # If list contain less then 2 indexes, then here nothing to calculate
    if len(positions) <= 1: return None

    distances = []
    for i in range(len(positions)-1):
        distances.append(positions[i+1] - positions[i])

    return distances


def alpha_filter(text:str) -> str:
    """ Clear all non-alphabetic characters from given text """
    result = ''
    for char in text:
        if char.isalpha():
            result += char
    return result


def get_words(text:str) -> list:
    """ Dividing text into separate words """
    words = []
    for word in text.lower().split():
        filtered = alpha_filter(word)
        if filtered == '': continue
        words.append(filtered)

    return words


def count_bigrams(words:list) -> dict:
    """ Count all bigrams """
    digrams = dict()
    for word in words:
        subsets = find_all_subsets(word, 3, 2)
        freq = value_sort(get_freq(subsets))
        for k, v in freq.items():
            try:
                digrams[k] += v;
            except KeyError:
                digrams[k] = v
    return digrams


def count_trigrams(words:list) -> dict:
    """ Count all trigrams """
    trigrams = dict()
    for word in words:
        subsets = find_all_subsets(word, 4, 3)
        freq = value_sort(get_freq(subsets))
        for k, v in freq.items():
            try:
                trigrams[k] += v;
            except KeyError:
                trigrams[k] = v
    return trigrams
