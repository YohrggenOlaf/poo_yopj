class Mesa:
    def __init__(self, material, forma, color, cantidad_patas, uso, altura, resistencia, compartimientos, ensamble, marca):
     
        self.material = material
        self.forma = forma
        self.color = color
        self.cantidad_patas = cantidad_patas
        self.uso = uso
        self.altura = altura
        self.resistencia = resistencia
        self.compartimientos = compartimientos
        self.ensamble = ensamble
        self.marca = marca

        print(f"Material: {self.material}")
        print(f"Forma: {self.forma}")
        print(f"Color: {self.color}")
        print(f"Cantidad de patas: {self.cantidad_patas}")
        print(f"Uso: {self.uso}")
        print(f"Altura: {self.altura}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Compartimientos: {self.compartimientos}")
        print(f"Ensamble: {self.ensamble}")
        print(f"Marca: {self.marca}")

        def soportar_peso(self):
            print(f"La mesa de {self.material} está soportando objetos sin problemas.")

        def organizar_espacio(self):
            print(f"La superficie de forma {self.forma} está permitiendo organizar las cosas.")

        def limpiar_superficie(self):
            print(f"Se ha limpiado la superficie de color {self.color} para mantenerla impecable.")

        def ajustar_posicion(self):
            print(f"La mesa se mantiene firme gracias a sus {self.cantidad_patas} patas.")

        def utilizar_funcion(self):
            print(f"La mesa está siendo utilizada para su función principal: {self.uso}.")

mi_mesa = Mesa("Madera de pino", "Rectangular", "Café roble", "4 patas", "Escritorio de estudio", "75 cm", "Hasta 80 kg", "2 cajones laterales", "Tornillos Allen", "Walmart")
