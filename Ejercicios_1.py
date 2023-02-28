"""**1)**

**Haz un programa que calcule los múltiplos de 3**

* Para ello primero primero debe preguntarse al usuario cuántos múltiplos desea añadir. 

* Nota: Puedes usar un bucle while si lo deseas"""

num = int(input("Cuantos multiplos de tres quieres añadir? "))
for i in range(1, num+1):
        print(i * 3)

num = int(input("Cuantos multiplos de tres quieres añadir? "))
lista =[]
i = 1
while i < num + 1:
    print(f"el numero {i * 3} es multiplo de tres")
    lista.append(i)
    i+=1     

#Haz lo mismo con np.arange

import numpy as np
num = int(input("Cuantos multiplos de tres quieres añadir? "))
a = np.arange(num + 1)
dale = [(i * 3) for i in a if i > 0]
dale    