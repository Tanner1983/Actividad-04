import os

def menu(): 
    
    print ("Selecciona una opción")
    print ("\t1 - Estreno ($4.200)")
    print ("\t2 - Infantil ($2.500)")
    print ("\t3 - 3D ($5.500)")
    print ("\t4 - Documentales ($1.800)")    
    print ("\t5 - salir")

def pelicula(cantidad, valor, tipo):
    print(f"Pelicula de tipo {tipo} -- {cantidad} Entradas -- Total a cancelar: $", valor *cantidad)	    		        
    input("\npulsa una tecla para continuar")
    return
