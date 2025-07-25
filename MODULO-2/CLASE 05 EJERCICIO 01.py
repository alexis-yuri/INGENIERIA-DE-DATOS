# 
# EJERCICIO 01
# 
# ALEXIS YURI M.
#
"""
Convierte a código Python esa class Auto(), con los atributos, métodos y estados que se menciona en la diapositiva.

Paso a Paso:
1. Observar con detenimiento la imagen, identificar todas las partes que componen a una clase.
2. Traducirlas a código Python, recordar las buenas prácticas.
3. Crear todas las instancias de Auto() que quieras (crear al menos una para asegurarnos de que funciona)

"""

# Se define la clase Auto con sus atributos, comportamientos y estados.
class Auto:
    def __init__(self, color, peso, tamaño, alto, largo, ruedas, puertas, tipo):
        self.color = color
        self.peso = peso
        self.tamaño = tamaño
        self.alto = alto
        self.largo = largo
        self.ruedas = ruedas
        self.puertas = puertas
        self.tipo = tipo
        self.estado = "Detenido"  

    def arrancar(self):
        if self.estado != "Dañado":
            self.estado = "Circulando"
            print("El auto arrancó.")
        else:
            print("El auto está dañado y no puede arrancar.")

    def acelerar(self):
        if self.estado == "Circulando":
            print("El auto está acelerando.")
        elif self.estado == "Detenido":
            print("El auto está detenido. Debe arrancar primero.")
        elif self.estado == "Estacionado":
            print("El auto está estacionado. Debe arrancar primero.")
        else:
            print("No se puede acelerar.")

    def frenar(self):
        if self.estado == "Circulando":
            self.estado = "Detenido"
            print("El auto ha frenado.")
        else:
            print("El auto no está circulando.")

    def girar(self, direccion):
        if self.estado == "Circulando":
            print(f"El auto gira hacia {direccion}.")
        else:
            print("El auto debe estar en movimiento para girar.")

    def estacionar(self):
        if self.estado == "Circulando" or self.estado == "Detenido":
            self.estado = "Estacionado"
            print("El auto se ha estacionado.")
        else:
            print("No se puede estacionar en este estado.")

    def daniar(self):
        self.estado = "Dañado"
        print("El auto está dañado.")

    def mostrar_estado(self):
        print(f"Estado actual del auto: {self.estado}")

    def mostrar_atributos(self):
        print("\nAtributos del Auto:")
        print(f"Color: {self.color}")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamaño}")
        print(f"Alto: {self.alto} m")
        print(f"Largo: {self.largo} m")
        print(f"Ruedas: {self.ruedas}")
        print(f"Puertas: {self.puertas}")
        print(f"Tipo: {self.tipo}\n")


# Se ingresan atributos para crear un objeto Auto.
def main():
    mi_auto = Auto(
        color="Azul",
        peso=1700,
        tamaño="Mediano",
        alto=1.6,
        largo=4.2,
        ruedas=4,
        puertas=5,
        tipo="SUV"
    )

    # Se muestran los atributos del objeto Auto creado.
    mi_auto.mostrar_atributos()

    # Se ejecutan los comportamientos del objeto Auto creado.
    mi_auto.mostrar_estado()
    mi_auto.arrancar()
    mi_auto.acelerar()
    mi_auto.girar("la derecha")
    mi_auto.frenar()
    mi_auto.estacionar()
    mi_auto.daniar()
    mi_auto.arrancar()  # Se prueba arrancar estando dañado.
    mi_auto.mostrar_estado()


# Ejecutar programa
if __name__ == "__main__":
    main()
