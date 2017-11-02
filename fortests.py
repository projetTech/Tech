# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:19:16 2017

@author: asus
"""

"""for tests"""
import matplotlib.pyplot as plt 
from random import randint
import module_akmc as mc 
#dicho_search OK
def dicho_search(L,a):
    i=0
    j=len(L)-1
    m=(i+j)//2
    while i < j:
        if a > L[m] and a<=L[m+1]:
            return m+1
        elif a<=L[m]:
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

#get_link_energy OK 
def get_link_energy(List_of_links,siteA,siteB):
    #list_of_links=[eaa,eab,ebb]
    if siteB.get_identity()==siteA.get_identity():
        if siteB.get_identity():
            return List_of_links[2]
        else:
            return List_of_links[0]
    else:
        return List_of_links[1]
    
n=1000
size = 4
e_aa = 0
e_ab = 0.21
e_bb = 0
list_of_links=[e_aa,e_ab,e_bb]
proportion_b = 0.5
Temperature=297 #EN kelvin

systeme = mc.system (size)
systeme.set_maille([(0,0),(0.5,0.5)])
systeme.set_link_energy(list_of_links)
systeme.initiate_map ()
#la map contient que des A

plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],s=100,marker="o",c='r')		    
plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],s=100,marker="o",c='b')		    
plt.show()  

#créer des B 

nombre_b = int(systeme.get_site_number()*proportion_b)
while nombre_b > 0 :
        i = randint(0,systeme.get_site_number()-1) # tirage d'un site au hasard
        if not systeme.get_map()[i].get_identity() : #
            nombre_b -= 1
            systeme.update_map(i,True)

systeme.sum_of_energy_init ()
plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],s=100,marker="o",c='r')		    
plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],s=100,marker="o",c='b')		    
plt.show() 
energy_init=systeme.get_sum_of_energy()

#OK pour le calcul d'energie en retirant et ajoutant 2* l'energie de liaisons à chaque fois
new_sys=systeme.config_choice_init()
new=systeme.get_sum_of_energy()
T=[]
L=[]
t=0
L.append(systeme.get_sum_of_energy())
T.append(t)
t+=1/new_sys[-1][-1]#total_energy_sorted[-1]
T.append(t)
L.append(systeme.get_sum_of_energy())

new_sys=systeme.config_choice_rec(new_sys[0],new_sys[1],new_sys[2])





