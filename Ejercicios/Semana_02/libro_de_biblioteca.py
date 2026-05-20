class LibroDeBiblioteca:
    def __init__(self, pasta, contenido, cantidad_de_hojas, capitulos, tomos, ilustraciones, portada, autor, editorial, genero_literario):
        
        self.pasta = pasta
        self.contenido = contenido
        self.cantidad_de_hojas = cantidad_de_hojas
        self.capitulos = capitulos
        self.tomo = tomos
        self.ilustraciones = ilustraciones
        self.portada = portada
        self.autor = autor
        self.editorial = editorial
        self.genero_literario = genero_literario

        print(f"La Pasta es el recubrimiento: {self.pasta}")
        print(f"El contenido muestra la información del libro: {self.contenido}")
        print(f"La cantidad de hojas indica la cantidad de contenido: {self.cantidad_de_hojas}")
        print(f"Los capítulos separan el contenido: {self.capitulos}")
        print(f"El tomo nos indica qué parte de la obra es: {self.tomo}")
        print(f"Ilustraciones del libro: {self.ilustraciones}")
        print(f"Portada del libro: {self.portada}")
        print(f"Autor del libro: {self.autor}")
        print(f"Editorial distribuidora: {self.editorial}")
        print(f"Género literario al que pertenece: {self.genero_literario}")

        def proteger_libro(self):
            print(f"El conductor: {self.conductor} conduce. ")

        def almacenar_información(self):
            print(f"El copiloto: {self.copiloto} apoya al conductor.")

        def corazon_coche(self):
            print(f"El motor: {self.motor} hace que el auto funcione y arranque.")

        def iluminación(self):
            print(f"Las luces: {self.luces} iluminan mejor la carretera.")

        def seguridad_vial(self):
            print(f"El espejo: {self.espejos} ayuda a revisar nuestro entorno.")

redes_cisco = LibroDeBiblioteca("Blanda","Configuración de dispositivos","1-630","10-12","1","Topologías","Redes Cisco","Ernesto Ariganello","Ra-Ma Editorial","Técnico")