from math import exp
import matplotlib.pyplot as pl
from config import *

def rhside(demands,M):
    return (demands[0]+demands[1])/max(precision(),(M.price_sensitivity[0]*demands[0]*(1-demands[0])+M.price_sensitivity[1]*demands[1]*(1-demands[1])))

def demands(item,price,llist,M):
    x=[0,0]
    x[0]=llist[0]*exp(item.utility-M.price_sensitivity[0]*price)
    x[1]=llist[1]*exp(item.utility-M.price_sensitivity[1]*price)
    return x

def findprice(item,llist,M):
    s=0
    e=max_price()
    mid=(s+e)/2
    count=0
    while(e-s>precision()) and count<loop_limit():
        if(rhside(demands(item,mid,llist,M),M)<mid-item.mcost):
            e=mid
        else:
            s=mid
        mid=(s+e)/2
        count+=1
    if(count==loop_limit()):
        print ("Error: price/root cannot be calculated")
    return mid

def f_2(llist,M):
    R=0.0
    for seller in M.sellers:
        seller.items[0].price=findprice(seller.items[0],llist,M)
        R+=exp(seller.items[0].utility-M.price_sensitivity[1]*seller.items[0].price)
    return (1)/(1+R)

def f_1(llist,M):
    R=0.0
    for seller in M.sellers:
        seller.items[0].price=findprice(seller.items[0],llist,M)
        R+=exp(seller.items[0].utility-M.price_sensitivity[0]*seller.items[0].price)
    return (1)/(1+R)


def fixpoint_f_2(l_1,M):
    s=precision()
    e=1
    mid=(s+e)/2
    count=0
    while( e-s>precision()) and (count<loop_limit()):
           if (f_2([l_1,mid],M)>mid):
                s=mid
           else:
                e=mid
           mid=(s+e)/2
           count+=1
    if count==loop_limit():
        print ("ERROR: fix point of f_2 cannot be calculated")
    return mid
    
def fixedpoint_f(M):
    s=precision()
    e=1
    mid=(s+e)/2
    count=0
    while ( e-s>precision()) and (count<loop_limit()):
           if (f_1([mid,fixpoint_f_2(mid,M)],M)>mid):
                s=mid
           else:
                e=mid
           mid=(s+e)/2
           count+=1
    if(count==loop_limit()):
        print ("ERROR: fix point of f_1 cannot be calculated")    
    return (mid,fixpoint_f_2(mid,M))


def mixlogit_2(M):
    fp=fixedpoint_f(M)
    for seller in M.sellers:
        seller.items[0].price=findprice(seller.items[0],fp,M)
        x=demands(seller.items[0],seller.items[0].price,fp,M)
        seller.items[0].demands.append(x[0])
        seller.items[0].demands.append(x[1])
    return M

def Two_Dimension_Logit_Binary_Search(M): # two d
    M=mixlogit_2(M)
    return M