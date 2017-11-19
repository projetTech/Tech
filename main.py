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


n_bloc=10
n_ite = 100
scale=2
size = 10
dimension = 2
e_aa = 0
e_ab = 0.21
e_bb = 0
proportion_b = 0.5
Temperature=297 #EN kelvin
systeme = mc.system (size,dimension)
systeme.set_maille([(0,0),(0.5,0.5)])
systeme.set_link_energy([e_aa,e_ab,e_bb])
systeme.initiate_map ()
print ("Système crée en ", time()-a, " secondes")
fn.monte_carlo(systeme,proportion_b,3,n_bloc,n_ite,scale)
print(systeme.get_sum_of_energy())

<<<<<<< HEAD
=======
#fn.monte_carlo(systeme,proportion_b,2,n)
#fn.monte_carlo(systeme,proportion_b,1,n)
fn.monte_carlo(systeme,proportion_b,4,n)
print("final energy =" , float(systeme.get_sum_of_energy()))
>>>>>>> parent of 64409e6... temps de résidence OK (i guess :p)



print ("Fin de la simulation. Elle aura durée ",time()-a, " secondes")