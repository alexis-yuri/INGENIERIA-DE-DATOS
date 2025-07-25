# 
# EJERCICIOS VARIOS
# 
# ALEXIS YURI M.
#
"""
class Persona:
    especie = 'Humano' # Atributo de clase
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo de instancia
        self.edad = edad
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

p = Persona('Ana', 30)
print(p.saludar())        

persona1 = Persona("Carlos", 28)
persona2 = Persona("María", 32)
print(persona1.especie) # Output: Humano
print(persona2.nombre) # Output: María



class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo
    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

mi_cuenta = Cuenta(100000)
print(mi_cuenta.mostrar_saldo())



class Producto:
    def __init__(self, precio):
        self._precio = precio

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self._precio = valor
        else:
            print("El precio debe ser positivo.")


p = Producto(100)
print(p.precio) # Output: 100

p.precio = 150 #decorator
print(p.precio)


#HERENCIA
class Animal:
    def comer(self):
        print("El animal está comiendo.")

class Perro(Animal):
    def ladrar(self):
        print("El perro está ladrando.")

mi_perro = Perro()
mi_perro.comer() # Output: El animal está comiendo.
mi_perro.ladrar() # Output: El perro está ladrando.

class Terrestre:
    def desplazar(self):
        print("El animal camina.")

class Acuatico:
    def desplazar(self):
        print("El animal nada.")

class Anfibio(Terrestre, Acuatico):
    pass

anfibio = Anfibio()
anfibio.desplazar() # Output: El animal camina.

print(Anfibio.__mro__)

class Ave:
    def volar(self):
        print("El ave vuela.")

class Avion:
    def volar(self):
        print("El avión vuela.")

def hacer_volar(objeto):
    objeto.volar()

pajaro = Ave()
boeing = Avion()

hacer_volar(pajaro) # Output: El ave vuela.
hacer_volar(boeing) # Output: El avión vuela.


class Calculadora:
    def sumar(self, *args):
        return sum(args)
    
calc = Calculadora()
print(calc.sumar(1, 2)) # Output: 3
print(calc.sumar(1, 2, 3, 4)) # Output: 10


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
    
persona = Persona("Lucía", 27)
print(persona) # Output: Lucía, 27 años

"""


