import string
from gerasenha import gs
import time

fonte = string.ascii_letters + string.digits + string.punctuation
senha = gs(3)
tam = 3
cobaia = ['','','']
qtd = len(fonte)
tinicial = time.time()
for i in range(qtd):
    cobaia[0] = fonte[i]
    for i in range(qtd):
        cobaia[1] = fonte[i]
        for i in range(qtd):
            cobaia[2] = fonte[i]
            if cobaia == list(senha):
                print('------------------')
                print('SENHA QUEBRADA')
                print(f'A SENHA EH {"".join(cobaia)}')
                tempofinal = time.time()
                t = str(tempofinal - tinicial)
                print('FORAM DECORRIDOS ' + t[0:4] +'s')
                print('------------------')
                break
