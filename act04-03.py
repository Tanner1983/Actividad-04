import pkg.moduloBebida as b

while True:
    b.menu()
    opcionMenu = input("inserte un numero correspondiente a su bebida >> ")
    if opcionMenu == "1":
        print ("Ingrese cantidad de bebidas")
        cantidad=int(input(": "))        
        b.bebida(cantidad, bebida= "Coca-cola")
    elif opcionMenu == "2":
        print ("Ingrese cantidad de bebidas")
        cantidad=int(input(": "))
        b.bebida(cantidad, bebida= "Fanta")
    elif opcionMenu == "3":
        print ("Ingrese cantidad de bebidas")
        cantidad=int(input(": "))
        b.bebida(cantidad, bebida= "Sprite")
    elif opcionMenu == "0":
        print("Hasta pronto!!")
        break
    else:
        print ("")
        input("No ha pulsado una opcion válida\npulsa una tecla para continuar")





