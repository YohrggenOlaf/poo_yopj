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
            print(f"La Pasta es el recubrimiento protector: {self.pasta}.")

        def almacenar_información(self):
            print(f"EEl contenido muestra la información del libro: {self.contenido}.")

        def separación_contenido(self):
            print(f"Los capítulos separan el contenido: {self.capitulos}")

        def ayuda_visual(self):
            print(f"Las ilustraciones del libro ayuda a entender el contenido: {self.ilustraciones}.")

        def reconocimiento_editorial(self):
            print(f"Es el Autor del libro quien merece el reconocimiento artistico e intelectual: {self.autor}.")

redes_cisco = LibroDeBiblioteca("Blanda","Configuración de dispositivos","1-630","10-12","1","Topologías","Redes Cisco","Ernesto Ariganello","Ra-Ma Editorial","Técnico")