import random as r

def word():
    start = r.choice(["ʒ", "ð", "ɜ"])

    vocala = r.choice(["B", "ɢʘ", "ɤ̞"])

    mid = r.choice(["ɱ", "m"])

    vocalb = r.choice(["m", "ɾ"])

    ra = r.randint(1, 2)

    if ra == 1:
        word = start + vocala + mid
    else:
        word = start + vocala + mid + vocalb

    return word

for i in "abcdefghijklmnopqrstuvwxy":
    print(word(), "\n")
