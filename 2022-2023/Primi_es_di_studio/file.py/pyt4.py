from pyt3 import PartyAnimal

# creo una classe estesa da partyanimal


class CricketFan(PartyAnimal):
    # contatore punti inizializzato a 0
    points = 0
    # funzioene che restituisce 6 punti

    def six(self):
        # aggiungo 6 al contatore
        self.points = self.points + 6
        # chiamo la funzione party estesa da partyanimal
        self.party()
        # stampo il nome, + parola + i punti
        print(self.name, 'points', self.points)


s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
print(dir(j))
