class Person():
    def __init__(self, Fprenom, Fnom):
        self.prenom = Fprenom
        self.nom = Fnom
        
    def sePresenter(self):
        print(self.prenom, " ", self.nom)

    def getPrenom(self):
        return self.prenom
    
    def getnom(self):
        return self.nom
    
    def setNom(self, newNom):
        self.nom = newNom
        return self.nom
    
    def setPrenom(self, newPrenom):
        self.prenom = newPrenom
        return self.prenom

P1 = Person("leo", "Messi")
P1.sePresenter()
P1.setNom("ponti")
P1.setPrenom("yaya")
P1.sePresenter()

P2 = Person("thierry", "henry")
P2.sePresenter()
P2.setNom("thierry")
P2.setPrenom("henry")
P2.sePresenter()
