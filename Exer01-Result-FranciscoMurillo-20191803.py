"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya

cliente:
    mira me gusta pero cada vez que inicio el programa, me borra el cliente anterior
    y solo puedo guardar el que he ingresado en ese momento, no habria forma de
    que se guarde a los 3 clientes que tengo?
programador:
    vaya
mente:
    y pollo no queres?

cliente:
    mira esta buenisimo peeeerroooooo, fijate que mi clientela a aumentado a veces tengo
    3 a veces 5  a veces 10 osea ya no se cuantos clientes tendre en un dia, podrias
    agregarle alguna forma de que yo le diga cuando quiero que se detenga y que me muestre
    el reporte de lo que llevo en costo total hasta ese momento.
programador:
    vaya
mente:
    no te pide nada el gusto mono


"""
"""-------------------------------------------"""
# RESOLUCIÓN DEL EJERCICIO
# creando la lista vacia
listaRegistro = []
costoTotal = 0
request = input("¿Desea registrar usuarios?")
i = 0
j = 0
if request == ("No" or "no"):
    print("Tenga buen día")

elif request == ("Sí" or "sí"):
    clientes = int(input("¿Cuántos clientes desea agregar?"))
    while request == ("Sí" or "sí"):

        while i < clientes:
            print("Cliente " + str(i + 1))
            cliente = input("Nombre del cliente: ")
            producto = input("Producto: ")
            costo = float(input("Costo ($0.00): "))
            print("")
            print("-----------------------------------")
            print("")

            # punto de programa
            # registro = {"cliente": cliente, "producto": producto, "costo": costo}
            registro = dict(cliente=cliente, producto=producto, costo=costo)
            # como agrego un elemento nuevo a una lista?
            listaRegistro.append(registro)
            # dejar de ocupar la variable registro
            # registro = None
            costoTotal += costo
            i += 1
        request = input("¿Desea registrar usuarios?")
        j += i
        if request == ("No" or "no"):
            print(
                "El costo total de los "
                + str(j)
                + " clientes ingresados es de: $"
                + str(costoTotal)
            )
        elif request == ("Sí" or "sí" or "si" or "sí"):
            i = 0
            clientes = int(input("¿Cuántos clientes desea agregar?"))
