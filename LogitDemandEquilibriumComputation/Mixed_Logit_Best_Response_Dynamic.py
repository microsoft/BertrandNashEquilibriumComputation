from math import exp
from random import random
from time import time
from config import *

def getx(i,price,item,R,ps):
    return exp(item.utility-ps[i]*price)/(R[i]-exp(item.utility-ps[i]*item.price)+exp(item.utility-ps[i]*price))

def rhside(price,item,R,ps):
    num=0
    dnum=0
    for i in range(0,len(ps)):
        x=(getx(i,price,item,R,ps))
        num+=x
        dnum+=ps[i]*x*(1-x)
    return num / max(precision(),dnum)

def best_response(M,item,R):
    s=item.mcost+precision()
    e=max_price()
    mid=(s+e)/2
    cont=1
    while ( e-s>precision() ) and (cont<loop_limit()):
        if rhside(mid,item,R,M.price_sensitivity)< mid-item.mcost:
            e=mid
        else:
            s=mid
        mid=(s+e)/2
        cont+=1
    if(cont==loop_limit()):
        print('ERROR: Best response cannot be calculated.')
    return mid


def computeR(M):
    R=[]
    for j in range(0,len(M.price_sensitivity)):
        R.append(1)
    for seller in M.sellers:
        for j in range(0,len(M.price_sensitivity)):
            R[j]+=exp(seller.items[0].utility-M.price_sensitivity[j]*seller.items[0].price)
    return R


def iteration(M): 
    R=computeR(M)
    Max_Error=0
    nprices=[]
    for seller in M.sellers:
        item=seller.items[0]
        nprice=(best_response(M,seller.items[0],R))
        if(Max_Error < abs(seller.items[0].price-nprice)):
            Max_Error = abs(seller.items[0].price-nprice)
        item.price=item.price*(mix_parameter())+nprice*(1-mix_parameter())
    return Max_Error
    
    
def heuristic(M): 
    for seller in M.sellers:
        seller.items[0].price=seller.items[0].mcost+1
    
    cont=1
    while iteration(M)>convergence_limit() and cont<loop_limit():
        cont+=1
    
    if( cont==loop_limit()):
        print ("ERROR: The best response dynamic did not converge")
    print ('Dynamic converged in ',cont,' epoches')
    return M

    

########################################


def Mixed_Logit_Best_Response_Dynamic(M):
    M=heuristic(M)
    R=computeR(M)
    for seller in M.sellers:
        for j in range(0,len(M.price_sensitivity)):
            if (len(seller.items[0].demands)<=j):
                seller.items[0].demands.append(getx(j,seller.items[0].price,seller.items[0],R,M.price_sensitivity))
            else:
                seller.items[0].demands[j]=(getx(j,seller.items[0].price,seller.items[0],R,M.price_sensitivity))

    return M
