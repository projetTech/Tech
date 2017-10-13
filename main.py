# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:44:20 2017

@author: Alexandre
"""


############## FILE AKMC_test1.py
from time import time

a=time()
import module_akmc as mc
import functions as fn
n=10000
size = 10
e_aa = 0
e_ab = 0
e_bb = 0.21
proportion_b = 0.5
Temperature=297 #EN kelvin
systeme = mc.system (size)
systeme.set_maille([(0,0),(0.5,0.5)])
systeme.set_link_energy([e_aa,e_ab,e_bb])
systeme.initiate_map ()
#systeme.sum_of_energy_init ()

#fn.monte_carlo(systeme,proportion_b,2,n)
#fn.monte_carlo(systeme,proportion_b,1,n)
fn.monte_carlo(systeme,proportion_b,3,n)
print(systeme.get_sum_of_energy())



#nombre_b = int(systeme.get_site_number()*proportion_b)
#print (nombre_b)
#while nombre_b > 0 :
 #   n = randint(0,systeme.get_site_number()-1) # tirage d'un site au hasard
  #  if not systeme.get_map()[n].get_identity() : #
   #     nombre_b -= 1
    #    systeme.update_map(n,True)
        

#file= open("coordonnee.txt","w")
#file.writelines(str(systeme.get_site_number())+"\n")
#file.writelines("\n")
#for i in systeme.get_map() :
 #   file.writelines("{} {:3.1f} {:3.1f} 0 \n".format(i.get_identity(), *i.get_coordinate() ) )

print (time()-a)