class Perro:
    def __init__(self, raza, altura, peso, tamaño, sexo, pelaje, color, edad, largo_de_cola, inteligencia):
     
        self.raza = raza
        self.altura = altura
        self.peso = peso
        self.tamaño = tamaño
        self.sexo = sexo
        self.pelaje = pelaje
        self.color = color
        self.edad = edad
        self.largo_de_cola = largo_de_cola
        self.inteligencia = inteligencia

        print(f"Raza: {self.raza}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Sexo: {self.sexo}")
        print(f"Pelaje: {self.pelaje}")
        print(f"Color: {self.color}")
        print(f"Edad: {self.edad}")
        print(f"Largo de cola: {self.largo_de_cola}")
        print(f"Inteligencia: {self.inteligencia}")

        def ladrar(self):
            print(f"El {self.raza} está ladrando: ¡Guau, guau!")

        def comer(self):
            print(f"El perro de tamaño {self.tamaño} está comiendo sus croquetas.")

        def dormir(self):
            print(f"El perro de {self.edad} se ha quedado dormido.")

        def jugar(self):
            print(f"El perro mueve su cola de {self.largo_de_cola} mientras juega.")

        def correr(self):
            print(f"El perro corre rápido gracias a su excelente condición física.")

mi_perro = Perro("Pug", "30 cm", "8 kg", "Chico", "Macho", "Corto", "Arena", "3 años", "Corto y rizado", "Media")
