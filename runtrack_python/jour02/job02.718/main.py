class Livre:
    def __init__(self, titre):
        self.titre = titre
        
    def printt(self):
        print(self.titre)
        
        
class Person:
    def __init__(self, Fprenom, Fnom):
        self.prenom = Fprenom
        self.nom = Fnom
        
    def sePresenter(self):
        print(self.prenom, " ", self.nom)


class Auteur(Person):
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        self.oeuvres = []
    
    def listerOeuvre(self):
        for i in self.oeuvres:
            print(i)
    
    def ecrireUnLivre(self, titre):
        self.oeuvres.append(titre)
        return Livre(titre)
    
    
A1 = Auteur("leo", "messi")

L21 = A1.ecrireUnLivre("book21")
L22 = A1.ecrireUnLivre("book22")
L23 = A1.ecrireUnLivre("book23")
L24 = A1.ecrireUnLivre("book24")

L21.printt()
L22.printt()
L23.printt()
L24.printt()

A1.listerOeuvre()

