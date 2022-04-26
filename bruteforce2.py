import string
from itertools import combinations_with_replacement as cwr
from gerasenha import gs
import time

fonte = string.ascii_letters + string.digits + string.punctuation
senha = list('123') # list(gs(3))
senhastr = ''.join(senha)
tam = len(senha)
cobaia = list(cwr(fonte, tam))
tinicial = time.time()
for n in range(len(list(cobaia))):
    if list(cobaia[n]) == senha:
        print('------------------')
        print("Senha quebrada")
        print(f"A senha eh: {senhastr}")
        tempofinal = time.time()
        t = str(tempofinal - tinicial)
        print('FORAM DECORRIDOS ' + t[0:4] +'s')
        print('------------------')
        break


