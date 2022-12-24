
import random

def calculate_coprime(n):

    recn = n
    mcdn = []
    coprimesn = []
    counter = 2
    counter2 = 0

    # Se usa un while porque se necesita cambiar la variable de la iteracion en tiempo de ejecucion
    while counter <= recn:
        if (recn/counter).is_integer() == True: # Si la division entre f y el contador es un numero entero, significa que el resultado es un comun divisor
            mcdn.append(counter) # añadir el comun divisor a una lista
            recn = recn/counter # modificar a f porque 90/2 = 45, ahora queremos saber el siguiente comun divisor
            counter = 1 # counter vuelve a valer 1 para volver a iterar desde el numero mas pequeño, que seria el 2 por la suma del iterador
        
        counter += 1 # se le suma 1 para que siga iterando

        # 90 | 2     mcdn = [2, 3, 3, 5]
        # 45 | 3
        # 15 | 3 
        # 5  | 5
        # 1  |
     

    # 1 < e < f  => i tiene que ir de 2 a f, en este caso a n
    for i in range(2, n):
        if (i%2 != 0): # Solo pueden ser numeros impares
            for j in range(2, (n+1)): # el denominador de la division no puede ser 1, porque seria mcd y no se puede el 1 y va hasta f o n pq por ejemplo 5/5, el comun divisor es el 5, si no fuera hasta n quedaria hasta 5/4
                if (i/j).is_integer() == True: # verificar si es comun divisor, para checar si el comun divisor de i está en la lista mcdn, si coincide algun elemento no son coprimos
                    try: # try porque si el elemento no esta en el array mcdn, va a salir una excepcion
                        mcdn.index(j) # verificar si el elemento esta en el array mcdn
                        for k in range(1, counter2): #* Si el elemento j está en el array mcdn, tenemos que eliminar los elementos que habiamos agregado a la lista de coprimos, por eso el contador
                            coprimesn.pop() # pop() elimina el ultimo elemento del array
                        counter2 = 0 # volvemos a reiniciar el contador 
                        break # si está en el array mcdn, rompe el array y pasa al siguiente posible coprimo i
                    except:
                        counter2 += 1 # si no está en el arrray vamos haciendo un contador para el segmento try
                        coprimesn.append(i) #* si no está en el array mcdn agregamos al posible cofactor a otro array, pero este puede que el tercer elemento si esté en el array mcdn, por eso el contador
                        pass

    # 90 | 2        71 | 71     3 | 3
    # 45 | 3        1  |        1 |
    # 15 | 3
    # 5  | 5        El numero 71 es coprimo de 90 porque no comparten ningun comun divisor mas que el 1
    # 1  |          El numero 3 NO es coprimo de 90 porque comparte el numero 3 como comun divisor

    return coprimesn

def get_coprime(n1):

    e = random.choices(calculate_coprime(n1)) # Chooses a random element from the list

    return e
