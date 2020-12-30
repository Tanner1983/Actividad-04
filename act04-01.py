a=0
frase = input("Ingrese una frase: ")
letrita= input("\nIngrese letra a buscar: ")

for letra in frase:
    if letra == letrita:
        a+=1
    #print(letra)

if a == 0:
    print("No aparece en la frase la letra ", letrita)
elif a ==1:
    print(a, "vez se repite dentro de la frase")
else:
    print(a, "veces se repite dentro de la frase")
