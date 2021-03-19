import random
import re
from nltk.tokenize import WhitespaceTokenizer
from nltk.util import trigrams
from collections import Counter

file = 'corpus.txt'

def generate_first_word(key_words):
    random_word = random.choice(key_words)
    while True:
        if re.match("^[A-Z][a-z'\s]+[,\.]?$", random_word):
            break
        else:
            random_word = random.choice(key_words)
    return random_word


with open(file, 'r', encoding='utf-8') as f:
    text = f.read()
    tk = WhitespaceTokenizer()
    words = tk.tokenize(text)
    tri_words = [(' '.join(word[0:2]), word[2]) for word in trigrams(words)]
    d = {}
    for item in tri_words:
        d.setdefault(item[0], [])
        d[item[0]].append(item[1])

counted_dict = {key: Counter(value).most_common(7) for key, value in d.items()}

def return_random_sentence(counted_dict):
    sentence = []
    key_words = [key for key in counted_dict.keys()]
    random_word = generate_first_word(key_words)
    random_word_sec = random_word.split()[1]
    sentence.append(random_word)
    i = 1
    while True:
        if i == 1:
            while True:
                if re.match("^[A-Z][a-z'\s]+[,\.]?$", random_word):
                    break
                else:
                    random_word = generate_first_word(key_words)
        lst = counted_dict[random_word]
        s = [c[0] if len(lst) > 1 else lst[0][0] for c in lst]
        w = [c[1] if len(lst) > 1 else lst[0][1] for c in lst]
        next_word = random.choices(s, w, k=1)[0]
        next_word = random_word_sec + ' ' + next_word
        try:
            lst2 = counted_dict[next_word]
        except KeyError:
            next_word = random.choices(s, w, k=1)[0]
            next_word = random_word_sec + ' ' + next_word
        sentence.append(next_word.split()[1])
        random_word = next_word
        random_word_sec = random_word.split()[1]
        if bool(re.match("[A-Za-z'\s]+[?!\.-]$", random_word)) and i >= 4:
            break
        if len(sentence) == 4 and bool(re.match(r"[a-zA-Z\'\"]+[?!.]+$", sentence[3])):
            break
        i += 1
    return ' '.join(sentence)

sentence = return_random_sentence(counted_dict)

sentences = []

for s in range(0, 3):
    sentence = return_random_sentence(counted_dict)
    sentences.append(sentence)

for sentence in sentences:
    print(sentence)





