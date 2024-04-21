from contextlib import redirect_stdout as rout
import random as r

def word():
    start = r.choice(["b", "c", "d", "f", "g", "j", "k", "l", "m", "n", "r", "s", "t", "v", "y"])

    vocala = r.choice(["a", "e", "ou"])

    mid = r.choice(["b", "c", "d", "dal", "f", "g", "j", "k", "l", "m", "moun", "n", "r", "ryn", "s", "t", "tsch", "v", "y", "youn"])

    vocalb = r.choice(["a", "e", "ou"])

    short_long = r.randint(1, 2)
    if short_long == 1:
        word = start + vocala + mid + vocalb
    elif short_long == 2:
        word = start + vocala + mid

    return word

with open("word_list.odt", "a") as t:
    with rout(t):
        print(word(), "\n", word(), "\n", word(), "\n", word(), "\n", word(), "\n")