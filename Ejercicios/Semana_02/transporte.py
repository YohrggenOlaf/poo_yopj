class Transporte:
    def __init__(self, pasajeros, chofer, espejos, ventanas, asientos, agarraderas, radio, motor, llantas, cinturon):
       
        self.pasajeros = pasajeros
        self.chofer = chofer
        self.espejos = espejos
        self.ventanas = ventanas
        self.asientos = asientos
        self.agarraderas = agarraderas
        self.radio = radio
        self.motor = motor
        self.llantas = llantas
        self.cinturon = cinturon

        print(f"Pasajeros: {self.pasajeros}")
        print(f"Chofer: {self.chofer}")
        print(f"Espejos: {self.espejos}")
        print(f"Ventanas: {self.ventanas}")
        print(f"Asientos: {self.asientos}")
        print(f"Agarraderas: {self.agarraderas}")
        print(f"Radio: {self.radio}")
        print(f"Motor: {self.motor}")
        print(f"Llantas: {self.llantas}")
        print(f"Cinturón: {self.cinturon}")

        def conducir_vehiculo(self):
            print(f"El conductor: {self.chofer} conduce. ")

        def corazon_coche(self):
            print(f"El motor: {self.motor} hace que el auto funcione y arranque.")

        def seguridad_vial(self):
            print(f"El espejo: {self.espejos} ayuda a revisar nuestro entorno.")

        def mueven_vehiculo(self):
            print(f"Las llantas {self.llantas} ayudan a el desplazamiento.")

        def seguridad(self):
            print(f"El cinturón: {self.cinturon} puede asegurar tu vida.")

microbus = Transporte("Personas","Ejiver","Retrovisor","Cristales","Tela suave","Plástico duro","Estéreo","V6 sxl","37","No")