"""
anagrams.py

Author: Rafeh Qazi

Modified: June 2016

Copyright (C) 2016 Rafeh Qazi
"""

from collections import Counter


def read_file(file):
    with open(file, 'r') as f:
        return [word[:-1] for word in f]


file_data = read_file('shortWordList.txt')

# print(file_data)
#
# for _ in range(5):
#     print('\n')
#
# anagrams = []
# for word_1 in file_data:
#     file_data.pop(0)
#     word_1_anagrams = []
#     for word_2 in file_data:
#         if Counter(word_1) == Counter(word_2):
#             if word_2 not in anagrams:
#                 word_1_anagrams.append(word_2)
#                 anagrams.append(word_2)
#     if word_1_anagrams:
#         print(word_1_anagrams)

# print(anagrams)
