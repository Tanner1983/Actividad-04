def menu():    
    print ("Selecciona una opción")
    print ("\t1 - Coca-Cola")
    print ("\t2 - Fanta")
    print ("\t3 - Sprite")   
    print ("\t0 - salir")

def bebida(cantidad, bebida):
    print("Se entregan ",cantidad," bebidas Marca ", bebida," -- Total a cancelar: $", 400 *cantidad)	    		        
    input("\npulsa una tecla para continuar")
    return
