#Ejercicio 1

# def sistema():
#     try:
#         fracc_solicitada = input("Ingrese una fracción en formato (X/Y): ")
#         x, y = map(int, fracc_solicitada.split('/'))
       
#         if y==0:
#             print("ZeroDivisionError: No se puede dividir por cero. Intente de nuevo ")
#             sistema()

#         if not (x <= y and y != 0 ):
#             print("El numerador debe ser menor o igual que el denominador. Vuelva a intentarlo.")
#             sistema()
#             return

#         fraccion_decimal = x / y
#         porcentaje_redondeado = round(fraccion_decimal * 100)

#         print(f"{porcentaje_redondeado}%")

#         if fraccion_decimal <= 0.01 * porcentaje_redondeado:
#             print("E")
#         elif fraccion_decimal > 0.99 * porcentaje_redondeado:
#             print("F")
#         else:
#             print(f"{porcentaje_redondeado}%")
#     except ValueError:
#         print("ValueError: Solo se permiten números enteros (X/Y). Intente de nuevo ")
#         sistema()
    
# sistema()

#Ejercicio 2

# def registrar_nota():
#     try:
#         nota_solicitada=input("Ingrese las notas separadas por coma: ")
#         lista_notas=list(map(int,nota_solicitada.split(",")))

#         print(lista_notas)

#     except:
#         print("Error en el tipeo o formato de nota. Intente ingresar las notas nuevamente. ")
#         registrar_nota()
    
# registrar_nota()

#Ejercicio 3

def calcular_coeficiente(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return calcular_coeficiente(n - 1, k - 1) + calcular_coeficiente(n - 1, k)

def imprimir_triángulo_pascal(filas):
    for i in range(filas):
        for j in range(i + 1):
            coeficiente = calcular_coeficiente(i, j)
            print(coeficiente, end=" ")
        print()

n = int(input("Ingrese el número de filas del triángulo de Pascal: "))

imprimir_triángulo_pascal(n)


#Ejercicio 4

# solic_cadena=input("Ingrese una frase o palabra: ")
# palabras = solic_cadena.split()

# if palabras:
#     ultima_palabra = palabras[-1]
#     long_ult_palabra = len(ultima_palabra)
# else:
#     long_ult_palabra = 0

# print(f"La longitud de la ultima palabra de {solic_cadena} es: {long_ult_palabra}")


#Ejercicio 5

#Ejercicio 6

