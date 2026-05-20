class Alumno:
    def __init__(self, nombre, carrera, cuatrimestre, promedio, matricula, edad, proyecto, asistencia):
     
        self.nombre = nombre
        self.carrera = carrera
        self.cuatrimestre = cuatrimestre
        self.promedio = promedio
        self.matricula = matricula
        self.edad = edad
        self.proyecto = proyecto
        self.asistencia = asistencia

        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Cuatrimestre: {self.cuatrimestre}")
        print(f"Promedio: {self.promedio}")
        print(f"Matrícula: {self.matricula}")
        print(f"Edad: {self.edad}")
        print(f"Proyecto: {self.proyecto}")
        print(f"Asistencia: {self.asistencia}")

        def estudiar(self):
            print(f"El estudiante de {self.carrera} está estudiando para sus exámenes.")

        def entregar_tarea(self):
            print(f"El alumno de {self.cuatrimestre} cuatrimestre está subiendo sus tareas a la plataforma.")

        def tomar_clase(self):
            print(f"El estudiante de {self.edad} años ha entrado a su sesión de programación.")

        def trabajar_integrador(self):
            print(f"El alumno avanza en su proyecto de {self.proyecto} mientras trabaja en equipo.")

        def registrar_asistencia(self):
            print(f"El alumno mantiene su {self.asistencia} gracias a su excelente puntualidad.")

alumno_ti = Alumno("Yuyu","Tecnologías de la Información","Tercer","9.5","TI-2026-01","19","100% de asistencia")
