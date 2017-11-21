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


n_bloc=100
n_ite = 10000
scale=0.3
size = 30
dimension = 2
e_aa = 0.21
e_ab = 0
e_bb = 0
proportion_b = 0.5
Temperature=297 #EN kelvin
systeme = mc.system (size,dimension)
systeme.set_maille([(0,0,0),(0.5,0.5,0.5)])
systeme.set_link_energy([e_aa,e_ab,e_bb])
systeme.initiate_map ()
print ("Système crée en ", time()-a, " secondes")



#fn.monte_carlo(systeme,proportion_b,2,n)
#fn.monte_carlo(systeme,proportion_b,1,n)
type_algo=4
fn.monte_carlo(systeme,proportion_b,type_algo)
if type_algo==2:
    print("algo utilisé est metropolis")
elif type_algo==4:
    print("algo utilisé est residence time")

print("final energy =" , float(systeme.get_sum_of_energy()))



print ("Fin de la simulation. Elle aura durée ",time()-a, " secondes")