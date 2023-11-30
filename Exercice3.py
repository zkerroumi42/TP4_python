class Employe:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def __str__(self):
        pass

    def gains(self):
        pass

class Patron(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.salaire = salaire

    def get_salaire(self):
        return self.salaire

    def set_salaire(self, salaire):
        self.salaire = salaire

    def __str__(self):
        return f"Patron: {self.nom} {self.prenom}"

    def gains(self):
        return self.salaire

class TravailleurCommission(Employe):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self.salaire = salaire
        self.commission = commission
        self.quantite = quantite

    def get_salaire(self):
        return self.salaire

    def set_salaire(self, salaire):
        self.salaire = salaire

    def get_commission(self):
        return self.commission

    def set_commission(self, commission):
        self.commission = commission

    def get_quantite(self):
        return self.quantite

    def set_quantite(self, quantite):
        self.quantite = quantite

    def __str__(self):
        return f"Travailleur à la commission: {self.nom} {self.prenom}"

    def gains(self):
        return self.salaire + (self.commission * self.quantite)

class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.retribution = retribution
        self.heures = heures

    def get_retribution(self):
        return self.retribution

    def set_retribution(self, retribution):
        self.retribution = retribution

    def get_heures(self):
        return self.heures

    def set_heures(self, heures):
        self.heures = heures

    def __str__(self):
        return f"Travailleur horaire: {self.nom} {self.prenom}"

    def gains(self):
        return self.retribution * self.heures

# pour tester les classes

p = Patron("Ali", "Allali", 5000)
t_commission = TravailleurCommission("Hamid", "Hamdani", 2000, 0.2, 100)
t_horaire = TravailleurHoraire("Safae", "kabiri", 20, 120)

employes = [p, t_commission, t_horaire]

for employe in employes:
    print(employe)
    print(f"Gains: {employe.gains()}")
