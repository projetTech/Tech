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
class species :
    def __init__(self,identity="gap",diameter):
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
                distance.append(np.linalg.norm(pbc(i,j,size))
        return (min(distance) > self.__diameter) 
        
               

        

        
        
        

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
    def __init__(self, size):
        self.__size = size 
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
    def update_map (self, location, value):
        self.__map[location].set_identity(value)
        self.__map[location].set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
        for x in self.__map[location].get_neighbor():
            x.set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
            
            
#Utiliser des fonctions recursives pour gérer le problème du nombre de boucle for   
   
    def initiate_map (self):
        for x in range (self.__size) :
            for y in range (self.__size):
                for z in range (self.__size) :
                    for position in self.__maille :
                        i=Site((x+position[0],y+position[1],z+position[2]))
                        self.__map.append(i) 

        self.set_site_number()
        # Neighbor management
        for site in self.__map:
                site.initiate_neighbor(self.__map,self.__size,self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
        
    def sum_of_energy_init (self):
        for site in self.__map :
            self.__sum_of_energy += site.get_energy()
    #fonction échange de deux sites (avec energy_change_typeelle peut remplacer update_sum_o_energy)
    #à utiliser avec algo temps de résidence
            
    def exchange(self, site_a, site_b):#to exchange two sites, we have to exchange their identities and update sites' energy 
        #exchanging identities
        tempo = site_a.get_identity()
        site_a.set_identity(site_b.get_identity())
        site_b.set_identity(tempo)
        
        #getting the new vector of site's and neighbors energy for each site
        A=site_a.energy_change_type(self.__link_energy)
        B=site_b.energy_change_type(self.__link_energy)
        #updating the energy of each site and its neighbors
        self.__sum_of_energy -= site_a.get_energy() + site_b.get_energy()
        for i in range(len(A)-1):
            self.__sum_of_energy-= A[i][0].get_energy()-A[i][1]
            A[i][0].set_energy1(A[i][1])
        for i in range(len(B)-1):
            self.__sum_of_energy-= B[i][0].get_energy()- B[i][1]
            B[i][0].set_energy1(B[i][1])
        self.__sum_of_energy+=A[-1]+B[-1]
        site_a.set_energy1(A[-1])
        site_b.set_energy1(B[-1])
        
   
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
        for site1 in self.__map:
            if site1.get_identity():
                for site2 in site1.get_neighbor():
                    if site2.get_identity()!=site1.get_identity():
                        #pour être certain de ne pas citer un couple deux fois 
                        if ((site1,site2) not in stockage_sites_list ) and ((site2,site1) not in stockage_sites_list ):
                            A=site1.energy_change_type(self.__link_energy)
                            B=site2.energy_change_type(self.__link_energy)
                            new_energy=energy_init
                            for i in range(len(A)-1):
                                new_energy-=A[i][0].get_energy()+B[i][0].get_energy()-B[i][1]-A[i][1]
                            new_energy-=site1.get_energy()+site2.get_energy()-A[-1]-B[-1]
                            total+=exp(-(new_energy - energy_init)*11585/(self.__temperature))                   
                            stockage_sites_list.append((site1,site2))
                            total_energy_sorted.append(total)
        r=random()*total
        i=fn.dicho_search(total_energy_sorted,r)
        self.exchange(stockage_sites_list[i][0],stockage_sites_list[i][1])
        return([stockage_sites_list[i],stockage_sites_list,total_energy_sorted])
    
    #elle donne le prochain pas à partir de la connaissance du dernier pas et de la liste des proba
    def config_choice_rec(self,couple_changed,stockage_sites_list,total_energy_sorted): #couple_changed=numbers_sites[i] obtenu avec la fonction précédente
        #je mets à jour ma liste de proba classé et de sites correspondants. le but est de ne pas tout recalculé vus que le nombre de proba qui change ne dépasse pas 8  
        energy_init=self.__sum_of_energy
        A=couple_changed[0].get_neighbor()
        B=couple_changed[1].get_neighbor()
        for i in range(len(A)):
            #s'ils étaient d'identités différentes 
            if couple_changed[0].get_identity() != A[i].get_identity(): #j'enlève les anciens potentiels changeables couples de voisins 
                j=stockage_sites_list.find((couple_changed[0],A[i]))+1+stockage_sites_list.find((A[i],couple_changed[0]))# s'il ne trouve pas le premier couple il renvoie -1, mais il trouvera certainement le 2
                #enlever tous la proba de l'échange fait aux sommes des proba qui suivent dans la liste
                
                stockage_sites_list.remove(j)
                if j!=0:
                    proba_exchange_done=total_energy_sorted[j]-total_energy_sorted[j-1]
                else: 
                    proba_exchange_done=total_energy_sorted[j]
                for k in range(j+1,len(total_energy_sorted)):
                    total_energy_sorted[k]-=proba_exchange_done
                total_energy_sorted.remove(j)
            else:
                #on calcul proba d'échange on l'ajoute à total et on le met à la fin de la list des proba classées
                #s'ils sont devenu d'identité différentes j'ajoute leur proba d'échange
                C=couple_changed[0].energy_change_type(self.__link_energy)
                D=A[i].energy_change_type(self.__link_energy)
                new_energy=energy_init
                for i in range(len(C)-1):
                    new_energy-=C[i][0].get_energy()+B[i][0].get_energy()-D[i][1]-C[i][1]
                new_energy-=couple_changed[0].get_energy()+A[i].get_energy()-C[-1]-D[-1]
                total=exp(-(new_energy - energy_init)*11585/(self.__temperature))+total_energy_sorted[-1]
                total_energy_sorted.append(total)
                stockage_sites_list.append((couple_changed[0],A[i]))
            #le choix de l'échange à effectuer
        r=random()*total
        i=fn.dicho_search(total_energy_sorted,r)
        self.exchange(stockage_sites_list[i][0][0],stockage_sites_list[i][1][0])
        return([stockage_sites_list[i],stockage_sites_list,total_energy_sorted])
    
    def config_choice(self):
        energy_init=self.__sum_of_energy #l'énergie de la configuration initiale / self. ... à verifier la synthaxe 
        total=0
        stockage_sites_list=[]
        total_energy_sorted=[]
        for site1 in self.__map:
            if site1.get_identity():
                for site2 in site1.get_neighbor():
                    #if not site2.get_identity():
                    if True :
                        self.update_sum_of_energy(site1,site2)
                        total+=exp(-(self.__sum_of_energy - energy_init)*11585/(self.__temperature))
                        stockage_sites_list.append((site1,site2))
                        total_energy_sorted.append(total)
                        self.update_sum_of_energy(site1,site2)
        r=random()*total
        i=fn.dicho_search(total_energy_sorted,r)
        self.update_sum_of_energy(stockage_sites_list[i][0],stockage_sites_list[i][1])
        return total_energy_sorted[-1]
    #one_step en utilisant deux fonctions aux lieux de update   
    def one_step_1(self):
        energy_init=self.__sum_of_energy 
        index_a, index_b = fn.site_selection(self.__map)
        A=self.__map[index_a].energy_change_type(self.__link_energy)
        B=self.__map[index_b].energy_change_type(self.__link_energy)
        energy_if_exchange=energy_init
        energy_if_exchange -= self.__map[index_a].get_energy() + self.__map[index_b].get_energy()
        for i in range(len(A)-1):
            energy_if_exchange-= A[i][0].get_energy()-A[i][1]
        for i in range(len(B)-1):
             energy_if_exchange-= B[i][0].get_energy()-B[i][1]
        energy_if_exchange+=A[-1]+B[-1]
        proba = exp(-(energy_if_exchange - energy_init)*self.__k_Boltzmann/(self.__temperature ))#AJOUTER ATTRIBUT K
        if random() <= proba:
            self.exchange(self.__map[index_a],self.__map[index_b])
          
        
    def one_step(self):
        energy_init=self.__sum_of_energy 
        index_a, index_b = fn.site_selection(self.__map)
        self.update_sum_of_energy(self.__map[index_a],self.__map[index_b])
        proba = exp(-(self.__sum_of_energy - energy_init)*self.__k_Boltzmann/(self.__temperature ))#AJOUTER ATTRIBUT K
        if random() > proba:
            self.update_sum_of_energy(self.__map[index_a],self.__map[index_b])
        

                
############## FILE AKMC_func.py
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
            if pbc (self, i, size) == [0.5,0.5,0.5]:
                self.__neighbor.append(i)
        if len(self.__neighbor)!=8:
            print("Error : bad number of neighbor")
        else :
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
    c=[0,0,0]
    for i in range(3):
        c[i]=min([abs(a.get_coordinate()[i]-b.get_coordinate()[i]),
        abs(a.get_coordinate()[i] - b.get_coordinate()[i] - size),
        abs(a.get_coordinate()[i] - b.get_coordinate()[i] + size)])
    return c

 