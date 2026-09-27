from helpers import *
import csv 
import ciphers

ciphertext = "Дхрчїщй ржкйазх рейтй жсреїкшд єзвєщїеї. Тшбїец ґй рштєд, щй рйдєдс іштшіщх, щшєвєкєзбшщй, щшєіяєжйщй — ейя кхашчц щшаштїьяїи жкєяєжйщїи ей и вєзх... Хзш ряєеїщй — щшдй жшкшжєщс — ьшкшґ вкюзяї ейя х ьшуш; рєійяї ейя х вщхґзюецрю! — ясітй жєаїіїайтї... Жсреїк жсреїкшд! Мйей мєь рейкй істй, ей юя жєтйвєзїа іса Єрейж, жєяї нш щш бшщїарю, еє аєщй дєа х ійзцєкїтйрю; й юя жхзщютйрц тїмй вєзїщй, нє ґйдьйтй щш ехтцяї тйз с мйех, й и рйдєвє Єрейжй, — еє и мйей єрсщстйрц... Рекхмй дхрчюдї жєаївщїайтй, жєякхатю зш-взш жкєайтїтйрю, ахящй жєіїех: ґйдхрец уїієя — вйщьхкяї рахеюец; нш зє еєвє зєн ей мскеєаїщй єііїтй, єіудйксайтй... Жсреяєф йб аєщюг! Х аршкшзїщх щш якйнш. Рехщї ьєкщх, йб чахттф аґютїрю єз аєзї, нє зєнх жєщйтїайтї якхґц тїмс єрштф; ьшкшайей жхь жєекхряйтйрц, — зїдхтй, яскхтй; ґйдхрец тйа юяхрц якїаєщєвх єртхщьїяї — х рхреї щй щїм рекйущє; рехт — мєзєкєд мєзїец; жхт — щй ж'юзц зєуяй єз зєуяї: Дєекю жхз мєтєз зах зєуяї ржйтїтй, іє щш істє ьїд с мйех жкєяскїеї... Іхзєей щшряйґйщщй, ґтїзщх щшаїтйґщх."

def main():
    # vigenere_try()
    # substitution_try()

    words = get_words(ciphertext)
    print("Bigrams:")
    print({k:v for k, v in sorted([pair for pair in count_bigrams(words).items()], key=lambda x: x[1], reverse=True)[:15]})

    print("Trigrams:")
    print({k:v for k, v in sorted([pair for pair in count_trigrams(words).items()], key=lambda x: x[1], reverse=True)[:15]})


    print(ciphers.substitute(ciphertext, "сталвикіойнршпдяуземпгжьчтхцю", "рейтаїяхєищкужзюсґшдівбцьнмчф"))
    return 0


def vigenere_try() -> None:
    """ Trying to difine if ciphertext ciphered by vigenere algorithm"""
    freq = value_sort(get_freq(find_all_subsets(alpha_filter(ciphertext), 5, 2)))
    
    # print(get_words(ciphertext))
    # print(freq)
    
    # Writing to CSV table that I can open in Excel
    with open("pattern_analysis_2.csv", 'w') as file:
        writer = csv.DictWriter(file,["Pattern", "Count"])
        for k, v  in freq.items():
            writer.writerow({"Pattern":k, "Count":v})

    # Finding indexes(positions) of patterns
    postitions = dict()
    for k in freq.keys():
        postitions[k] = find_pos(alpha_filter(ciphertext), k)

    # Calculating distances between patterns
    distances = dict()
    for k, v in postitions.items():
        distances[k] = find_distances(v)

    # Numbers dont have common greatest divider -> plaintext wasnt ciphered using Vigenere Cipher.
    print(distances)
    


def substitution_try() -> None:
    """ Tring to use substitution alphabet, where each cipher letter freq corresponds ukr letter """
    ukranian_alpa = "оаитенлсврідукмпязбьгйчюхжшєїцщфґ"
    ciphertext_alpha = "ЙЄЇХЩЕТРШЗКЯАЖДСЮІЦВМҐЬНУБИЧФГ---".lower()

    # It dont work :(
    print(ciphers.substitute(ciphertext, ukranian_alpa, ciphertext_alpha))

main()