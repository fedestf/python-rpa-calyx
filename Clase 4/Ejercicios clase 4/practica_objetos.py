# Modelar, utilizando clases, la estructura del curso actual.
# Cada clase deberá tener como mínimo 3 métodos
# TIP: Piensen que clases van a necesitar, y cuales pueden aplicar herencia.
# IMPORTANTE: EL EJERCICIO ES MERAMENTE SINTÁCTICO, ES PARA QUE PRACTIQUEN
# COMO SE ESCRIBEN LAS CLASES. Por eso los métodos a definir quedan a elección
# del alumno.


class DatosPersonales:

    def __init__(self, nombre, apellido, edad, dni):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.nombre_completo = nombre+" "+apellido

    def mostrar_nombre_completo(self):

        print(self.nombre_completo)

    def mostrar_dni(self):

        print(self.dni)

    def mostrar_datos_completos(self):

        print(f"{self.nombre_completo}\n {self.edad} \n {self.dni}\n")


class Profesor(DatosPersonales):

    def __init__(self, nombre, apellido, edad, dni, lenguaje):

        DatosPersonales.__init__(self, nombre, apellido, edad, dni)
        self.lenguaje = lenguaje

    def saludar(self):

        print(
            f"Hola chicos los saluda {self.nombre_completo} bienvenidos al curso de {self.lenguaje}")


class Alumno(DatosPersonales):

    def __init__(self, nombre, apellido, edad, dni, legajo, turno):

        DatosPersonales.__init__(self, nombre, apellido, edad, dni)
        self.legajo = legajo
        self.turno = turno

        # Modifico el metodo para que muestre legajo y turno
    def mostrar_datos_completos(self):

        print(
            f"{self.nombre_completo}\n {self.edad} \n {self.dni} \n {self.legajo} \n {self.turno}")

    def saludar(self):

        print(f"El alumno {self.nombre_completo} dice HOLA")


class Curso(Profesor, Alumno):

    def __init__(self, Profesor, Alumno, nombre_curso, horario, modo):

        # (Clase, 'nombre de atributo')
        self.profesor_nombre = getattr(Profesor, 'nombre_completo')
        self.alumno_nombre = getattr(Alumno, 'nombre_completo')
        self.nombre_curso = nombre_curso
        self.horario = horario
        self.modo = modo

    def mostrar_curso(self):

        print(f"{self.nombre_curso}\n {self.horario} \n {self.modo}\n el curso es dictado por: {self.profesor_nombre}\n alumno : {self.alumno_nombre}")


alumno1 = Alumno("Roberto", "Rodriguez", 80, 10254124, "8059-F", "Tarde")
profesor1 = Profesor("Pepe", "Pompin", 80, 8888888, "Python")
curso1 = Curso(profesor1, alumno1, "Calyx Python RPA", "Tarde", "Virtual")

alumno2 = Alumno("Jorge", "testing", 80, 12445, "85055-F", "noche")
profesor2 = Profesor("Olof", "zonic", 80, 000000, "java")
curso2 = Curso(profesor2, alumno2, "TESTEANDO ANDO", "Noche", "Presencial")

curso1.mostrar_curso()
curso2.mostrar_curso()
