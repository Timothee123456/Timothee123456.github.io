import nltk
from nltk import ngrams, FreqDist
import total_time as ttime
import time

ttime.start()

def read(filepath, encoding="utf-8"):
    return open(filepath, "r", encoding=encoding).read()

books = (read("Frankenstein.txt"), read("The_Odyssey.txt"), read("Peter_Pan.txt"), read('The_Wonderful_Wizard_of_Oz.txt'), read('Alice_Adventures_in_Wonderland.txt'))
most_common_nb = 20

#bigrams = []
#for book in books:
#    tokens = nltk.word_tokenize(book.lower())
#    bigrams.extend(list(ngrams(tokens, 2)))
## Calculate frequency distribution
#fdist = FreqDist(bigrams)

def loading_bar():
    # globals
    import sys
    import math
    global n
    global total
    global st
    
    # time left
    difference = time.time() - st
    forone = difference / n
    fortotal = (total - n) * forone
    minutes = math.floor(fortotal / 60)
    seconds = round(fortotal - minutes * 60)
    
    # percent
    percent = (n / total) * 100
    total2 = 50
    percent2 = int(percent)
    bar = '█' * (percent2 // 2) + '-' * (total2 - percent2 // 2)
    
    # colours
    blue = '\033[94m'
    orange = '\033[33m'
    purple = '\033[35m'
    end = '\033[0m'
    
    # display
    sys.stdout.write(f'\r|{bar}|'+blue+f' {percent:.2f}% '+end+' --- '+purple+f' {n}/{total} '+end+' --- '+orange+f' {minutes} min {seconds} s'+end)
    sys.stdout.flush()
    n += 1


trigrams = []
words = []
n = 1
total = len(books)
print('\033[32m' + 'Getting trigrams' + '\033[0m')
st = time.time()
for book in books:
    loading_bar()
    tokens = nltk.word_tokenize(book.lower())
    trigrams.extend(list(ngrams(tokens, 3)))
    words.extend(tokens)
words = list(set(words))
trigrams_words = {}

print(f'\n\n' + '\033[32m' + 'Starting trigrams' + '\033[0m')
n = 1
total = len(words)
st = time.time()
for x in words:
    loading_bar()
    # Filter for ...-starting trigrams and count using FreqDist
    fdist3 = FreqDist(trigram for trigram in trigrams if trigram[0] == x)   

    # Get the most common trigram
    trigrams_most_commons = fdist3.most_common(most_common_nb)
    word_list = []
    for i in range(most_common_nb):
        word_list.append([])
    
    for trigram in trigrams_most_commons:
        a = trigrams_most_commons.index(trigram)
        for group in trigram:
            if type(group) is tuple:
                for item in group:
                    if item != group[0]:
                        word_list[a].append(item)
    for item in word_list:
        for i in range(most_common_nb - 1):
            if [] in word_list:
                word_list.remove([])

    trigrams_words.update({x: word_list})

print()
print(trigrams_words)



quadgrams = []
words = []
n = 1
print(f'\n\n' + '\033[32m' + 'Getting quadgrams' + '\033[0m')
total = len(books)
st = time.time()
for book in books:
    loading_bar()
    tokens = nltk.word_tokenize(book.lower())
    quadgrams.extend(list(ngrams(tokens, 4)))
    words.extend(list(ngrams(tokens, 3)))
print(words)
quadgrams_words = {}

print(f'\n\n' + '\033[32m' + 'Starting quadgrams' + '\033[0m')
n = 1
total = len(words)
st = time.time()
for x in words:
    loading_bar()
    # Filter for ...-starting quadgrams and count using FreqDist
    fdist3 = FreqDist(quadgram for quadgram in quadgrams if quadgram[0] == x[0] and quadgram[1] == x[1] and quadgram[2] == x[2])

    # Get the most common quadgram
    quadgrams_most_commons = fdist3.most_common(most_common_nb)
    
    word_list = []
    
    for quadgram in quadgrams_most_commons:
        a = quadgrams_most_commons.index(quadgram)
        for group in quadgram:
            if type(group) is tuple:
                word_list.append(group[3])

    quadgrams_words.update({x: word_list})

print()
print(quadgrams_words)


# Code to replace JSON file
import json

# Save to JSON file
with open('trigrams-dictionary.json', 'w') as json_file:
    json.dump(trigrams_words, json_file)
    
with open('quadgrams-dictionary.json', 'w') as json_file:
    json.dump(quadgrams_words, json_file)

ttime.end()

print('\033[92m' + 'Files has sucessfully been updated.' + '\033[0m')
print(ttime.total() + '\033[1;37m')


# sound
import pygame
pygame.mixer.init()
pygame.mixer.Sound('alert.wav').play()
