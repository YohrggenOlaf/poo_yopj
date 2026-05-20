class Coche:
    def __init__(self, conductor, copiloto, asientos, motor, luces, espejos, ventanas, mecanica, ruedas, almacenamiento):
        
        self.conductor = conductor
        self.copiloto = copiloto
        self.asientos = asientos
        self.motor = motor
        self.luces = luces
        self.espejos = espejos
        self.ventanas = ventanas
        self.mecanica = mecanica
        self.ruedas = ruedas
        self.almacenamiento = almacenamiento

        print(f"Conductor: {self.conductor}")
        print(f"Copiloto: {self.copiloto}")
        print(f"Asientos: {self.asientos}")
        print(f"Motor: {self.motor}")
        print(f"Luces: {self.luces}")
        print(f"Espejos: {self.espejos}")
        print(f"Ventanas: {self.ventanas}")
        print(f"Mecánica: {self.mecanica}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Almacenamiento: {self.almacenamiento}")

        def conducir_vehiculo(self):
            print(f"El conductor: {self.conductor} conduce. ")

        def auxilio_conductor(self):
            print(f"El copiloto: {self.copiloto} apoya al conductor.")

        def corazon_coche(self):
            print(f"El motor: {self.motor} hace que el auto funcione y arranque.")

        def iluminación(self):
            print(f"Las luces: {self.luces} iluminan mejor la carretera.")

        def seguridad_vial(self):
            print(f"El espejo: {self.espejos} ayuda a revisar nuestro entorno.")

chevrolet = Coche("Ruben","Axel","Piel","V6","LED","Retrovisor","Cristal","Estándar","R17","Amplio")