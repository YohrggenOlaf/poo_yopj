class Silla:
        def __init__(self,forma_asiento, altura, textura, color, material, dureza, forma_respaldo, ensamble, estilo, antiguedad):
                
                self.forma = forma_asiento
                self.altura = altura
                self.textura = textura
                self.color = color
                self.material = material
                self.dureza = dureza
                self.respaldo = forma_respaldo
                self.ensamble = ensamble
                self.estilo = estilo
                self.antiguedad = antiguedad

                print(f"La forma del asiento es: {forma_asiento}")
                print(f"La altura de la silla es: {altura}")
                print(f"La textura de la silla es: {textura}")
                print(f"El color de la silla es: {color}")
                print(f"La silla esta hecha de: {material}")
                print(f"La silla cuenta con el siguiente valor de dureza: {dureza}")
                print(f"La forma del respaldo es: {forma_respaldo}")
                print(f"La silla esta ensamblada con: {ensamble}")
                print(f"La silla tiene un estilo: {estilo}")
                print(f"La silla tiene una antiguedad de: {antiguedad}")

mi_gamer = Silla("Rectangular","35 cm","Terciopelo","Guinda","Madera","30–40 ILD","Ovaldado","Tornillos","Rustica","6 meses")
