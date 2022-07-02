import pandas as pd
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# ---------- PROBLEM with file dataFlower link at racine ---------- #
data = pd.read_csv('dataFlower.csv', delimiter=',')
df = pd.DataFrame(data, columns=['x','y'])

#XXXXXXXXXXXXXXXXXXXX--------A FACTORISER----------XXXXXXXXXXXXXXXXXXX
#                   *FAIRE MAX 2 CLASSE (population, crossOver)
#                   *faire plus de fonctions(plus explicite moins de code dans chaques function )
#                   *METTRE TOUT EN ANGLAIS (mettre a jour les variables EXPLICITE)

class Firstselection:
    def __init__(self, id, gene, score):
        self.id = id
        self.gene = gene
        self.score = score

class Newselection:
    def __init__(self, id, gene, score):
        self.id = id
        self.gene = gene
        self.score = score

def getWayRandom():
    posFlower = []
    for q in range(len(df)):
        flower = tuple((df.loc[q]))
        posFlower.append(flower)
    # k = FLOWER GET BY First selection
    randomise = random.sample(posFlower, k=50)
    return randomise

def firstSelection():
    listAbeille = []
    for p in range(100):
        #call class in function WTFFFFF
        gene = getWayRandom()
        listAbeille.append(Firstselection(p, gene, 0))
    return listAbeille

#-------create first pop.--------
def getScore(pop):
    stop = 0
    # list of object FirstSelection whith score
    listAbeille = []
    #boucle W qui parcourt toutes mes abeille
    for w in range(len(pop)):

        # ---------calcule la distance euclidienne----------
        pt_sum_difference = [(x[0] - x[1]) ** 2 for x in pop[w].gene]
        pt_sum = sum(pt_sum_difference)

        #-----------FUCNTION sqrt = racine carre
        distanceEuclidienne = math.sqrt(pt_sum)

        # -------- update la FirstSelection ------------
        listAbeille.append(Firstselection(w, pop[w].gene, distanceEuclidienne))

        stop = stop + 1
        if(stop == 100):
            return listAbeille

def getMoyenne(list):
    scoreMean = np.mean(list)
    return scoreMean

scorePopDestroy = []
def getChild(population):
    separate = 0
    lista = []
    listb = []
    for pop in population:
        #   LIST append for MEAN SCORE
        if separate < 50:
            #print(pop.gene)
            first = tuple((separate, pop.gene, pop.score))
            separate = separate + 1
            lista.append(first)
        else:
            second = tuple((separate, pop.gene, pop.score))
            separate = separate + 1
            listb.append(second)
    m = 100
    listPop = lista + listb
    #print(listMean)
    #--------GET MEAN OF SCORE-------
    newPopulation1 = []
    for z in range(50):
        newGene = []
        newPopulation = []
        for d in range(50):
            if d % 2 == 0:
                newGene.append(lista[z][1][d])
            else:
                newGene.append(listb[z][1][d])
        pt_sum_difference = [(x[0] - x[1]) ** 2 for x in newGene]
        pt_sum = sum(pt_sum_difference)

        # -----------FUCNTION sqrt = racine carre
        distanceEuclidienne = math.sqrt(pt_sum)
        newPopulation = tuple((m, newGene, distanceEuclidienne))
        newPopulation1.append(newPopulation)
        m = m + 1
    listPop = listPop + newPopulation1
    return listPop


#bestPopGene = []
def getBestPopulation(arret, population):
    popDeads = []
    bestPopScore = []
    bestPopGene = []
    population.sort(key=lambda x: x[2])
    for a in range(150):
        if(a < 100):
            bestPopGene.append(population[a][2])
            bestPopScore.append(Newselection(a, population[a][1], population[a][2]))
        else:
            popDeads.append(population[a][2])
        if(a==0):
            pass #POUR RECUPERER LES MEILLEURS GENES DE CHAQUES SELECTION ET FAIRE GRAPH

    # ------------------ GET MEAN OF BESTSCORE & LOSESCORE ------------------
    resultMean = getMoyenne(bestPopGene)
    resultMeanPopDead = getMoyenne(popDeads)
    scorePopDestroy.append(resultMeanPopDead)
    arretrecursive(arret, resultMean, scoreMeans, scorePopDestroy)
    return bestPopScore


scoreMeans = []
def arretrecursive(arret, scoreMean, scoreMeans, scorePopDestroy):
    scoreMeans.append(scoreMean)
    if arret > 2:
        for x in range(len(scoreMeans)):
            temp = scoreMeans[x]
            if temp == scoreMeans[x - 1]:
                xaxis = np.arange(len(scoreMeans))
                xaxis1 = np.arange(len(scorePopDestroy))
                yaxis = scoreMeans
                plt.figure()
                plt.plot(xaxis, yaxis, label='bestScoreMean')
                plt.plot(xaxis1, scorePopDestroy, label='badScoreMean')
                plt.grid()
                plt.legend()
                #naming the x axis
                plt.xlabel('n generation')
                # naming the y axis
                plt.ylabel('Mean score of generations')
                # giving a title to my graph
                plt.title('My first graph!')
                # function to show the plot
                plt.show()
                #   pour second GRAPH DU PARCOURS GENE
                #plt.plot(1, 100)
                #plt.show()
                quit()

def recursive(arret, result):
    if arret == 0:
        #----------FIRST SELECTION
        firstPop = firstSelection()
        firstPopulation = getScore(firstPop)
        population = getChild(firstPopulation)
        resultat = getBestPopulation(arret, population=population)
        arret = arret + 1
        recursive(arret, resultat)
    else:
        #---------OTHER SELECTION--------------------
        population = getChild(result)
        result = getBestPopulation(arret, population)
        #getWayToBestGene(result)
        arret = arret + 1
        recursive(arret, result)

recursive(arret=0, result=[])
