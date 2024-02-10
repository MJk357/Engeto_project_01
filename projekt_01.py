"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Jelínek
email: jelmic@gmail.com
discord: michal2853
"""
import math

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registered_user = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}
#Pomocne promenne
registered_bool = 0
correct_number = 0
text_number = 0
lenght_dict = {}

#Nacteni uzivatele
name = input('username:')
password = input('password:')

#overeni uzivatele
if password.strip() == registered_user.get(name.strip()):
    registered_bool = 1
else:
    print('unregistered user, terminating the program..')

#Vyber textu
if registered_bool:
    #Uvitani
    print('-' * 40)
    print('Welcome to the app,', name)
    print('We have 3 texts to be analyzed.')
    print('-' * 40)

    #Vyber varianty
    text_number = int(input('Enter a number btw. 1 and 3 to select:'))
    print('-' * 40)
    #Overeni vyberu
    if text_number not in range(1, 4):
        print('Wrong entered value.')
    else:
        correct_number = 1
#Vypocet statistiky
if correct_number:
    my_text = TEXTS[text_number-1].replace('.', '').replace(',', '')

    total_words = 0
    first_letter = 0
    capital_words = 0
    lowercase_words = 0
    numeric = 0
    total_sum = 0
    for word in my_text.split():
        total_words += 1
        if len(word) in lenght_dict.keys():
            lenght_dict[len(word)] = lenght_dict.get(len(word)) + 1
        else:
            lenght_dict[len(word)] = 1
        if word.istitle():
            first_letter += 1
            continue
        if word.isupper():
            capital_words += 1
            continue
        if word.islower():
            lowercase_words += 1
            continue
        if word.isnumeric():
            numeric += 1
            total_sum += int(word)


    #Vypis
    print('There are', total_words, 'words in the selected text.')
    print('There are', first_letter, 'titlecase words.')
    print('There are', capital_words, 'uppercase words.')
    print('There are', lowercase_words, 'lowercase words.')
    print('There are', numeric, 'numeric strings.')
    print('The sum of all the numbers', total_sum)
    print('-' * 40)

    #Graf
    pocet_mezer = math.ceil((max(lenght_dict.values())-10)/2)
    print('LEN|', ' ' * pocet_mezer, 'OCCURENCES', ' ' * pocet_mezer, '|NR.', sep='')
    print('-' * 40)
    for key in sorted(lenght_dict):
        digits = 3 - len(str(key))
        stars = lenght_dict[key]
        empty = (pocet_mezer * 2) + 10 - stars
        print(' ' * digits, key,'|', '*' * stars , ' ' * empty, '|', stars, sep='')
