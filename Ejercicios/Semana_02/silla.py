class Silla:
    def __init__(self,forma_asiento, altura, textura, color, material, dureza, respaldo, ensamble, estilo, antiguedad):
                
        self.forma = forma_asiento
        self.altura = altura
        self.textura = textura
        self.color = color
        self.material = material
        self.dureza = dureza
        self.respaldo = respaldo
        self.ensamble = ensamble
        self.estilo = estilo
        self.antiguedad = antiguedad

        print(f"La forma del asiento es: {self.forma_asiento}")
        print(f"La altura de la silla es: {self.altura}")    
        print(f"El color de la silla es: {self.color}")
        print(f"La silla esta hecha de: {self.material}")
        print(f"La silla cuenta con el siguiente valor de dureza: {self.dureza}")
        print(f"La forma del respaldo es: {self.respaldo}")
        print(f"La silla esta ensamblada con: {self.ensamble}")
        print(f"La silla tiene un estilo: {self.estilo}")
        print(f"La silla tiene una antiguedad de: {self.antiguedad}")

        def soportar_peso(self):
            print(f"La silla de material {self.material} esta soportando de una persona")

        def brindar_confort(self):
            print(f"El asiento de forma {self.respaldo} con textura {self.textuta} es muy comodo.")

        def reclinar_respaldo(self):
            print(f"El respaldo con forma {self.respaldo} se adapta bien a la espalda.")

        def verificar_desgaste(self):
            print(f"Por su antigüedad de {self.antiguedad}, se revida si el ensamble con {self.ensamble} requiere un ajuste.")

        def decorar_espacio(self):
            print(f"La silla de color {self.color} y estilo {self.estilo} combina con la sala.")


mi_gamer = Silla("Rectangular","35 cm","Terciopelo","Guinda","Madera","30–40 ILD","Ovaldado","Tornillos","Rustica","6 meses")
