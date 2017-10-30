# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:10:54 2017

@author: asus
"""
#import module_akmc as mc
import matplotlib.pyplot as plt
from random import randint
from mpl_toolkits.mplot3d import Axes3D

## reverifer les indices
def dicho_search(L,a):
    i=0
    j=len(L)-1
    m=(i+j)//2
    while i < j:
        if a >= L[m] and a<L[m+1]:
            return m
        elif a<L[m]:
            j=m
        else:
            i=m+1
        m=(i+j)//2
    return m

def site_selection (M):
    index_a = randint(0,len(M)-1)
    index_b = randint(0,len(M)-1)
    while M[index_a].get_identity() == M[index_b].get_identity () :
        index_b = randint(0,len(M)-1)
    return index_a, index_b



""" Boucle principale du programme
Permet d'executer plusieurs type d'algorithme de monte-carlo en fonction de la variable entrée
type = 1 -> Temps de résidence naif
type = 2 -> Algorithme métropolis naif
type = 3 -> Algorithme métropolis amélioré
type = 4 -> Temps de résidence amélioré

A terme, cette variable type sera de type string et contiendra le nom de la fonction directement
"""

def monte_carlo(systeme,proportion_b,type_algo,nb_bloc = 10 , scale_affichage =1.25, ite_bloc = 1000000):
    t=0
    nombre_b = int(systeme.get_site_number()*proportion_b)
    L=[]
    T=[]

    # Création du système initial, en changeant une proportion d'individu d'un type a l'autre
    while nombre_b > 0 :
        i = randint(0,systeme.get_site_number()-1) # tirage d'un site au hasard
        if not systeme.get_map()[i].get_identity() :
            nombre_b -= 1
            systeme.update_map(i,True)
    systeme.sum_of_energy_init ()

    # Affichage & enregistrement du système initial
    scale = scale_affichage * systeme.get_size()
    fig = plt.figure(figsize = (scale,scale))
    ax = fig.add_subplot(111, projection='3d')

    file1= open("coordonnee1.txt","w")
    file1.writelines(str(systeme.get_site_number())+"\n")
    file1.writelines("\n")
    for i in systeme.get_map() :
        file1.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identity(), *i.get_coordinate() ) )
    file1.close()
    ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if a.get_identity()],s=20,marker="o",c='r')
    ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if not a.get_identity()],s=20,marker="o",c='b')
    plt.show()



    #Boucle principale par bloc / sous-bloc
    if type_algo == 1:#"residence-time"
        for i in range(nb_bloc):
            for j in range (ite_bloc) :
                t+=systeme.config_choice()
                L.append(systeme.get_sum_of_energy())
                T.append(t)
    elif type_algo == 2:#"metropolis"
        for i in range (nb_bloc):
            for j in range (ite_bloc) :
                t+=10**(-13)
                systeme.one_step()
                L.append(systeme.get_sum_of_energy())
                T.append(t)
    elif type_algo==3:
        for i in range (nb_bloc):
            for j in range (ite_bloc) :
                t+=10**(-13)
                systeme.one_step_1()
                L.append(systeme.get_sum_of_energy())
                T.append(t)
    elif type_algo==4:#nouvelle version de temsp de résidence
            new_sys=systeme.config_choice_init()[-1][-1]
            t=new_sys[-1][-1]
    else:
        print("incorrect type")

# Affichage final
    fig = plt.figure(figsize = (scale,scale))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if a.get_identity()],s=20,marker="o",c='r')
    ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if not a.get_identity()],s=20,marker="o",c='b')
    plt.show()


# Affichage de l'énergie
    plt.plot(T,L)
    plt.xlabel('temps')
    plt.ylabel('energy')
    plt.show()

# Enregistrement du système final
    file2= open("coordonnee2.txt","w")
    file2.writelines(str(systeme.get_site_number())+"\n")
    file2.writelines("\n")
    for i in systeme.get_map() :
        file2.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identity(), *i.get_coordinate() ) )
    file2.close()














