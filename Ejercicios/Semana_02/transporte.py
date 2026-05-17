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

microbus = Transporte("Personas","Conductor","Retrovisor","Cristales","Tela suave","Plástico duro","Estéreo","V6 sxl","37","No")