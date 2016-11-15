import random
from string import ascii_lowercase

VIGENERE_KEY_LENGTH = 5
ROTATION_VALUE = {letter: value for letter, value in zip(ascii_lowercase, range(len(ascii_lowercase)))}
names = []

def random_pad(text, length):
    while len(text) < length:
        text += random.choice(ascii_lowercase)
    return text

def rotate(letter, num):
    # lowercase a-z only
    number_representation = ROTATION_VALUE[letter]
    number_representation += num
    number_representation %= len(ascii_lowercase)
    rotated_letter = chr(number_representation + ord('a'))
    return rotated_letter

def vigenere(text, key='santa'):
    result = []
    for index, letter in enumerate(text):
        result.append(rotate(letter, ROTATION_VALUE[key[index % len(key)]]))
    return ''.join(result)

with open('names.txt') as f:
    for name in f:
        names.append(name.strip())

longest_name = max(len(name) for name in names)
mapping = list(range(len(names)))
while any(mapping[i] == i for i in range(len(mapping))):
    random.shuffle(mapping)

vigenere_key = ''.join(random.choice(ascii_lowercase) for _ in range(VIGENERE_KEY_LENGTH))
encoded_names = {name: vigenere(random_pad(name, longest_name), vigenere_key) for name in names}

with open('result.txt', 'w') as f:
    f.write('Vigenere key: {}\n\n'.format(vigenere_key))
    for index, name in enumerate(names):
        f.write('{}: {}\n'.format(name, encoded_names[names[mapping[index]]]))
