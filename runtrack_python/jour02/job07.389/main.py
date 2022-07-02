class Person:
    def __init__(self, Fprenom, Fnom):
        self.prenom = Fprenom
        self.nom = Fnom
        
    def sePresenter(self):
        print(self.prenom, " ", self.nom)
        
        # heritage
class Auteur(Person):
    def __init__(self, prenom, nom, oeuvre):
        super().__init__(prenom, nom)    
        self.oeuvre = oeuvre
    
    def listerOeuvre(self):
        for i in self.oeuvre:
            print(i)
    
    def allOeuvres(self):
        return self.oeuvre
    
    def ecrireUnLivre(self, titre):
        Livre(titre, self)

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        # reference
        auteur.oeuvre.append(self)
    
    def afficherLivre(self):
        print(self.titre)

    def printt(self):
        print(self.titre)

class Bibliotheque:
    def __init__(self, nom, catalogue):
        self.nom = nom
        self.catalogues = catalogue
    
    def acheterLivre(self, auteur, titre, nb):
        li = []
        for book in auteur.oeuvre:
            li.append(book.titre)
        if titre in li:
            self.catalogues[titre] = nb
        else:
            print("Ce livre n'est pas une oeuvre de cet auteur")

    def inventaire(self):
        print(" inventaire biblio ")
        for titre, quantite in self.catalogues.items():
            print(titre, quantite)
    
    def louer(self, client, titre):
        if self.catalogues[titre] > 0:
            client.collection.append(titre)
            self.catalogues[titre] -= 1
        else:
            print("Ce livre n'est plus en stock")
    
    def rendresLivres(self, client):
            for i in client.collection:
                if len(client.collection) != 0:
                    self.catalogues[i] += 1
                    client.collection.remove(i)

class Client(Person):
    def __init__(self, Fprenom, Fnom, collection):
        self.collection = collection
        super().__init__(Fprenom, Fnom)
    
    def inventaire(self):
        for titre in self.collection:
            print(titre)
        
        
A1 = Auteur("leo", "messi", [])
A2 = Auteur("beberrr", "camus", [])
A1.ecrireUnLivre("book1")
A1.ecrireUnLivre("book2")
A2.ecrireUnLivre("la peste")
A2.ecrireUnLivre("l'etranger")
B1 = Bibliotheque('som', {})
B1.acheterLivre(A1, "book1", 1)
B1.acheterLivre(A2, "la peste", 1)
B1.inventaire()

C1 = Client("marwin", 'belga', [])
B1.louer(C1, "la peste")
C1.inventaire()
B1.rendresLivres(C1)
C1.inventaire()
B1.inventaire()

