
# Global variables
UPPER = ord('A')
LOWER = ord('a')
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_POWER = len(ALPHABET)
LETTER_PROBABILITIES = [
    0.0817,  # A
    0.0129,  # B
    0.0278,  # C
    0.0425,  # D
    0.1270,  # E
    0.0223,  # F
    0.0202,  # G
    0.0609,  # H
    0.0697,  # I
    0.0015,  # J
    0.0077,  # K
    0.0403,  # L
    0.0241,  # M
    0.0675,  # N
    0.0751,  # O
    0.0193,  # P
    0.0010,  # Q
    0.0599,  # R
    0.0633,  # S
    0.0906,  # T
    0.0276,  # U
    0.0098,  # V
    0.0236,  # W
    0.0015,  # X
    0.0197,  # Y
    0.0007   # Z
]

def caesars_cipher(plaintext:str, shift:int) -> str:
    """Caesars cipher algorithm"""
    ciphertext = ''
    for char in plaintext:
        # Skip if char isnt alphabetical
        if not char.isalpha(): 
            ciphertext += char
            continue

        # Shifted char
        shifted = ALPHABET[(ALPHABET.index(char.upper()) + shift) % ALPHABET_POWER]

        # If origin char is lowercase
        if char.islower(): shifted = shifted.lower()
        ciphertext += shifted

    return ciphertext


def vigenere_cipher(plaintext:str, key:str) -> str:
    """ Vigenére cipher algorithm"""
    key = key.upper()
    ciphertext = ''
    for i in range(len(plaintext)):
        # Take shift of [i % key_len] character
        try:
            shift = ALPHABET.index(key[i % len(key)])
        except ValueError:
            print(f"{key[i % len(key)]} char isnt in alphabet variable!")
            shift = 0

        # Add shift
        shifted = ALPHABET[(ALPHABET.index(plaintext[i].upper()) + shift) % ALPHABET_POWER]
        
        # Lowering char if origin was
        if plaintext[i].islower(): shifted = shifted.lower()
        ciphertext += shifted

    return ciphertext


def vigenere_decipher(ciphertext: str, key:str) -> str:
    """ Vigenére decipher algorithm """
    key = key.upper()
    plaintext = ''
    for i in range(len(ciphertext)):
        try:
            shift = ALPHABET.index(key[i % len(key)])
        except ValueError:
            print(f"{key[i % len(key)]} char isnt in alphabet variable!")
            shift = 0

        # Substracting shift
        shifted = ALPHABET[(ALPHABET.index(ciphertext[i].upper()) - shift) % ALPHABET_POWER]

        # Lowering char if origin was
        if ciphertext[i].islower(): shifted = shifted.lower()
        plaintext += shifted

    return plaintext


def substitute(plaintext: str, substitute_alpha:str, alphabet:str = ALPHABET) -> str:
    """ Alphabet substitution algorithm """
    assert len(substitute_alpha) == len(alphabet)
    substitute_alpha = substitute_alpha.upper()
    alphabet = alphabet.upper()
    ciphertext = ''

    for char in plaintext:
        if char.upper() in alphabet: 
            if char.islower(): 
                ciphertext += substitute_alpha[alphabet.index(char.upper())].lower()
            else:
                ciphertext += substitute_alpha[alphabet.index(char.upper())]
        else:
            ciphertext += char
    return ciphertext
