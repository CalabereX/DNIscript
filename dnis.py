import random

def generar_valor_unico(nombre):
    random.seed(nombre)


    numeros_aleatorios = ''.join(str(random.randint(0, 9)) for _ in range(8))

    letra_aleatoria = chr(random.randint(ord('A'), ord('Z')))

    valor_unico = numeros_aleatorios + letra_aleatoria

    return valor_unico

#nombre = "Ejemplo" 

valor = generar_valor_unico(nombre = input("Indque el nombre: "))
print("Valor generado:", valor)
