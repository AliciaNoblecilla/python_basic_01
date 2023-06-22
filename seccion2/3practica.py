"""
REQUISITOS:
- Crear 3 variables: nombre, apellido, edad y sueldo
-imprimir el siguiente mensaje: 'hola 'nombre apellido' su sueldo actual es de: sueldo soles
- mostrar la suma(concatenancion) del sueldo y la edad en un mensaje

"""
var_nombre = "alicia"
var_apellido = "noblecilla"
var_edad = "20"
var_sueldo = 3000

print("hola {} {} su sueldo actual es de: {} soles".format(var_nombre,var_apellido,var_sueldo))
"""conversion"""
conversion_sueldo = str(var_sueldo)
suma_string = var_edad + " Y " + conversion_sueldo
print("LA EDAD Y SUELDO ES DE :{}".format(suma_string))

