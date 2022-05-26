from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, deporte, anios):
        super().__init__(nombre, edad, altura, sexo)
        self._deporte = deporte
        self._añosPracticando = anios
        
    def setAñosPracticando(self, anios):
        self._añosPracticando = anios
    
    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self, deporte):
        self._deporte = deporte

    def getDeporte(self):
        return self._deporte