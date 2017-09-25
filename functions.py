# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:10:54 2017

@author: asus
"""
#import module_akmc as mc
from random import randint
## reverifer les indices
def dicho_search(L,a):
    i=0
    j=len(L)-1
    m=(i+j)//2
    while i < j:
        if a > L[m] and a<=L[m+1]:
            return m
        elif a<=L[m]:
            j=m
        else:
            i=m
        m=(i+j)//2
    return i
            
def site_selection (M,size):
    index_a = randint(0,size-1)
    index_b = randint(0,size-1)
    while M[index_a].get_identity() == M[index_b].get_identity () :
        index_b = randint(0,size-1)
    return index_a, index_b

            
def monte_carlo(systeme,proportion_b,type_algo,n):
    t=0
    nombre_b = int(systeme.get_site_number()*proportion_b)
    
    while nombre_b > 0 :
        n = randint(0,systeme.get_site_number()-1) # tirage d'un site au hasard
        if not systeme.get_map()[n].get_identity() : #
            nombre_b -= 1
            systeme.update_map(n,True)
    
    file1= open("coordonnee1.txt","w")
    file1.writelines(str(systeme.get_site_number())+"\n")
    file1.writelines("\n")
    for i in systeme.get_map() :
        file1.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identity(), *i.get_coordinate() ) ) 
    file1.close()
    
    if type_algo == "residence-time":
        for i in range(1):
            t+=systeme.config_choice()
    elif type_algo == "metropolis":
        for i in range (1000):
            t+=10**(-13)
            systeme.one_step()
        #### à toi de compléter alexandre#######################""""
        file2= open("coordonnee2.txt","w")
        file2.writelines(str(systeme.get_site_number())+"\n")
        file2.writelines("\n")
        for i in systeme.get_map() :
            file2.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identity(), *i.get_coordinate() ) )
        file2.close()
    else:
        print("incorrect type")
    
    
    

        
    
    
        
        
        
        
        