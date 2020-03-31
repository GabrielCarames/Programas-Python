#Consigna
"""
La rectoria necesita un diagrama de clases que tenga las diferente funcionalidades.
Alumnos, los alumnos tiene nombre apellido legajo , curso , notas y materias que cursa
se quiere saber el promedio de cada materia
Por otro lado la materia que esta compuesta por un nombre y los alumnos que la componen

Bonus:
Se quiere saber cual es el promedio del curso
"""

class Alumnos():
    def __init__(self, legajo, nombre, apellido, curso):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.materiasAlumno = {}

    def mostrarNotaAlumno(self, materia):
        return self.materiasAlumno[materia]
        
    def mostrarInfoAlumno(self):
        print(f"Información del alumno: \nLegajo: {self.legajo}\nNombre: {self.nombre}\nApellido: {self.apellido}\nCurso: {self.curso}")

    def mostrarNotaMateria(self, materia):
            for materia in self.materiasAlumno:
                print(f"La nota de la materia {materia.nombre} del alumno {self.nombre} {self.apellido} es de: {self.materiasAlumno[materia]}")

    def verificarNotasMateria(self):
        for x in self.materiasAlumno:
            if(self.materiasAlumno[x] <= 10 and self.materiasAlumno[x] >= 0):
                return True
            else:
                print("La nota de la materia tiene que estar entre un 0 y un 10 ")
                return False

    def agregarMateriaAlumno(self, materia, nota):
        self.materiasAlumno[materia] = nota

    def promedioAlumno(self):
        notasmateria = 0
        cantidadmaterias = 0
        promedio = 0
        if(self.verificarNotasMateria()):
            for materia in self.materiasAlumno:
                notasmateria = sum(self.materiasAlumno.values())
                cantidadmaterias += 1
            promedio = notasmateria / cantidadmaterias
            print(f"El promedio de todas las materias del alumno es de: {promedio}")
        else:
            print("No hay materias registradas para sacar el promedio")

    def mostrarCreditos(self):
        print("\nAlumno: Gabriel Caramés\nProfesor: Ezequiel Corbalan\nCurso: 6° Computación\nEscuela: Fragata Libertad N°21 DE 10")

class Materias():
    def __init__ (self, nombre):
        self.materias = [nombre]
        self.nombre = nombre
        self.alumnos = []

    def mostrarMaterias(self):
        return self.materias

    def mostrarCantidadMaterias(self, materia):
        return len(materias)

    def agregarAlumno(self, alumno):
        if alumno is not self.alumnos:
            self.alumnos.append(alumno)
        else:
            print("El alumno ya existe")

    def eliminarAlumno(self, alumno):
        if alumno in Alumnos:
            alumnos.removes(alumno)
        else:
            print("El alumno a eliminar no se ha encontrado")

    def promedioMateria(self):
        notasmateria = 0
        self.promedio = 0
        for alumno in self.alumnos:
            notasmateria += alumno.mostrarNotaAlumno(self)
        self.promedio = notasmateria / len(self.alumnos)
        return self.promedio

    def mostrarPromedioMateria(self):
        print(f"El promedio de la materia {self.nombre} es de: {self.promedio}")

    def mostrarAlumnos(self):
        return self.alumnos

class Curso():
    def __init__ (self, nombre):
        self.nombre = nombre
        self.promediosMateria = []
        self.materiasEscuela = []

    def agregarMateria(self, materia):
        self.materiasEscuela.append(materia)

    def agregarPromediosMateria(self, promateria):
        self.promediosMateria.append(promateria)

    def mostrarPromediosMateria(self):
        return promediosMateria

    def promedioCurso(self):
        promedioCurso = 0
        promedioCursoTotal = 0
        for materia in self.materiasEscuela:
            promedioCurso += materia.promedioMateria()
        promedioCursoTotal = promedioCurso / len(self.materiasEscuela)
        print(f"El promedio del curso {self.nombre} es de: {promedioCursoTotal}")
    
#Creación de instancias de los objetos
manuel = Alumnos(0, "Manuel", "Cabral", "Sexto Computacion")
santiago = Alumnos(1, "Santiago", "Fabregas", "Sexto Computacion")
gabriel = Alumnos(2, "Gabriel", "Carames", "Sexto Computacion")
fede = Alumnos(3, "Federico", "Gauna", "Sexto Computacion")
sexto = Curso("Sexto Computacion")
Matematica = Materias("Matematica")
Ingles = Materias("Ingles")
Redes = Materias("Redes")

#Casos de prueba

#Se ingresan a cada alumno sus materias junto a sus notas
santiago.agregarMateriaAlumno(Ingles, 6)
manuel.agregarMateriaAlumno(Ingles, 7)
gabriel.agregarMateriaAlumno(Ingles, 10)
fede.agregarMateriaAlumno(Ingles, 3)
santiago.agregarMateriaAlumno(Matematica,2)
manuel.agregarMateriaAlumno(Matematica, 7)
gabriel.agregarMateriaAlumno(Matematica, 10)
fede.agregarMateriaAlumno(Matematica, 9)
santiago.agregarMateriaAlumno(Redes,8)
manuel.agregarMateriaAlumno(Redes, 6)
gabriel.agregarMateriaAlumno(Redes, 10)
fede.agregarMateriaAlumno(Redes, 5)

#Se le ingresa a cada materia su alumno
Matematica.agregarAlumno(santiago)
Matematica.agregarAlumno(manuel)
Matematica.agregarAlumno(gabriel)
Matematica.agregarAlumno(fede)
Ingles.agregarAlumno(santiago)
Ingles.agregarAlumno(manuel)
Ingles.agregarAlumno(gabriel)
Ingles.agregarAlumno(fede)
Redes.agregarAlumno(santiago)
Redes.agregarAlumno(manuel)
Redes.agregarAlumno(gabriel)
Redes.agregarAlumno(fede)

#Se muestra la información del alumno junto a sus materias y notas
santiago.mostrarInfoAlumno()
santiago.mostrarNotaMateria(Matematica)

#Al curso de sexto se le agrega las materias
sexto.agregarMateria(Matematica)
sexto.agregarMateria(Ingles)
sexto.agregarMateria(Redes)

#Se realizan los promedios de cada materia, se los muestra y luego se hace el promedio total del curso
Matematica.promedioMateria()
Matematica.mostrarPromedioMateria()
Ingles.promedioMateria()
Ingles.mostrarPromedioMateria()
Redes.promedioMateria()
Redes.mostrarPromedioMateria()
sexto.promedioCurso()

#Creditos
gabriel.mostrarCreditos()
