import random  # Importa el módulo random para generar números aleatorios.

def generar_valor_unico(nombre):
    random.seed(nombre)  # Establece la semilla del generador de números aleatorios.

    numeros_aleatorios = ''.join(str(random.randint(0, 9)) for _ in range(8))  # Genera una cadena de 8 dígitos aleatorios.

    letra_aleatoria = chr(random.randint(ord('A'), ord('Z')))  # Genera una letra aleatoria en mayúsculas.

    valor_unico = numeros_aleatorios + letra_aleatoria  # Combina los dígitos y la letra aleatoria.

    return valor_unico  # Devuelve el valor único generado.

#nombre = "Ejemplo" 

valor = generar_valor_unico(nombre = input("Indique el nombre: "))  # Llama a la función con el nombre ingresado por el usuario.
print("Valor generado:", valor)  # Imprime el valor generado.
