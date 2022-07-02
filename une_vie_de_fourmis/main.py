import re
import time

import matplotlib.pyplot as plt
import networkx as nx


class Extract_txt:
    def __init__(self, nom_fichier) -> dict:    # --- CONSTRUCTEUR param fichier txt
        self.txt = nom_fichier                  # --- nom fichier txt a parsé
        self.extract = self.parse_txt()         # --- fonction de parsage du txt RETURN dictionnaire F=nF, chemin, et porte/piece
    
    def parse_txt(self):                        # --- FUNCTION de parsage du txt
        all_in_dict = {
        "nF" : 0,
        "all_edges" : [],
        "all_rooms" : {
        }
        }
        nbr_f = 0
        all_edges = []
        all_rooms = []
        txt = open(self.txt, "+r")
        lines = txt.read()
        txt.close()
        lines = re.split(r"\n", lines)

        for i in range(len(lines)):
            if len(lines[i]) == 8 and "-" not in lines[i]:
                nbr = lines[i][5]
                n_room = lines[i][1]
                all_rooms.append((nbr, "S"+str(n_room)))

            if len(lines[i]) == 9 and '{' in lines[i] :
            
                nbr = lines[i][6]
                for x in range(len(lines[i])):

                    if lines[i][x] == "S":
                        first_number = lines[i][x+1]
                        second_number = lines[i][x+2]
                    if (nbr, "S"+str(first_number)+str(second_number)) not in all_rooms:
                        all_rooms.append((nbr, "S"+str(first_number)+str(second_number)))

            if len(lines[i]) == 7:
                    all_edges.append(lines[i])

            if len(lines[i]) == 9 and "{" not in lines[i]:
                    all_edges.append(lines[i])
        
            if len(lines[i]) == 8 and "{" not in lines[i]:
                    all_edges.append(lines[i])

            if lines[i] == "S"+str(i):
                all_rooms.append((str(1), lines[i]))

            for y in range(len(lines[i])):  

                if lines[i][y] == "=":
                    if len(lines[i]) == 4:
                        nbr_f = str(lines[i][ y + 1 ]) + str(lines[i][ y + 2 ])
                    if len(lines[i]) == 3:
                        nbr_f = lines[i][ y + 1 ]

        all_in_dict['nF'] = nbr_f
        all_in_dict['all_rooms'] = all_rooms
        all_in_dict['all_edges'] = all_edges

        return all_in_dict

class Antnest():
    def __init__(self, n_ants, all_rooms, all_edges, num_txt):
        self.all_rooms = all_rooms
        self.n_ants = n_ants
        self.all_edges = all_edges
        self.Sv = "Sv"
        self.start = "Sv"
        self.Sd = "Sd"
        self.num = num_txt
        self.G = self.createGraph()
        self.nodePos
        self.test 

    def createGraph(self):
        G = nx.Graph()
        
        print("")
        print("Soit une fourmilière de " + str(self.n_ants) + " fourmis constituée ainsi:")
        print("")
        self.test = { "Sv" : self.n_ants}
        G.add_node("Sv", key=self.n_ants)
        G.add_node("Sd", key=self.n_ants)
        for room in self.all_rooms:
            self.test.update({room[1] : 0})
            if room[0] == 1:
                G.add_node(room[1], key=str(1))

            else:
                G.add_node(room[1], key=room[0])

        for edge in self.all_edges:
            new = edge.split(" ")
            new.pop(1)
            G.add_edge(new[0], new[1])

        self.test.update({"Sd" : 0})

        # --- zone de print
        print("Affichage des tunnel du nombre de fourmis")
        print("")
        for edge in G.edges:
            print(edge)
        print("")
        # --- zone de print
        
        self.nodePos = nx.spring_layout(G)
        nx.draw(G, self.nodePos, with_labels=True, font_size=8, alpha=0.8, node_color="lightgrey")
        plt.annotate(self.n_ants, xy=self.nodePos.get("Sv"), xytext=(0, 20), textcoords='offset points', bbox=dict(boxstyle="round", fc='red'))
        figure = plt.gcf()
        figure.canvas.manager.set_window_title('Anthill')
        plt.savefig("./fig_"+ self.num +"/anthill.png")
        return G

    def find_best_way(self):
        return [p for p in nx.all_shortest_paths(self.G, source="Sv", target="Sd", method="dijkstra")]

    def calcul_free_place(self, f_actuel, f_voisin):
        
        if int(self.test[f_voisin]) != 0:
            reste =  int(self.test[f_actuel]) - int(self.get_current_capacity_node(f_voisin))
            free_place = int(self.get_current_capacity_node(f_voisin)) + int(self.test[f_voisin])
        
        elif int(self.get_current_capacity_node(f_voisin)) != 1:
            if int(self.test[f_actuel]) <= int(self.get_current_capacity_node(f_voisin)):
                reste = 0
                free_place = int(self.test[f_actuel])
            else:
                reste =  int(self.test[f_actuel]) - int(self.get_current_capacity_node(f_voisin))
                free_place = int(self.test[f_actuel]) - reste
        else:
            reste =  int(self.test[f_actuel]) - int(self.get_current_capacity_node(f_voisin))
            free_place = int(self.test[f_actuel]) - reste

        return reste, free_place

    def get_current_capacity_node(self, node):
        return int(self.G.nodes[node]["key"]) - int(self.test[node])

    def make_move_ants(self):
        i = 0
        s = 0
        actuel = ""
        voisin = ""
        best_path = self.find_best_way()
        list_best_path = best_path[0]
        list_best_path.reverse()

        while True:
            if int(self.test['Sd']) == int(self.G.nodes["Sd"]["key"]): # si toute les fourmis sont dans le dortoir return 
                print("Toutes les fourmits sont dans le dortoir")
                return
            s += 1
            print("+++  E"+str(s)+" +++")
            for i in range(len(list_best_path)):
                 
                if list_best_path[i] == "Sd": continue  # --- Il faut passer "Sd" pour pouvoir jouer avec les index -1 
                
                actuel = list_best_path[i]              # --- Noeud actuel
                voisin = list_best_path[i-1]            # --- Noeud voisins

                if self.test[actuel] != 0:                                  # step One : Si une cellule contient quelques chose

                    if voisin == "Sd":                                      # si le vosin est le dortoir 
                        reste = 0                                           # -1 sur l'avant derniere salle
                        free_place = int(self.test[voisin]) + int(self.test[actuel]) # +1 sur l'avant derniere salle
                    
                    else : 
                        reste, free_place = self.calcul_free_place(actuel, voisin) # sinon calcul nbr fourmit dans l'actuel salle - la capacité actuel de la salle voisine
                
                    # mis a jour de la case initial de la fourmit 
                    plt.annotate(int(reste), xy=self.nodePos.get(actuel), xytext=(0, 20), textcoords='offset points', bbox=dict(boxstyle="round", fc='red'))
                    self.test.update({str(list_best_path[i]) : reste})

                    # mis a jour de l'avancée de la fourmit 
                    plt.annotate(int(free_place), xy=self.nodePos.get(voisin), xytext=(0, 20), textcoords='offset points', bbox=dict(boxstyle="round", fc='red'))
                    self.test.update({str(voisin) : int(free_place)})
                    print("   " + str(actuel) + " - " + str(voisin))
                    print("")
                    PrintG(self.G, s, self.num)

class PrintG:
    def __init__(self, G, step, num) -> None:
        self.G = G
        self.method_print = self.print_graph(step, num)
    
    def print_graph(self, step, num):
        plt.savefig("./fig_"+ num +"/step"+str(step)+".png")
        # plt.draw()
        # plt.clf()  # clear figure from the canvas
        # plt.close()


numero_txt = "cinq"

nom_fichier = "Fourmilieres/fourmiliere_"+ numero_txt +".txt"

data = Extract_txt(nom_fichier)

A = Antnest(data.extract["nF"], data.extract["all_rooms"], data.extract["all_edges"], numero_txt)

A.make_move_ants()


