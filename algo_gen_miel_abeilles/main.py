import random
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
import networkx as nx



"""[Fonction d'extraction de données des fleurs du csv]

    Returns:
        [list]: [liste de tuple fleurs(x, y)]
"""
def parse_dataflower_txt():
    data = pd.read_csv('dataFlower.csv', delimiter=',')
    list_tuples_pos_x_y = []
    for i in range(50):
        list_tuples_pos_x_y.append((data['x'][i], data['y'][i]))
    return list_tuples_pos_x_y


""" [class Abeille representant le déplacement des abeilles(gênes) leurs score de fitness ]

[Attributs : id, genes, score]

    Returns:
        [object]: [Abeille id[int], genes[tuple], score[float]]
"""
class Abeille():
    def __init__(self, id):
        self.id = id
        self.genes = self.__get__first_gene_random(data)
        self.score = self.set_score(self.genes)

    """ Setter id """
    def set_id(self, id):
        self.id = id
    
    """ Setter genes """
    def set_genes(self, genes):
        self.genes = genes
    
    """ Getter genes retourne une list de toutes les genes aléatoirement """
    def __get__first_gene_random(self, data):
        self.__randomize_all_genes()
        list_gene = []
        for tuple in data:
            list_gene.append(tuple)
        return list_gene
    
    """ Setter score donne un score a chaques chemin de gene d'une abeille """
    def set_score(self, all_genes):
        score_fitness = 0
        for i in range(len(all_genes)):
            if i+1 == len(all_genes): 
                self.score = score_fitness
                return self.score
            score = distance.euclidean(all_genes[i], all_genes[i+1])
            score_fitness += score
            
    """ Getter score """
    def get_scores(self):
        return self.score   
    
    """ randomize all genes of list """
    def __randomize_all_genes(self):
        random.shuffle(data)
            
                                 
""" [classe Rûche representant les populations dans la rûche]

[Attributs : iteration, pos, child, population]

    Returns:
        [type]: [description]
"""
class Ruche():
    def __init__(self):
        self.__pos = (500, 500)
        self.pop = [Abeille(i) for i in range(100)]
        self.list_of_average_score_pop = []
        self.average_score_pop = 0
    
    """ méthode de calcule de la moyenne du score de fitnesse de toutes la population """
    def __calcul_average_score_of_pop(self):
        score_mean = 0
        for bee in self.pop:
            score_mean += bee.score
        score = score_mean / 100       
        # print(score)
        self.list_of_average_score_pop.append(score) 
    
    """ méthode de selection des abeilles par un trie de la population par leur score de fitness """
    def get_pop_selection_best_score(self):
        self.__calcul_average_score_of_pop()
        self.pop.sort(key=lambda x: x.score)

    """ méthode de reproduction de la population des 50 meilleurs abeilles  """    
    def crossover(self):
        i = 0
        all_gen_child = []
        
        while i < 60:                                                  # parcourt sur la best partie de la  population d'abeilles           
            y = 0                                                      # on initialise (y) qui incrementera sur les differentes genes 
            max_g1 = 0                                                 # on initialise (max_g1) qui incrementera sur le max de gen du parent 1
            max_g2 = 0                                                 # on initialise (max_g2) qui incrementera sur le max de gen du parent 2
            child_gen = []                                             # liste de gen de l'enfant
            genome_parent1 = self.pop[i].genes                         # on recupere une abeille
            genome_parent2 = self.pop[i+1].genes                       # on recupere une deuxieme abeille
            
            while True:                                                # while True 
                if len(child_gen) == 50:                                    # condition d'arret quand la liste de gen de l'enfant a 50
                    all_gen_child.append(child_gen)
                    break                                                   # break pour sortir de la premiere boucle

                if genome_parent1[y] not in child_gen and max_g1 < 25: # si le gen du parent 1 n'existe pas dans la liste de gen des enfants et qu'il y a moins de 25 gene de ce parent
                    child_gen.append(genome_parent1[y])                # append gene dans liste de gen enfants
                    max_g1 += 1                                        # +1 gene du parent 1

                if genome_parent2[y] not in child_gen and max_g2 < 25: # pareille pour parent 2 
                    child_gen.append(genome_parent2[y])                
                    max_g2 += 1                                        
                
                # print(y)
                y += 1                                                 # fin boucle while True y +1

            i += 2                                                     # fin boucle while sur la pop d'abeilles i +1
            if i == 60:                                                # si i a parcouru toutes la pop d'abeille                                    
                return all_gen_child                                        # retourne list 30 tuple de 50 gene
    
    """ méthode de modification de la population __rée index de tt la pop  __modification des 30 dernieres"""
    def update_new_pop_child(self, gene_child):
        i = 0
        y = 0
        while i < 100:
            if i < 70:  
                Abeille.set_id(self.pop[i], i)
            else:
                Abeille.set_id(self.pop[i], i)
                Abeille.set_genes(self.pop[i], gene_child[y])
                Abeille.set_score(self.pop[i], gene_child[y])
                y += 1
            i += 1

    """ méthode de mutation de la population """
    def mutation(self):
        pass
        # print(self.pop[0].score)
        # print("")
        # i =0
        # for gene in self.pop[0].genes:
            
            # print(gene)
            # i +=1
        # print(self.pop[1].genes)
    
    def parcourt_vizualisation(self):
        G = nx.Graph()
        i=0
        while i <= len(self.pop[0].genes):
            # print(i)
            if i == len(self.pop[0].genes)-1:
                nx.draw(G,pos)
                
                plt.xlabel('x - axis')
                # Set the y axis label of the current axis.
                plt.ylabel('y - axis')
                plt.grid()
                plt.show()
                return
            # print(len(self.pop[0].genes))
            # print(self.pop[0].genes[i])
            # print(self.pop[0].genes[i+1])
            
            G.add_node(i,pos=(self.pop[0].genes[i][0], self.pop[0].genes[i][1]))
            G.add_node(i+1,pos=(self.pop[0].genes[i+1][0], self.pop[0].genes[i+1][1]))
            
            G.add_edge(i, i+1)
            
            pos=nx.get_node_attributes(G,'pos')
            # x = range(0, 1000)
            # y = range(0, 1000)
            
            
            i+=1
        

            
    """ méthode d'optimisation de la population """
    def iteration_of_bee_population(self):
        i = 0
        y = 0
        while True:

            if y == 2:
                return
                            
            if self.average_score_pop == self.list_of_average_score_pop[-1]:           # condition d'arret check l'avant dernier score moyen == le dernier (mutation) 
                self.mutation()
                y += 1
                return
            
            self.average_score_pop = self.list_of_average_score_pop[-1]                 # je mets a jour le score moyen du pour pouvoir checker avec le suivant juste au dessus

            self.get_pop_selection_best_score()                                         # trie sur la population
            
            gene_child = self.crossover()                                               # cross over de la population
            
            self.update_new_pop_child(gene_child)                                       # modifie la list de la pop par 30 enfants et 30 moins bonne
            # print("une iteration de population dessous list des moyennes : "+ str(i))
            i += 1
    
    
    def debug_la_ruche(self):
        pass
        # for bee in self.pop:
            # print(bee.score)
            # print("") 
            # print("") 
    
data = parse_dataflower_txt()

R = Ruche()

R.get_pop_selection_best_score()

gene_child = R.crossover()

R.update_new_pop_child(gene_child)

R.iteration_of_bee_population()

R.parcourt_vizualisation()



        # --- SELECTION ---- #
# -- battle royal 20 par 20 -- #
# best, worse = P.get_selection_via_battle()

# -- 50 meilleurs, 50 moins bon -- #
# best, worse = P.get_pop_selection_best_score()

# print(best, end="")
# child = P.get_child(best)

# reussit a avoir 25 children mtn donné un score et relancé en iteratif avec une mutation quand l'adaptation stagne
# print(child)
# print(len(child))








# ------------- ZONE DE TEST ------------- #

def testingCalcul():
    list_tuples_of_genes = [(761, 772), (273, 105), (708, 99), (444, 428), (897, 324), (371, 429), (549, 329), (862, 361), (278, 434), (796, 310), (684, 273), (964, 726), (328, 489), (501, 287), (98, 711), (2, 897), (837, 787), (758, 405), (3, 517), (116, 69), (724, 631), (528, 794), (704, 995), (951, 209), (189, 739), (494, 898), (938, 646), (898, 898), (45, 549), (436, 619), (901, 639), (508, 31), (929, 389), (345, 560), (921, 964), (493, 970), (573, 903), (628, 311), (276, 666), (908, 534), (220, 307), (330, 410), (875, 407), (643, 404), (101, 482), (602, 68), (730, 742), (213, 639), (774, 130), (437, 601)]
    score_fitness = 0
    for i in range(len(list_tuples_of_genes)):     # --- position x , y actuel + x , y voisin 
        if i+1 == len(list_tuples_of_genes): return score_fitness
        score = distance.euclidean(list_tuples_of_genes[i],list_tuples_of_genes[i+1])
        score_fitness += score

def test_gen():

    list_tuples_of_genes = [(730, 742), (796, 310), (758, 405), (684, 273), (220, 307), (501, 287), (328, 489), (278, 434), (774, 130), (951, 209)]
    list_tuples_of_genes1 = [(758, 405), (730, 742), (951, 209), (796, 310), (684, 273), (220, 307), (501, 287), (774, 130), (278, 434), (328, 489)]


    rendue_attendu = [(730, 742), (758, 405), (796, 310), (951, 209), (684, 273), (220, 307), (684, 273), (501, 287), (774, 130), (278, 434)]
   

    i = 0
    g1 = 0
    g2 = 0
    new_gen = []
    while True:
        
        if len(new_gen) == 10: return new_gen 
        
        genome1 = list_tuples_of_genes[i]
        genome2 = list_tuples_of_genes1[i]

        if genome1 not in new_gen and g1 < 5:
            new_gen.append(genome1)
            g1 += 1
            print(g1)

        if genome2 not in new_gen and g2 < 5:
            new_gen.append(genome2)
            g2 += 1
            print(g2)


        i+=1


# p = test_gen()
# print(p)
# p=testingCalcul()
# print(str(p) + " resultat attendue : 25428.30557650137")
# resultat 2553.479059338494

# ------------- ZONE DE TEST ------------- #
