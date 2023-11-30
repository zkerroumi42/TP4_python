class Batiment:
    def __init__(self, adresse):
        self.adresse = adresse

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse

    def __str__(self):
        return f"Batiment({self.adresse})"


class Maison(Batiment):
    def __init__(self, adresse, nbPieces):
        super().__init__(adresse)
        self.nbPieces = nbPieces

    def get_nbPieces(self):
        return self.nbPieces

    def set_nbPieces(self, nbPieces):
        self.nbPieces = nbPieces
        
    def __str__(self):
        return f"Maison({self.adresse}, {self.nbPieces} pièces)"


class Immeuble(Batiment):
    def __init__(self, adresse, nbAppart):
        super().__init__(adresse)
        self.nbAppart = nbAppart

    def get_nbAppart(self):
        return self.nbAppart

    def get_nbAppart(self, nbAppart):
        self.nbAppart = nbAppart
        
    def __str__(self):
        return f"Immeuble({self.adresse}, {self.nbAppart} appartements)"


# pour tester la classe Batiment
b = Batiment("rue de l'eau")
print(b)
print(b.get_adresse())

# pour tester la classe Maison
m = Maison("rue de l'eau", 2)
print(m)
print(m.get_adresse(), m.get_nbPieces())

# pour tester la classe Immeuble
i = Immeuble("rue de l'eau", 2)
print(i)
print(i.get_adresse())
