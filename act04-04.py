#En una tienda se han realizado una serie de ventas (boleta y factura) y se desea
#saber cuántas de éstas fueron realizadas según el siguiente criterio:
#a.	Cantidad de ventas o boletas emitidas
#b.	El total de la venta inferiores  a $10.000
#Se pide:
#•	Una aplicación que permita ingresar n cantidad de ventas.
#•	Por cada venta ingresada, mostrar la estadística solicitada por los criterios mencionados.
#•	Sumar los montos de ventas ingresados y mostrar el total.
tipoVenta=""
ventaBoletas=0
ventaFactura=0
cantidadVentas=0
valorVenta=0
totalInferior = 0
totalTotal=0

while True:
    print("Welcome\nDesea ingresar una nueva venta")
    respuesta = input(": ")
    if respuesta.upper() == "S" or respuesta.upper() == "SI":
        cantidadVentas+=1
        print("Ingrese tipo de venta Boleta o Factura")
        tipoVenta=input(": ")
        valorVenta=int(input("Ingrese valor total de la venta: "))
        
        if tipoVenta.upper()=="BOLETA" or tipoVenta.upper()=="B":
            ventaBoletas +=1
        else:
            ventaFactura +=1
        
        if valorVenta < 10000:
            totalInferior+= valorVenta
            
        totalTotal+=valorVenta

        print("\n======Resultados=======")
        print("Total de ventas: ", cantidadVentas)
        print("Boletas Emitidas: ", ventaBoletas)
        print("Facturas emitidas: ", ventaFactura)
        print("Total de ventas menores a $10000: $",totalInferior)
        print("========================\n")
            
    elif respuesta.upper() == "N" or respuesta.upper() == "NO":
        print("El total de ventas es: $",totalTotal)
        print("Hasta pronto!!")
        break        
    else:
        print ("")
        input("No ha ingresado respuesta valida\npulsa una tecla para continuar")
