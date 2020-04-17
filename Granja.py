"""
Atención de animales
En un campo hay que atender a los animales, que tienen varias necesidades. Consideremos vacas, gallinas y cerdos, que tienen estas carácterísticas:

Vaca
-Cuando come aumenta el peso en lo que comió / 3 y le da sed.
-Cuando bebe se le va la sed y pierde 500 g de peso.
-Conviene vacunarla una vez, o sea, si no se la vacunó conviene vacunarla, y si ya se la vacunó no conviene volverla a vacunar.
-Tiene hambre si pesa menos de 200 kg.                    
-Cada tanto se la lleva a caminar, en cada caminata pierde 3 kg..

Cerdo
-Cuando come aumenta el peso en lo que comió – 200 g (si come menos de 200 g no aumenta nada); si come más de 1 kg se le va el hambre, si no, no.
-Quiero saber, para cada cerdo, cuánto comió la vez que más comió.
-Siempre conviene vacunarlo.
-Cuando bebe se le va la sed, y le da hambre.
-Si come más de tres veces sin beber le da sed.

Gallina                    
-Cuando come no se observa ningún cambio, siempre pesa 4 kg.
-Siempre tiene hambre, nunca tiene sed, nunca conviene vacunarla.
-Quiero saber, para una gallina, cuántas veces fue a comer.
-Como se ve, importa cuánto come un animal cuando come (excepto para las gallinas), pero no cuánto bebe cuando bebe.

Hay varios dispositivos de atención automática a los animales:
Comederos normales:
-Cada comedero da de comer una cantidad fija que varía para cada comedero.
-Puede atender a los animales con hambre que pesen menos de lo que soporta el comedero, que también es un valor que depende del comedero. 
-Un comedero normal necesita recarga si le quedan menos de 10 raciones, cuando se lo recarga se le cargan 30 raciones.

Comederos inteligente: 
-Le dan de comer a un animal su peso / 100.
-Pueden atender a cualquier animal con hambre. 
-Un comedero inteligente necesita recarga si le quedan menos de 15 kg, al recargarlo se lo lleva hasta su capacidad máxima (que se indica para cada comedero). 

Bebederos:
-Dan de beber a un animal, pueden atender a los animales con sed. 
-Un bebedero necesita recarga cada 20 animales que atiende, 
-Al recargarlo no se registra en el sistema (sí que se lo recarga para volver a contar desde ahí 20 animales atendidos). 

Vacunatorios: 
-Vacunan a un animal
-Pueden atender a los animales que conviene vacunar.
-Un vacunatorio necesita recarga si se queda sin vacunas, al atenderlo se le recargan 50 vacunas.

Una estación de servicio tiene 3 dispositivos de atención automática.

Modelar lo que se describió de forma tal de poder
Saber si un animal puede ser atendido por una estación de servicio; o sea, si se lo puede atender en alguno de sus dispositivos.
Indicar que un animal se atiende en una estación, en este caso se elige un dispositivo al azar que pueda atenderlo, y se lleva al animal a ese dispositivo para que lo atienda. 
Saber para un cerdo cuánto comió la vez que más comió. 
Recargar los dispositivos que necesitan recarga en una estación de servicio.
"""

class Animales(object):
    def __init__(self, id, peso, hambre, sed, vacunado):
        self.id = id
        self.peso = peso
        self.hambre = hambre
        self.sed = sed
        self.vacunado = vacunado
        self.registro = False
        self.registroAlimento = 0
        self.registroAlimentoSinBebida = 0
        self.registroVecesALimentado = 0

    def alimentar(self, gramos):
        self.peso += gramos
 
    def darBeber(self):
        self.sed = False

    def vacunar(self):
        self.vacunado = True
        print(f"El animal de id: {self.id} fué vacunado, su estado de vacunado es de: {self.vacunado}")

class Vaca(Animales):
    def __init__(self, id, peso, hambre, sed , vacunado):
        super().__init__(id, peso, hambre, sed , vacunado)
    
    def alimentar(self, gramos):
        if(self.verifHambre()):
            self.peso += (gramos / 3)
            self.sed = True
            print(f"El animal de id: {self.id}, fue alimentado con {gramos} gramos de comida y su peso actual es de: {self.peso}")
        else:
            print("El animal no tiene hambre")

    def darBeber(self):
        self.peso -= 500
        print(f"El animal de id: {self.id} bebió, su estado de sed es de: {self.sed} y su peso actual es de: {self.peso}")

    def vacunar(self):
        if(self.vacunado == False):
            self.vacunado = True
            self.registro = True
            print(f"El animal de id: {self.id} fué vacunado, su estado de vacunado es de: {self.vacunado}")
        else:
            print("El animal ya fue vacunado anteriormente")
    
    def darCaminata(self):
        self.peso -= 3000
        print(f"El animal de id: {self.id} fué a caminar, y su peso actual es de: {self.peso}")

    def verifHambre(self):
        if(self.peso <= 199999):
            self.hambre = True
            return True

class Cerdo(Animales):
    def __init__(self, id, peso, hambre, sed , vacunado):
        super().__init__(id, peso, hambre, sed , vacunado)
    
    def alimentar(self, gramos):
        if(self.verifAlimento(gramos)):
            self.peso += (gramos - 200)
            self.registroAlimentoSinBebida += 1
            print(f"El animal de id: {self.id}, fue alimentado con {gramos} gramos comida y su peso actual es de: {self.peso}")
            if(self.verifComidasSinBeber()):
                self.sed = True
            if(self.verifVezMasAlimentado(gramos)):
                self.registroAlimento = gramos
        else:
            print(f"El animal de id: {self.id}, fue alimentado con {gramos} y su peso actual es de: {self.peso} debido a que no supero los 200 gramos")
    
    def darBeber(self):
        self.sed = False
        self.Hambre = True
        print(f"El animal de id: {self.id} bebió, su estado de sed es de: {self.sed} y su estado de hambre es de: {self.hambre}")

    def verifAlimento(self, gramos):
        if(gramos <=199):
            return False
        else:
            if(gramos >= 1000):
                self.hambre = False
                return True
            else:
                return True

    def verifVezMasAlimentado(self, gramos):
        if(self.registroAlimento <= gramos):
            return True
    
    def mostrarVezMasAlimentado(self):
        print(f"La vez que el cerdo de id: {self.id}, comió mas alimento es de: {self.registroAlimento}")

    def verifComidasSinBeber(self):
        if(self.registroAlimentoSinBebida >= 3):
            return True

class Gallina(Animales):

    def __init__(self, id, peso, hambre, sed , vacunado):
        super().__init__(id, peso, hambre, sed , vacunado)
    
    def alimentar(self, gramos):
        self.peso = 4000
        self.registroVecesALimentado += 1
        print(f"El animal de id: {self.id}, fue alimentado con {gramos} gramos comida y su peso actual es de: {self.peso}")

    def darBeber(self):
        self.sed = False
        print(f"El animal de id: {self.id} nunca tiene sed")
    
    def vacunar(self):
        if(self.vacunado == False):
            print("No conviene vacunar a la gallina")
    
    def mostrarAlimentosGallina(self):
        print(f"La gallina de id: {self.id}, fué alimentada {self.registroVecesALimentado} veces")

class Estaciones():
    def __init__(self, id):
        self.id = id

class ComederosNormales(Estaciones):
    def __init__(self, id, pesoSoporte, raciones, gramos):
        super().__init__(id)
        self.id = id
        self.pesoSoporte = pesoSoporte
        self.raciones = raciones
        self.gramos = gramos

    def alimentarAnimal(self, animal):
        if(self.verifPeso(animal)):
            animal.alimentar(self.gramos)
            self.raciones -= 1
        else:
            print("El peso del animal supera el peso del soporte o el animal no tiene hambre")

    def recargarEstacion(self):
        if(self.verifRecarga()):
            self.raciones += 30
            print("El comedero se ha recargado")
        else:
            print("La estacion ya cuenta con suficientes raciones")

    def verifPeso(self, animal):
        if(animal.peso <= self.pesoSoporte):
            return True
        else:
            return False

    def verifRecarga(self):
        if(self.raciones <= 9):
            return True
        else:
            return False
    
    def mostrarRaciones(self):
        print(f"La estación de id: {self.id} tiene {self.raciones} raciones")

class ComederosInteligentes(Estaciones):
    def __init__(self, id, pesoSoporte, capacidadMaxima, cantidadAlimento):
        self.id = id
        self.pesoSoporte = pesoSoporte
        self.capacidadMaxima = capacidadMaxima
        self.cantidadAlimento = cantidadAlimento
        self.alimento = 0
    
    def alimentarAnimal(self, animal):
        self.alimento = animal.peso/100
        if(self.verifCantidadAlimento()):
            animal.alimentar(self.alimento)
            self.cantidadAlimento -= self.alimento
        else:
            print("No hay suficiente alimento para alimentar a los animales")

    def recargarEstacion(self):
        if(self.verifRecarga()):
            self.cantidadAlimento = self.capacidadMaxima
            print("El comedero inteligente se ha recargado")
        else:
            print("El comedero aun cuenta con 15kg de alimento")
        
    def verifRecarga(self):
        if(self.capacidadMaxima >= 14999):
            return True
        else: 
            return False

    def verifCantidadAlimento(self):
        if(self.cantidadAlimento >= self.alimento):
            return True
        else:
            return False
    
    def mostrarCantidadAlimento(self):
        print(f"La estación de id: {self.id} tiene {self.cantidadAlimento} gramos de alimento")

class Bebederos(Estaciones):
    def __init__(self, id, bebidas):
        self.id = id
        self.bebidas = bebidas
    
    def darBeberAnimal(self, animal):
        if(self.verificarBebidas()):
            if(self.verifSed(animal)):
                animal.darBeber()
                self.bebidas -= 1
            else:
                print(f"El animal de id: {animal.id}, no tiene sed")
        else:
            print("No hay bebidas disponibles")

    def recargarBebedero(self):
        if(self.bebidas <= 0):
            self.bebidas += 20
            print(f"El bebedero de id: {self.id} se lo recargo con 20 bebidas")
        else:
            print("El bebedero aun cuenta con agua")

    def verifSed(self, animal):
        if(animal.sed == True):
            return True
        else:
            return False
    
    def verificarBebidas(self):
        if(self.bebidas >= 1):
            return True
        else:
            return False
        
    def mostrarBebidas(self):
        print(f"El bebedero de id: {self.id} tiene {self.bebidas} bebidas ")

class Vacunatorios(Estaciones):
    def __init__(self, id, vacunas):
        self.id = id
        self.vacunas = vacunas
    
    def vacunarAnimal(self, animal):
        if(self.verificarVacunas()):
            if(animal.vacunado == False):
                animal.vacunar()
                self.vacunas -= 1
            else:
                print(f"El animal de id: {animal.id}, no conviene vacunarlo")
        else:
            print("No hay mas vacunas disponibles")

    def recargarVacunatorio(self):
        if(self.vacunas == 0):
            self.vacunas = 50
            print(f"El vacunatorio de id: {self.id} fúe recargado con 50 vacunas ")
        else:
            print("El vacunatorio aun tiene vacunas para aplicar")

    def verificarVacunas(self):
        if(self.vacunas >= 1):
            return True
        else:
            return False
    
    def mostrarVacunas(self):
        print(f"El vacunatorio de id: {self.id} tiene {self.vacunas} vacunas ")
#Instancias de objetos
#              (Id, Peso, Hambre, Sed, Vacunado)
vaquita0 = Vaca(0, 180000, True, True, False)
cerdita0 = Cerdo(1, 100000, True, True, False)
gallinita0 = Gallina(2, 2100, True, False, False)
comederonormal0 = ComederosNormales(0, 400000, 5, 3000)
comederointeligente0 = ComederosInteligentes(0 , 5000, 50000, 50000)
bebedorito0 = Bebederos(0, 1)
vacunatorio0 = Vacunatorios(0, 1)
#Se alimenta a cada animal
vaquita0.alimentar(5000)
cerdita0.alimentar(700)
gallinita0.alimentar(20)
#Se da de beber a cada animal
vaquita0.darBeber()
cerdita0.darBeber()
gallinita0.darBeber()
#Se vacuna a cada animal
vaquita0.vacunar()
cerdita0.vacunar()
gallinita0.vacunar()
#Se alimenta a cada animal por medio del comedero normal
comederonormal0.alimentarAnimal(vaquita0)
comederonormal0.alimentarAnimal(cerdita0)
comederonormal0.alimentarAnimal(gallinita0)
#Se muestra y recarga el comedero normal
comederonormal0.mostrarRaciones()
comederonormal0.recargarEstacion()
comederonormal0.mostrarRaciones()
#Se muestra y recarga el comedero normal
comederointeligente0.alimentarAnimal(vaquita0)
comederointeligente0.alimentarAnimal(cerdita0)
comederointeligente0.alimentarAnimal(gallinita0)
#Se muestra y recarga el comedero inteligente
comederointeligente0.mostrarCantidadAlimento()
comederointeligente0.recargarEstacion()
comederointeligente0.mostrarCantidadAlimento()
#Se da de beber a cada animal por medio del bebedero
bebedorito0.darBeberAnimal(vaquita0)
bebedorito0.darBeberAnimal(cerdita0)
bebedorito0.darBeberAnimal(gallinita0)
#Se muestra y recarga el bebedero
bebedorito0.mostrarBebidas()
bebedorito0.recargarBebedero()
bebedorito0.mostrarBebidas()
#Se vacuna a cada animal por medio del vacunatorio
vacunatorio0.vacunarAnimal(vaquita0)
vacunatorio0.vacunarAnimal(cerdita0)
vacunatorio0.vacunarAnimal(gallinita0)
#Se muestra y recarga el vacunatorio
vacunatorio0.mostrarVacunas()
vacunatorio0.recargarVacunatorio()
vacunatorio0.mostrarVacunas()
#Cada animal realiza su acción característica
vaquita0.darCaminata()
cerdita0.mostrarVezMasAlimentado()
gallinita0.mostrarAlimentosGallina()