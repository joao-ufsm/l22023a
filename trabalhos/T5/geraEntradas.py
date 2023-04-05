#!/usr/bin/python

import random
import string

for i in range(25):
    carga = []
    n = random.randint(20,50)
    for j in range(n):
        c = random.choice(string.ascii_uppercase[:15])
        carga.append(c)
    for c in carga:
        print(c,end='')
    print('')
   
