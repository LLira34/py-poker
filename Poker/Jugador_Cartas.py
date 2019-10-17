from Pokar import Pokar

class Jugador_Cartas(Pokar):
    def __init__(self):
        self.jugador=Jugador
    
    def ordenarcartas(self,lista):
        lista.sort(key = lambda x: x.nivel)
        return lista

    def tipojugadas(self,lista):
        Pokar.__init__(self,lista)
        nivel=1
        # Probabilidad para los tipos de jugadas
        prob=0.5
        nom="Carta Alta"

        if self.escalera(3):
            nom="Escalera real"
            nivel=10
            # Probabilidad nivel 10
            prob=0.85
        elif self.escalera(2):
            nom="Escalera de color"
            nivel=9
            # Probabilidad nivel 9
            prob=0.87
        elif self.parejasotrioypokar(4):
            nom="Pokar"
            nivel=8
            # Probabilidad nivel 8
            prob=0.76
        elif self.full():
            nom="Full"
            nivel=7
            # Probabilidad nivel 7
            prob=0.86
        elif self.color():
            nom="Color"
            nivel=6
            # Probabilidad nivel 6
            prob=0.81
        elif self.escalera(1):
            nom="Escalera"
            nivel=5
            # Probabilidad nivel 5
            prob=0.61
        elif self.parejasotrioypokar(3):
            nom="Tercia"
            nivel=4
            # Probabilidad nivel 4
            prob=0.79
        elif self.doblesparejas():
            nom="Dobles Parejas"
            nivel=3
            # Probabilidad nivel 3
            prob=0.53
        elif self.parejasotrioypokar(2):
            nom="Parejas"
            nivel=2
            # Probabilidad nivel 2
            prob=0.42
        return nom,nivel,self.lidic[0]


