# Úvodní hlavička.
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Nárožný
email: narozny.jakub@gmail.com
discord: Jakub N.
"""

# Import dat z podpůrných souborů.
from logo import project_name
from users_db import users_list
from task_template import TEXTS
import re

# Pomocné proměnné.
titlecase_w = 0
uppercase_w = 0
lowercase_w = 0
numbers = 0
all_numbers_sum = 0
len_all_words = list()

# Logo
print(project_name)
print("$ python projekt1_druhe_odevzdani.py\nversion 1.0.0")

# Vyžádání přihlašovacího jména a hesla.
username = input("username: ")
password = input("password: ")

# Ověření a pozdrav registrovaného uživatele.
if users_list.get(username) == password:
    print(f"{"-" * 40}\n"
          f"Welcome to the app, {username}\n"
          f"We have 3 texts to be analyzed.\n"
          f"{"-" * 40}")
# Uživatel není registrovaný.
else:
    print("unregistered user, terminating the program..")
    exit()

# Výběr textu z proměnné TEXTS.
users_input = input("Enter a number btw. 1 and 3 to select: ")
print("-" * 40)

# Zadána nesprávná hodnota pro výběr textu.
if users_input.isnumeric() is False:
    print("Wrong input, terminating the program..")
    exit()
else:
    choice = int(users_input)

# Zadáno číslo z výběru.
if choice in range(1, 4):
    # Odstranění tečky z textu.
    clean_text = TEXTS[choice - 1].replace(".", "")
    clean_text = clean_text.replace(",", "")

    # Rozdělení textu na slova a jejich počet.
    all_words = re.split(r"[\s,\n]", clean_text)
    word_counter = len(all_words)

    for word in all_words:
        # Počet slov začínajících velkým písmenem.
        if word.istitle():
            titlecase_w += 1

        # Počet slov psaných velkými písmeny.
        elif word.isupper():
            uppercase_w += 1

        # Počet slov psaných malými písmeny.
        elif word.islower():
            lowercase_w += 1

        # Počet a součet všech čísel v textu.
        elif word.isnumeric():
            numbers += 1
            all_numbers_sum += int(word)

        # Četnost délek slov.
        len_w = len(word)
        len_all_words.append(len_w)

    # Výsledky statistiky vybraného textu.
    print(f"There are {word_counter} words in the selected text.\n"
          f"There are {titlecase_w} titlecase words.\n"
          f"There are {uppercase_w} uppercase words.\n"
          f"There are {lowercase_w} lowercase words.\n"
          f"There are {numbers} numeric strings.\n"
          f"The sum of all the numbers {all_numbers_sum}\n"
          f"{"-" * 40}")

    # Sloupcový graf četnosti délek slov v textu.
    occurences = list(set(len_all_words))
    heading = "LEN|{:^20}|NR."f"\n{"-" * 40}"
    print(heading.format("OCCURENCES"))

    #  Grafický výpis pro jednotlivá slova.
    for i in occurences:
        word_occurence = len_all_words.count(i)
        print(("{:>3}".format(i)), end="")
        table = "|{:<20}"f"|{word_occurence}"
        stars = '*' * word_occurence + (' ' * (max(occurences) - word_occurence))
        print(table.format(f"{stars}"))

# Zadáno nesprávné číslo pro výběr textu.
elif choice not in range(1, 4):
    print("Incorrect number, terminating the program..")
