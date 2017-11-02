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

 #avoir l'energie de liaison enre deux sites
def get_link_energy(List_of_links,siteA,siteB):
    #list_of_links=[eaa,eab,ebb]
    if siteB.get_identity()==siteA.get_identity():
        if siteB.get_identity():
            return List_of_links[2]
        else:
            return List_of_links[0]
    else:
        return List_of_links[1]
# type=1 pour temps de résidence et =2 pour metropolis, type=3 pour tester les nouvelles fonctions qui peuvent remplacer update_energy
            
def monte_carlo(systeme,proportion_b,type_algo,n):#ajouter les types de variables
    t=0
    nombre_b = int(systeme.get_site_number()*proportion_b)
    L=[]
    T=[]
    while nombre_b > 0 :
        i = randint(0,systeme.get_site_number()-1) # tirage d'un site au hasard
        if not systeme.get_map()[i].get_identity() : #
            nombre_b -= 1
            systeme.update_map(i,True)
    systeme.sum_of_energy_init ()
    
   
    file1= open("coordonnee1.txt","w")
    file1.writelines(str(systeme.get_site_number())+"\n")
    file1.writelines("\n")
    for i in systeme.get_map() :
        file1.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identity(), *i.get_coordinate() ) ) 
    file1.close()
    
    plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],s=100,marker="o",c='r')		    
    plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],s=100,marker="o",c='b')		    
    plt.show()  		     
    	     
   
    """ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if a.get_identity()],s=20,marker="o",c='r')
    ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if not a.get_identity()],s=20,marker="o",c='b')
    plt.show()"""

    if type_algo == 1:#"residence-time"
        for i in range(n):
            t+=systeme.config_choice()
            L.append(systeme.get_sum_of_energy())
            T.append(t)
    elif type_algo == 2:#"metropolis"
        for i in range (n):
            t+=10**(-13)
            systeme.one_step()
            L.append(systeme.get_sum_of_energy())
            T.append(t)
    elif type_algo==3:
        for i in range (n):
            t+=10**(-13)
            systeme.one_step_1()
            L.append(systeme.get_sum_of_energy())
            T.append(t)
    elif type_algo==4:#nouvelle version de temps de résidence
        t=0
        L.append(systeme.get_sum_of_energy())
        T.append(t)
        new_sys=systeme.config_choice_init()
        t+=1/new_sys[-1][-1]#total_energy_sorted[-1]
        L.append(systeme.get_sum_of_energy())
        T.append(t)
        for i in range (n):
            new_sys=systeme.config_choice_rec(new_sys[0],new_sys[1],new_sys[2])
            t+=1/new_sys[-1][-1]#total_energy_sorted[-1]
            L.append(systeme.get_sum_of_energy())
            T.append(t)
        
        
        
            
    else:
        print("incorrect type")
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if a.get_identity()],s=20,marker="o",c='r')
    ax.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[2] for a in systeme.get_map() if not a.get_identity()],s=20,marker="o",c='b')
    plt.show()"""
    plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if a.get_identity()],s=100,marker="o",c='r')		    
    plt.scatter([a.get_coordinate()[0] for a in systeme.get_map() if not a.get_identity()],[a.get_coordinate()[1] for a in systeme.get_map() if not a.get_identity()],s=100,marker="o",c='b')		    
    plt.show()  		     
    	     
    plt.plot(T,L)
    plt.xlabel('temps')
    plt.ylabel('energy')
    plt.show()
    file2= open("coordonnee2.txt","w")
    file2.writelines(str(systeme.get_site_number())+"\n")
    file2.writelines("\n")
    for i in systeme.get_map() :
        file2.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identity(), *i.get_coordinate() ) )
    file2.close()
   
        

    
    
    

        
    
    
        
        
        
        
        