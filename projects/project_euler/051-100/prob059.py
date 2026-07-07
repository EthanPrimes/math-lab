from itertools import product

CIPHERTEXT_FILE = "projects/project_euler/051-100/data_files/prob059.txt"
LOWER_ASCII_LETTERS = [i for i in range(97, 123)]
COMMON_WORDS = [
    " the ",
    "of",
    "be",
    "to",
]

with open(CIPHERTEXT_FILE, "r") as file:
    CIPHERTEXT = list(map(int, file.readline().split(",")))


def decrypt(chars):
    message = ""
    for i in range(len(CIPHERTEXT)):
        message += chr(CIPHERTEXT[i] ^ chars[i % 3])

    return message

for c1, c2, c3 in product(LOWER_ASCII_LETTERS, repeat=3):
    message = decrypt([c1, c2, c3])
    if all(word in message for word in COMMON_WORDS):
        print(message)
        print(chr(c1), chr(c2), chr(c3))

key = [ord(c) for c in "exp"]
total = 0
for index, char in enumerate(CIPHERTEXT):
    total += char ^ key[index % 3]

print(total)
