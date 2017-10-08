# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:49:18 2017

@author: Alexandre
"""

from math import exp
from random import random
import functions as fn
from time import sleep
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
    #Get function
    def get_temperature(self):
        return self.__temperature
    
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
        
    #Set function
    def set_link_energy(self, link_energy):
        self.__link_energy = link_energy
    
    def set_temperature(self,temperature):
        self.__temperature = temperature
        
    def set_maille(self, maille):
        self.__maille = maille
        
    def set_site_number(self):
        self.__site_number = len(self.__map)
    
    def update_map (self, location, value):
        self.__map[location].set_identity(value)
        self.__map[location].set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
        for x in self.__map[location].get_neighbor():
            x.set_energy(self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
            
        
    def initiate_map (self):
        for x in range (self.__size) :
            for y in range (self.__size):
                for position in self.__maille :
                    self.__map.append(Site((x+position[0],y+position[1]))) 
        self.set_site_number()
        # Neighbor management
        for site in self.__map:
                site.initiate_neighbor(self.__map,self.__size,self.__link_energy[0],self.__link_energy[1],self.__link_energy[2])
        
    def sum_of_energy_init (self):
        for site in self.__map :
            self.__sum_of_energy += site.get_energy()
    #fonction échange de deux sites (avec energy_change_typeelle peut remplacer update_sum_o_energy)
    #à utiliser avec algo temps de résidence
    def exchange(self, site_a, site_b):
        tempo = site_a.get_identity()
        site_a.set_identity(site_b.get_identity())
        site_b.set_identity(tempo)
        A=site_a.energy_change_type(self.__link_energy)
        B=site_b.energy_change_type(self.__link_energy)
        self.__sum_of_energy-= site_a.get_energy() + site_b.get_energy()
        for i in range(len(A)-1):
            self.__sum_of_energy-= i.get_energy()
            i[0].set_energy(i[1])
            self.__sum_of_energy+= i[1]
        for i in range(len(B)-1):
            self.__sum_of_energy-= i.get_energy()
            i[0].set_energy(i[1])
            self.__sum_of_energy+= i[1]
        self.__sum_of_energy+=A[-1]+B[-1]
        
   
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
        
        
    def one_step(self):
        energy_init=self.__sum_of_energy 
        index_a, index_b = fn.site_selection(self.__map)
        self.update_sum_of_energy(self.__map[index_a],self.__map[index_b])
        proba = exp(-(self.__sum_of_energy - energy_init)*11585/(self.__temperature ))#AJOUTER ATTRIBUT K
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
        
    def set_identity(self, identity= bool):
        self.__identity = identity 
    
    def set_neighbor(self, neighbor):
        self.__neighbor = neighbor
        
    def set_energy (self, e_aa, e_ab, e_bb) :
        self.__energy = 0
        if self.__identity:
            for i in self.__neighbor :
                if i.get_identity() :
                    self.__energy += e_bb
                else :
                    self.__energy += e_ab
        else:
            for i in self.__neighbor :
                if i.get_identity() :
                    self.__energy += e_ab
                else :
                    self.__energy += e_aa
                    self.__energy*=0.5
            
    def initiate_neighbor (self, system, size, e_aa, e_ab, e_bb) :
        for i in system :
            if pbc (self, i, size) == [0.5,0.5]:
                self.__neighbor.append(i)
        if len(self.__neighbor)!=4:
            print("Error : bad number of neighbor")
        else :
            self.set_energy(e_aa,e_ab,e_bb)
    
    def get_neighbor (self):
        return self.__neighbor
        
    def get_energy (self):
        return self.__energy

    #cette fonction rend la nouvelle énergie des voisins d'un site si on change le type de celui-ci
    def energy_change_type(self, Link_energy):
        #Link_energy=[eaa,eab,abb]
        energy_site_neghbors=[]
        energy_site=0
        for i in self.neghbor:
            energy_i=i.get_energy()
            if self.__identity!=i.get_identity:
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
            energy_site_neghbors.append([i,energy_i])
        energy_site_neghbors.append(energy_site)
        

    
def pbc (a, b, size) :
    c=[0,0]
    for i in range(2):
        c[i]=min([abs(a.get_coordinate()[i]-b.get_coordinate()[i]),
        abs(a.get_coordinate()[i] - b.get_coordinate()[i] - size),
        abs(a.get_coordinate()[i] - b.get_coordinate()[i] + size)])
    return c