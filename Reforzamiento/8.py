"""8.Usando la condicional if imprimir por
pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista vacía."""

primera_lista = []
segunda_lista = ["nombre","edad","año de nacimiento","direccion"]

if len(primera_lista) == 0:
    print("lista vacia")
if len(segunda_lista) != 0:
    print("numero de datos de la lista es de: {}".format(len(segunda_lista)))

