import requests
import argparse
from bs4 import BeautifulSoup

LANGUAGES = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', \
             'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish', 'All']


def get_user_input():
    print("""Hello, you're welcome to the translator. Translator supports: """)
    for num, lang in enumerate(LANGUAGES, start=1):
        print(f"{num}. {lang}")
    print("Type the number of your language:")
    user_input1 = input()
    user_src = LANGUAGES[int(user_input1) - 1]
    print("Type the number of language you want to translate to:")
    user_input2 = input()
    if user_input2 == '0':
        user_trg = 0
    else:
        user_trg = LANGUAGES[int(user_input2) - 1]
    print("Type the word you want to translate:")
    word_to_trans = input()
    return user_src, user_trg, word_to_trans


def get_translations(user_src, user_trg, word_to_trans):
    base_url = 'https://context.reverso.net/translation/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    rest_url = user_src.lower() + '-' + user_trg.lower() + '/' + word_to_trans.lower()

    url = base_url + rest_url
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    file_name = word_to_trans + '.txt'

    if r.status_code == 200:
        print('200 OK')
        words = soup.find_all('a', class_='translation')
        sentences_o = soup.select('div.src.ltr')
        sentences_t = soup.select('div.trg.ltr')
    elif r.status_code == 404:
        print(f"Sorry, unable to find  {word_to_trans}")
    else:
        print("Something wrong with your internet connection")

    if r.status_code == 200:
        with open(file_name, 'w', encoding='utf-8') as f:
            if words:
                list_of_words = [item.text.strip() for item in words[1::]]
                # print()
                # print(f'{user_trg} Translations:')
                f.write(f'{user_trg} Translations:\n')
                for index, word in enumerate(list_of_words):
                    if index == 5:
                        break
                    f.write(f"{word}\n")
                    # print(f"{word}")
            if sentences_o:
                # print()
                # print(f'{user_trg} Examples:')
                f.write(f'\n{user_trg} Examples:\n')
                lst_of_origi = [item.text.strip() for item in sentences_o]
                lst_of_trans = [item.text.strip() for item in sentences_t]
                for i in range(0,5):
                    # print(f"{lst_of_origi[i]}")
                    f.write(f"{lst_of_origi[i]}\n")
                    # print(f"{lst_of_trans[i]}")
                    if i == 4:
                        f.write(f"{lst_of_trans[i]}\n")
                    else:
                        f.write(f"{lst_of_trans[i]}\n\n")
                # print()


def translate_all(user_src, user_trg, word_to_trans):
    all_langs = LANGUAGES[::]
    all_langs.remove(user_src.title())
    all_langs.remove('All')
    headers = {'User-Agent': 'Mozilla/5.0'}
    base_url = 'https://context.reverso.net/translation/'
    file_name = word_to_trans + '.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        for lang in all_langs:
            rest_url = user_src.lower() + '-' + lang.lower() + '/' + word_to_trans.lower()
            url = base_url + rest_url
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            if r.status_code == 200:
                print(lang)
                word = soup.find_all('a', class_='translation')[1].text.strip()
                sentence_o = soup.find('div', class_='src').text.strip()
                sentence_t = soup.find('div', class_='trg').text.strip()
                f.write(f'{lang} Translations:\n')
                f.write(f"{word}\n\n")
                f.write(f'{lang} Examples:\n')
                f.write(f"{sentence_o}\n")
                f.write(f"{sentence_t}\n\n")
            elif r.status_code == 404:
                print(f"Sorry, unable to find {word_to_trans}")
            else:
                print("Something wrong with your internet connection")


def read_file(user_src, user_trg, word_to_trans):
    if user_src.title() not in LANGUAGES:
        return print(f"Sorry, the program doesn't support {user_src}")
    elif user_trg.title() not in LANGUAGES:
        return print(f"Sorry, the program doesn't support {user_trg}")

    if user_trg != 'all':
        get_translations(user_src, user_trg, word_to_trans)
    elif user_trg == 'all':
        translate_all(user_src, user_trg, word_to_trans)
    file_name = word_to_trans + '.txt'
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f.read().splitlines():
                print(line)
    except FileNotFoundError:
        pass


parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('trg')
parser.add_argument('word')
args = parser.parse_args()

# get_translations(*get_user_input())
read_file(args.src, args.trg, args.word)



