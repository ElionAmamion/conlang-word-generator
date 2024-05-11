from contextlib import redirect_stdout as rout
import random as r

def word():
    start = r.choice(["f", "h", "l", "m", "n", "N", "g", "k", "p", "r", "s", "S", "th", "TH", "w", "s"])

    vocala = r.choice(["a:","e", "o"])

    mid = r.choice(["f", "h", "l", "m", "N", "r", "s", "S", "th", "w"])

    vocalb = r.choice(["a:","e", "e..(r)", "Ou", "o"])

    short_long = r.randint(1, 2)
    if short_long == 1:
        word = start + vocala + mid + vocalb
    elif short_long == 2:
        word = start + vocala + mid

    return word
#           |-------change to wanted data format
#          \ /
with open("word_list.odt", "a") as t:
    with rout(t):
        print(word(), "\n", word(), "\n", word(), "\n", word(), "\n", word(), "\n")