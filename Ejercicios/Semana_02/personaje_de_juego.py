class PersonajeJuego:
    def __init__(self, nombre, clase, nivel, vida, mana, arma, habilidad_especial, elemento, faccion, estado):     
        
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.vida = vida
        self.mana = mana
        self.arma = arma
        self.habilidad_especial = habilidad_especial
        self.elemento = elemento
        self.faccion = faccion
        self.estado = estado

        print(f"Nombre: {self.nombre}")
        print(f"Clase: {self.clase}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida: {self.vida}")
        print(f"Maná: {self.mana}")
        print(f"Arma: {self.arma}")
        print(f"Habilidad especial: {self.habilidad_especial}")
        print(f"Elemento: {self.elemento}")
        print(f"Facción: {self.faccion}")
        print(f"Estado: {self.estado}")

        def usar_habilidad(self):
            print(f"El {self.clase} desata su poder usando {self.habilidad_especial}.")

        def subir_nivel(self):
            print(f"El personaje ha subido más allá del nivel {self.nivel} tras ganar experiencia.")

        def recibir_daño(self):
            print(f"La barra de {self.vida} disminuye tras recibir un golpe crítico.")

        def canalizar_elemento(self):
            print(f"El personaje canaliza magia vinculada al elemento {self.elemento}.")

mi_personaje = PersonajeJuego("Arthas", "Guerrero/Paladín", "Nivel 80", "5000 HP", "2000 MP", "Espada Agonía de Escarcha", "Espiral de la Muerte", "Hielo/Oscuridad", "La Plaga", "Activo")
