class Universidad:
    def __init__(self, logo, oferta_educativa, localidad, sistema_informatico, modalidad, servicios, ubicacion, talleres, cantidad_salones, rector):

        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informatico = sistema_informatico
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres
        self.cantidad_salones = cantidad_salones
        self.rector = rector

        print(f"Logotipo de la Universidad: {self.logo}")
        print(f"Oferta educativa: {self.oferta_educativa}")
        print(f"Localidad: {self.localidad}")
        print(f"Sistema Informático: {self.sistema_informatico}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Servicios: {self.servicios}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Talleres: {self.talleres}")
        print(f"Cantidad de salones: {self.cantidad_salones}")
        print(f"Nombre del Rector: {self.rector}")

        def mostrar_identidad(self):
            print(f"El logotipo {self.logo} representa la identidad de la institución. ")

        def revisar_carreras(self):
            print(f"La cuenta educativa cuenta actualmente con: {self.oferta_educativa}.")

        def automatizar_procesos(self):
            print(f"El sistema informático {self.sistema_informatico} esta gestionando las calificaciones.")

        def impartir_clases(self):
            print(f"Las clases se estan dictando en la modalida: {self.modalidad}.")

        def dirigir_institucion(self):
            print(f"El rector {self.rector} esta firmando los títulos oficiales.")


unideh = Universidad("logo.jpg", "Ing. software, Turismo alternativo", "San Miguel", "CADU", "Virtual", "Biblioteca digital", "Santa Catarina", None, None, "Octavio Castillo")