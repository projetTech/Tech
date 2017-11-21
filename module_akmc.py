# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:49:18 2017

@author: Alexandre
"""

from math import exp
from random import random
import functions as fn
import matplotlib.pyplot as plt

import numpy as np


""" classe interaction
fonction : energie d'interaction entre 2 espèces
"""
"""
class species :
    def __init__(self,diameter,identity="gap"):
        self.__identity= identity
        self.__diameter = diameter
        self.__links_energy =[]
        self.__exchange_species = []

    def get_diameter(self):
        return self.__diameter

    def get_links_energy(self):
        return self.__links_energy

    def get_exchange_species(self):
        return self.__exchange_species

    def get_identity(self):
        return self.__identity

    def set_diameter(self,diameter):
        self.__diameter= diameter

    def set_links_species(self,specie,link_energy):
        self.__links_energy.append(link_energy)
        self.__exchange_species.append(specie)

    def authorized_sites(self,site,size_systeme):
        neighbors = site.get_neighbors()
        distance = []
        for i in neighbors:
            for j in neighbors:
<<<<<<< HEAD
                distance.append(np.linalg.norm(pbc(i,j,size_systeme)))
        return (min(distance) > self.__diameter)

=======
                distance.append(np.linalg.norm(pbc(i,j,size))
        return (min(distance) > self.__diameter) """
        


""" classe espèce
fonction : peut s'échanger avec
fonction : peut aller dans tel site ( gestion de sites intersticiels et autres)
"""


class measure :
    """ Un systeme composé d'une partie du matériau"""
    def __init__(self, number_of_iteration=1000):
        self.__time = []
        self.__energy_of_system = []
        self.__number_of_exchange = []
        self.__rate_of_exchange = []
        self.__number_of_iteration = number_of_iteration


    def print_energy_over_time (self):
        plt.plot( self.__time, self.__energy_of_system)
        plt.xlabel('Time')
        plt.ylabel('Energy')
        plt.title("Energy over time")
        plt.show()

    def save_energy_over_time (self, name="") :
        plt.plot( self.__time, self.__energy_of_system)
        plt.xlabel('Time')
        plt.ylabel('Energy')
        plt.title("Energy over time")
        plt.savefig("Energy_over_time_"+name)

    def increment_exchange (self):
        self.__number_of_exchange += 1
        self.__rate_of_exchange += 1/ self.__number_of_iteration

""" Coefficient de diffusion"""


""" Paramètre d'ordre
Mesure la probabilité dans la boite qu'il y ait un atome de type a à coté d'un atome de type b
Warren coweny
"""





class system :
    """ Un systeme composé d'une partie du matériau"""
    def __init__(self, size, dimension = 3):
        self.__size = size
        self.__dimension = dimension
        self.__maille = []
        self.__sum_of_energy = 0
        self.__map = []
        self.__link_energy =[]
        self.__site_number = 0
        self.__temperature=297
        self.__k_Boltzmann=11585


    #Get functions
    def get_temperature(self):
        return self.__temperature

    def get_dimension (self):
        return self.__dimension

    def get_k_Boltzmann(self):
        return self.__k_Boltzmann

    def get_size(self):
        return self.__size

    def get_link_energy(self):
        return self.__link_energy

    def get_sum_of_energy(self):
        return self.__sum_of_energy

    def get_map (self):
        return self.__map

    def get_maille(self):
        return self.__maille

    def get_site_number (self):
        return self.__site_number

    #Set functions
    def set_link_energy(self, link_energy):
        self.__link_energy = link_energy

    def set_temperature(self,temperature):
        self.__temperature = temperature

    def set_k_Boltzmann(self,k):
        self.__k_Boltzmann = k

    def set_maille(self, maille):
        self.__maille = maille

    def set_site_number(self):
        self.__site_number = len(self.__map)

    #classes' methods
    """cette méthode change l'identité d'un site et met à jour l'énergie du site et de ses voisins
    elle prend en entrée une location et une identité"""
    def update_map (self, location, value):
        self.__map[location].set_identity(value)
        self.__map[location].set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
        for x in self.__map[location].get_neighbor():
            x.set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])


    """Cette serie de fonction permet d'initialiser la carte en créant les sites. La fonction principale (initiate_map1)
    se charge d'appeller la bonne fonction récursive et de generer les voisins une fois que cela est fait
    Il y a beaucoup de fonction: nous aurions pu en mettre qu'une, mais au prix d'un nombre important de condition :
    3 fois le nombre de site total, ainsi que des variables supplémentaires a stocker. Pour éviter cela, coder 3 fonctions
   presques identiques ralonge uniquement la longueur du code, mais pas sa complexité. """
    def initiate_map1 (self, dimension,tab) :
        if dimension == 0:
            for position in self.__maille :
                i=Site((tab[0]+position[0]))
                self.__map.append(i)
        else :
            for i in range (self.__size):
                tab[dimension-1]=i
                self.initiate_map1 ((dimension-1),tab)

    def initiate_map2 (self, dimension,tab) :
        if dimension == 0:
            for position in self.__maille :
                i=Site((tab[0]+position[0],tab[1]+position[1]))
                self.__map.append(i)
        else :
            for i in range (self.__size):
                tab[dimension-1]=i
                self.initiate_map2 ((dimension-1),tab)

    def initiate_map3 (self, dimension,tab) :
        if dimension == 0:
            for position in self.__maille :
                i=Site((tab[0]+position[0],tab[1]+position[1],tab[2]+position[2]))
                self.__map.append(i)
        else :
            for i in range (self.__size):
                tab[dimension-1]=i
                self.initiate_map3 ((dimension-1),tab)

    def initiate_map (self):
        tab_init= [0]*self.__dimension
        test=self.__dimension
        exec("self.initiate_map"+str(test)+" (test, tab_init)")
        self.set_site_number()
        # Neighbor management
        for site in self.__map:
                site.initiate_neighbor(self.__map,self.__size,self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])

    """cette méthode calcule l'energie totale du systeme"""
    def sum_of_energy_init (self):
        for site in self.__map :
            self.__sum_of_energy += site.get_energy()

    def update_sum_of_energy (self, site_a, site_b):
        #Echange des identités des sites
        tempo = site_a.get_identity()
        site_a.set_identity(site_b.get_identity())
        site_b.set_identity(tempo)

        #Actualisation des energies des voisins
        for site in site_a.get_neighbor():
            self.__sum_of_energy-= site.get_energy()
            site.set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
            self.__sum_of_energy+= site.get_energy()

        for site in site_b.get_neighbor():
            self.__sum_of_energy-= site.get_energy()
            site.set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
            self.__sum_of_energy+= site.get_energy()

        #Actualisation des energies des 2 sites
        self.__sum_of_energy-= site_a.get_energy() + site_b.get_energy()
        site_a.set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
        site_b.set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
        self.__sum_of_energy+= site_a.get_energy() + site_b.get_energy()
        

    #cette fonction fait le calcul de la list des proba la première fois
    def config_choice_init(self):
        energy_init=self.__sum_of_energy

        total=0
        stockage_sites_list=[]
        total_energy_sorted=[]
        #initialiser l'indice de parcours de la map
        for i in range(len(self.__map)):
            if self.__map[i].get_identity():#mettre = à une identité si plus de deux identités
                for j in range(4):
                    if((self.__map[i].get_neighbor())[j].get_identity()) != self.__map[i].get_identity() :
                        site1=self.__map[i]
                        site2=(self.__map[i].get_neighbor())[j]
                        if ((site1,site2) not in stockage_sites_list ) and ((site2,site1) not in stockage_sites_list ):
                            new_energy=energy_init
                            for site3 in site1.get_neighbor():
                                if site3 != site2:
                                    #chaque energie de liaisons se compte deux fois dans l'energy totale
                                    new_energy -= 2*fn.get_link_energy(self.__link_energy,site3,site1)
                                    new_energy += 2*fn.get_link_energy(self.__link_energy,site3,site2)
                            for site3 in site2.get_neighbor():
                                if site3 != site1:
                                    new_energy -= 2*fn.get_link_energy(self.__link_energy,site3,site2)
                                    new_energy += 2*fn.get_link_energy(self.__link_energy,site3,site1)
                            total += exp(-(new_energy - energy_init)*self.__k_Boltzmann/(self.__temperature))
                            stockage_sites_list.append((site1,site2))
                            total_energy_sorted.append(total)



        r=random()*total
        picked=fn.dicho_search(total_energy_sorted,r)
        self.update_sum_of_energy(stockage_sites_list[picked][0],stockage_sites_list[picked][1])
        
        couple=stockage_sites_list[picked]
        stockage_sites_list.remove(stockage_sites_list[picked])
        if picked!=0:
            energy_exchange = total_energy_sorted[picked]-total_energy_sorted[picked-1]
        else: 
            energy_exchange = total_energy_sorted[picked]
        if picked !=len(total_energy_sorted)-1 : 
            for l in range(picked+1,len(total_energy_sorted)):
                total_energy_sorted[l] -=energy_exchange
            
        total_energy_sorted.remove(total_energy_sorted[picked])
        
        return([couple,stockage_sites_list,total_energy_sorted])




    #elle donne le prochain pas à partir de la connaissance du dernier pas et de la liste des proba
    def config_choice_rec(self,couple_changed,stockage_sites_list,total_energy_sorted): #couple_changed=numbers_sites[i] obtenu avec la fonction précédente
        #je mets à jour ma liste de proba classé et de sites correspondants. le but est de ne pas tout recalculé vus que le nombre de proba qui change ne dépasse pas 8
        energy_init=self.__sum_of_energy
        A=couple_changed[0].get_neighbor()
        B=couple_changed[1].get_neighbor()
        #voisins de couple[0] sont les anciens voisins du couple[1] 
        #j'enlève les anciens potentiels changeables couples de voisins pour l'ancien couple_changed[1]
        for i in range(len(A)):
             #QUAND on echange deux sites on échange juste leur identité et on modifie leurs energies 
            #enlever toutes les proba d'échange des sites échangés avec eurs voisins dans la config précedente
            #s'ils étaient d'identités différentes 
            if couple_changed[1].get_identity() != A[i].get_identity(): 
                #retourne l'indice de l'ancien couple dans la liste
                if (couple_changed[0],A[i]) in stockage_sites_list:
                    j=stockage_sites_list.index((couple_changed[0],A[i]))
                elif (A[i],couple_changed[0]) in stockage_sites_list:
                    j=stockage_sites_list.index((A[i],couple_changed[0]))
                else:
                    j=None 
                #enlever toutes les proba d'échange concernant la config précedente 
                if j != None:
                    stockage_sites_list.remove(stockage_sites_list[j])
                    if j != 0:
                        proba_exchange_done=total_energy_sorted[j]-total_energy_sorted[j-1]
                    else:
                        proba_exchange_done=total_energy_sorted[j]
                    if j != len(total_energy_sorted)-1:
                        for k in range(j+1,len(total_energy_sorted)):
                            total_energy_sorted[k]-=proba_exchange_done
                    total_energy_sorted.remove(total_energy_sorted[j])
                        
        for i in range(len(B)):
             if couple_changed[0].get_identity() != B[i].get_identity(): #j'enlève les anciens potentiels changeables couples de voisins 
                #retourne l'indice de l'ancien couple dans la liste
                if (couple_changed[1],B[i]) in stockage_sites_list:
                    j=stockage_sites_list.index((couple_changed[1],B[i]))
                elif (B[i],couple_changed[1]) in stockage_sites_list:
                    j=stockage_sites_list.index((B[i],couple_changed[1]))
                else:
                    j= None
                    
                if j!= None:
                #enlever toutes les proba d'échange concernant la config précedente 
                    stockage_sites_list.remove(stockage_sites_list[j])
                    if j != 0:
                        proba_exchange_done=total_energy_sorted[j]-total_energy_sorted[j-1]
                    else:
                        proba_exchange_done = total_energy_sorted[j]
                    if j != len(total_energy_sorted)-1:
                        for k in range(j+1,len(total_energy_sorted)):
                            total_energy_sorted[k]-=proba_exchange_done
                    total_energy_sorted.remove(total_energy_sorted[j])
                 
        #ajouter les nouveaux echanges 
        for i in range(len(A)):
            #ajouter les nouveaux echanges pour couple_change[0]
            if couple_changed[0].get_identity() != A[i].get_identity():
                if ((couple_changed[0],A[i]) not in stockage_sites_list ) and ((A[i],couple_changed[0]) not in stockage_sites_list ):
                    new_energy=energy_init
                    total=total_energy_sorted[-1]
                    #on calculera l'energie d'échange de A[i] et de couple_changed[0], les voisins de couple_changed[0] sont A
                    for site3 in A:
                        if site3 != A[i]:
                            new_energy -= 2*fn.get_link_energy(self.__link_energy,site3,couple_changed[0])
                            new_energy += 2*fn.get_link_energy(self.__link_energy,site3,A[i])
                    for site3 in A[i].get_neighbor():
                        if site3 != couple_changed[0]:
                            new_energy -= 2*fn.get_link_energy(self.__link_energy,site3,A[i])
                            new_energy += 2*fn.get_link_energy(self.__link_energy,site3,couple_changed[0])
                    total += exp(-(new_energy - energy_init)*self.__k_Boltzmann/(self.__temperature))
                    stockage_sites_list.append((couple_changed[0],A[i]))
                    total_energy_sorted.append(total)

            #ajouter les nouveaux echanges pour couple_change[1]
            if couple_changed[1].get_identity() != B[i].get_identity():
                #je calcul l'energy d'échange de couple_changed[1] et B[i]
                if ((couple_changed[1],B[i]) not in stockage_sites_list ) and ((B[i],couple_changed[1]) not in stockage_sites_list ):
                    new_energy=energy_init
                    total=total_energy_sorted[-1]
                    for site3 in B:
                        if site3 != B[i]:
                            new_energy -= 2*fn.get_link_energy(self.__link_energy,site3,couple_changed[1])
                            new_energy += 2*fn.get_link_energy(self.__link_energy,site3,B[i])
                    for site3 in B[i].get_neighbor():
                        if site3 != couple_changed[1]:
                            new_energy -= 2*fn.get_link_energy(self.__link_energy,site3,B[i])
                            new_energy += 2*fn.get_link_energy(self.__link_energy,site3,couple_changed[1])
                    total += exp(-(new_energy - energy_init)*self.__k_Boltzmann/(self.__temperature))
                    stockage_sites_list.append((couple_changed[1],B[i]))
                    total_energy_sorted.append(total)

        r=random()*total_energy_sorted[-1]
        picked=fn.dicho_search(total_energy_sorted,r)
        self.update_sum_of_energy(stockage_sites_list[picked][0],stockage_sites_list[picked][1])
        couple=stockage_sites_list[picked]
        stockage_sites_list.remove(stockage_sites_list[picked])
        if picked!=0:
            energy_exchange = total_energy_sorted[picked]-total_energy_sorted[picked-1]
        else: 
            energy_exchange = total_energy_sorted[picked]
        if picked != len(total_energy_sorted)-1:
            for l in range(picked+1,len(total_energy_sorted)):
                total_energy_sorted[l] -=energy_exchange        
        total_energy_sorted.remove(total_energy_sorted[picked])    
        return([couple,stockage_sites_list,total_energy_sorted])



    def one_step(self):
        energy_init=self.__sum_of_energy
        index_a, index_b = fn.site_selection(self.__map)
        self.update_sum_of_energy(self.__map[index_a],self.__map[index_b])
        proba = exp(-(self.__sum_of_energy - energy_init)*self.__k_Boltzmann/(self.__temperature ))#AJOUTER ATTRIBUT K
        if random() > proba:
            self.update_sum_of_energy(self.__map[index_a],self.__map[index_b])




class Site:
    """Un site du systeme"""
    def __init__(self, coordinate= tuple):
        self.__coordinate = coordinate # coordinate of the site
        self.__identity = False # type of atom in this site
        self.__neighbor = []
        self.__energy = None # local energy of this site



    def get_identity(self):
        return self.__identity

    def get_coordinate(self):
        return self.__coordinate

    def get_neighbor(self):
        return self.__neighbor

    def get_energy (self):
        return self.__energy

    def set_identity(self, identity= int):
        self.__identity = identity

    def set_neighbor(self, neighbor):
        self.__neighbor = neighbor

    def set_energy1(self,energy):
        self.__energy=energy

    def set_energy (self, e_aa, e_ab, e_bb) :
        self.__energy = 0
        if self.__identity:
            for i in self.__neighbor :
                if i.get_identity():
                    self.__energy += e_bb
                else : # Arbitraire, a changer
                    self.__energy += e_ab
        else:
            for i in self.__neighbor :
                if i.get_identity() :
                    self.__energy += e_ab
                else :
                    self.__energy += e_aa
                    self.__energy*=0.5

    def set_energy_2 (self, energy_of_link) :
        for i in self.__neighbor :
            self.__energy += energy_of_link[self.get_identity()][i.get_identity()]


    def initiate_neighbor (self, system, size, e_aa, e_ab, e_bb) :
        for i in system :
            if pbc (self, i, size) == [0.5]*len(self.get_coordinate()):
                self.__neighbor.append(i)
        self.set_energy(e_aa,e_ab,e_bb)




    #cette fonction rend la nouvelle énergie de chaque voisin d'un site si on change son type
    def energy_change_type(self, Link_energy):
        #Link_energy=[eaa,eab,abb]
        list_energy=[]
        energy_site=0
        for i in self.__neighbor:
            energy_i=i.get_energy()
            if self.__identity!=i.get_identity():
                if self.__identity:
                    energy_site+=Link_energy[0]
                    energy_i+= Link_energy[0]-Link_energy[1]
                else:
                    energy_site+=Link_energy[2]
                    energy_i+=Link_energy[2]-Link_energy[1]
            else:
                energy_site+=Link_energy[1]
                if self.__identity:
                    energy_i+= Link_energy[1]-Link_energy[2]
                else:
                    energy_i+=Link_energy[1]-Link_energy[0]
            list_energy.append([i,energy_i])
        list_energy.append(energy_site)
        return list_energy


def pbc (a, b, size) :
    c=[0]*len(a.get_coordinate())
    for i in range(len(c)):
        c[i]=min([abs(a.get_coordinate()[i]-b.get_coordinate()[i]),
        abs(a.get_coordinate()[i] - b.get_coordinate()[i] - size),
        abs(a.get_coordinate()[i] - b.get_coordinate()[i] + size)])
    return c

