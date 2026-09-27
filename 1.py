import ciphers
from helpers import *


ciphertext = "X pqolkd hbv molqbzqp zlkcfabkqfxi fkclojxqflk"


def main():
    print(f"Guess #1(I->X: 15): {ciphers.ceasers_cipher(ciphertext, ord('I') - ord('X'))}")
    print(f"Guess #2(A->X: 23): {ciphers.ceasers_cipher(ciphertext, ord('A') - ord('X'))}")

    return 0


main()