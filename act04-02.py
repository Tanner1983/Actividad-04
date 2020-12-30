import pkg.moduloCine as cine

while True:
    cine.menu()
    opcionMenu = input("inserta un numero valor >> ")
    
    if opcionMenu == "1":
        print ("Ingrese cantidad de entradas")
        cantidad=int(input(": "))
        cine.pelicula(cantidad, 4200, tipo="Estreno")
        
    elif opcionMenu == "2":
        print ("Ingrese cantidad de entradas")
        cantidad=int(input(": "))
        cine.pelicula(cantidad, 2500, tipo="Infantil")
        
    elif opcionMenu == "3":
        print ("Ingrese cantidad de entradas")
        cantidad=int(input(": "))
        cine.pelicula(cantidad, 5500, tipo="3D")
        
    elif opcionMenu == "4":
        print ("Ingrese cantidad de entradas")
        cantidad=int(input(": "))
        cine.pelicula(cantidad, 1800, tipo="Documentales")
        
    elif opcionMenu == "5":
        print("Hasta pronto!!")
        break
    else:
        print ("")
        input("No ha pulsado una opcion válida\npulsa una tecla para continuar")
        

    
