"""conversion de datos"""

"""de string: str a entero: int"""

var_1 = "860"   # string
var_2 = 6789    # int
var_3 = 89.67   # float
var_4 = "900"

suma_string = var_1 + "+" + var_4
print("suma de string:{}".format(suma_string))

"""conversion"""
conversion = int(var_1)

print("el valor de mi variable 'conversion' es: {}".format(conversion))
print("el tipo de dato de mi variale 'conversion' es: {}".format(type(conversion)))

suma = conversion + var_2
print("la suma de mi variables es: {}".format(suma))

"""suma de dos variables: int + float = float"""

suma_2 = var_2 + var_3
print("la suma de 'var_2' y 'var_3' es: {}".format(suma_2))
print(type(suma_2))

"""conversion: de flotante a int"""

conversion_2 = int(suma_2)

print("el valor de mi variables 'conversion_2' es: {}".format(conversion_2))