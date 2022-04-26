import string
from random import random, choice

def gs(t): # funcao para gerar senhas aleatorias
    fonte = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for i in range(t):
        senha += choice(fonte)
    return senha