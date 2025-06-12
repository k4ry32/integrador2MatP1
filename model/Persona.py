class Persona:
    def __init__(self, nombre, dni, anio_nacimiento):
        self.nombre = nombre
        self.dni = dni
        self.anio_nacimiento = anio_nacimiento
        self.edad = self.calcularEdad()

    def __str__(self):
        return f"Nombre: {self.nombre} - DNI: {self.dni} - Edad: {self.edad}"

    def calcularEdad(self):
        return 2025 - self.anio_nacimiento