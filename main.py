# Contador

import os
import time

contador = int(input("Informe um número: "))
os.system('cls')

while contador >=0:
    print(f'Auto destruição em: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -=1

print('A COBRA FUMOU !!!')
    
