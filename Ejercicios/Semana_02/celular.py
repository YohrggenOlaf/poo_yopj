class Celular:
    def __init__(self, sistema_operativo, aplicaciones, actualizaciones, configuracion, teclado, pantalla, puertos, camara, memoria, botones):
     
        self.sistema_operativo = sistema_operativo
        self.aplicaciones = aplicaciones
        self.actualizaciones = actualizaciones
        self.configuracion = configuracion
        self.teclado = teclado
        self.pantalla = pantalla
        self.puertos = puertos
        self.camara = camara
        self.memoria = memoria
        self.botones = botones

        print(f"El sistema operativo {self.sistema_operativo} está conectando el hardware con el software.")
        print(f"Ejecutando aplicaciones: {self.aplicaciones}. Son los programas ejecutables del dispositivo.")        
        print(f"Seguimiento de seguridad activo a través del estado de actualizaciones: {self.actualizaciones}.")
        print(f"Accediendo al menú de {self.configuracion} para modificar los parámetros del dispositivo.")       
        print(f"El teclado {self.teclado} nos permite teclear y agregar información de texto.")
        print(f"La pantalla {self.pantalla} permite visualizar todo el contenido multimedia.")
        print(f"Los puertos de tipo {self.puertos} permiten la conexión con otros dispositivos físicos.")
        print(f"La cámara de {self.camara} toma capturas de lo que se le muestra en el entorno.")
        print(f"La memoria {self.memoria} almacena de forma segura la información que se indica.")
        print(f"Los botones de tipo {self.botones} nos permiten cierta interacción física con el equipo.")

mi_celular = Celular("Android 14","WhatsApp, GitHub Mobile, Termux","Al día (Parche de Mayo)","Ajustes del Sistema","Gboard Digital","AMOLED 6.7 pulgadas","USB Type-C","50 Megapíxeles","128 GB NVMe","Volumen y Encendido")
