#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:09:51 2019

@author: batdora
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:44:58 2019

@author: batdora
"""
from timeit import default_timer as timer
from matplotlib.pyplot import *
import numpy as np
from scipy import stats
import seaborn as sns


N=np.zeros((1000,1000))
t=np.zeros((1000,1000))
Bank=np.zeros((1000,1000))
inf=np.zeros((1000,1000))
t[0,:]=0
N[0,:]=50
Bank[0,:]=100


start = timer()


debt=0;
savings=0;
tsaving=0;
tdebt=0;
interest=1.1;
cost= 1
inflation= 1
tinf=0;
poor=0;
rich=0;
for i in range(0,1000-1):
    t[i+1,:]=t[i,:]+1;
    #Inflation
    if Bank[i,:]/float(N[i,:])<3 and t[i+1,:] - tinf > 10:
        inflation= inflation*1.01
        tinf= t[i+1,:]
        cost= cost*inflation
    #Bank Bancrupcy
    if Bank[i,:] < 0 and N[i,:]>40:
        N[i,:]= N[i,:]-20
        Bank[i,:]= Bank[i,:]+20
        savings= savings+20
        interest= 1.5
    #Investment
    if N[i,:]>40:
        if tsaving == 0:
            if np.random.rand()<(0.2):
                N[i,:]= N[i,:] - N[i,:]*0.1
                savings= savings + N[i,:]*0.1
                Bank[i,:]= Bank[i,:]+ N[i,:]*0.1
                tsaving=t[i+1,:]
    if tsaving!=0 and t[i+1,:]-tsaving == 10:
        savings = savings * interest
    if np.random.rand()<(0.2) and tsaving!=0 and t[i+1,:]-tsaving > 10:
        N[i,:]= N[i,:] + savings
        Bank[i,:]= Bank[i,:]+ savings
        tsaving=0
        savings=0
    #Debt
    if tdebt !=0 and t[i+1,:]-tdebt == 10:
        debt = debt * interest
    if N[i,:] > debt:
        N[i,:] = N[i,:] - debt
        Bank[i,:]= Bank[i,:]+ debt
        debt=0
    if debt == 4:
        interest= (interest-1)*1.5 + 1
    if debt == 8:
        interest= (interest-1)/1.5 *2 + 1
    if debt > 10:
        N[i+1,:]= 0
        Bank[:,:]= Bank[i,:]
        break
    else:
        if N[i,:]>0:
            N[i,:]=N[i,:]-cost
            Bank[i,:]= Bank[i,:]+cost
            if np.random.rand()<(0.5):
                 R=np.random.rand(1,1000);
                 N[i+1,:]=N[i,:]+(R<0.5)*2-1
            else:
                N[i+1,:]=N[i,:]
                Bank[i+1,:]= Bank[i,:]
        else:
            N[i+1,:]=N[i,:]+1
            Bank[i+1,:]= Bank[i,:]-1
            debt= debt+1
            tdebt= t[i+1,:]

    if N[i+1,:]==N[i,:]==0:
        poor=poor+1
    if N[i+1,:]> 2000:
        rich=rich+1

"""
BANK STARTS WITH MORE MONEY THAN 100"""



end = timer()
print(end-start)

figure(0)
plot(t,N)

figure(1)
plot(t,Bank)

print(rich, poor)