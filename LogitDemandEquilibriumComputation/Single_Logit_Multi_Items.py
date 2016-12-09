
from math import exp
from random import random
from config import *

def f(x,R,g):
    return (1-(1/(g*(x))))/max(precision(),R*exp(-g*x))

def invertf(y,R,g):
    s,e=0,max_price()
    con=0
    while abs(e-s)>precision() and con<loop_limit() :
        con=con+1
        mid=((s+e)/2)
        if y<f(mid,R,g):
            e=mid
        else:
            s=mid
    if(con==loop_limit()):
        print("Invert calculations timed out")
    return (s+e)/2

def alpha(l,M):
    for j in M.sellers:
        j.alpha=invertf(l,j.R,M.price_sensitivity[0])

def ComputeR(M):
    for s in M.sellers:
        s.R=0
        for i in s.items:
            s.R+=exp(i.utility - M.price_sensitivity[0]*(i.mcost))

def mainf(l,M):
    alpha(l,M)
    sm=0
    ComputeR(M)
    for s in M.sellers:
        sm=sm+s.R*exp(-M.price_sensitivity[0]*(s.alpha))
    return 1/(1+sm)


def fixpoint(M): # Read the precision as a parameter from a config file. Cont limit
  #  print ('fix')
    s,e=0,1
    m=0.5
    cont=0
    while abs(e-s)>precision() and cont<loop_limit():
        if mainf(m,M)>m:
            s=m
        else:
            e=m
        m=(s+e)/2
        cont+=1
    if cont==loop_limit():
        print ('ERROR: fixpoint calculation timed out')
    return m


def Single_Logit_Multi_Items(M):
    ComputeR(M)
    fp=fixpoint(M)
    R=0
    alpha(fp,M)
    for s in M.sellers:
        s.rev=(s.alpha-1/M.price_sensitivity[0])
        for i in s.items:
            i.price=s.alpha+i.mcost

    for s in M.sellers:
        for i in s.items:
            R+=exp(i.utility-M.price_sensitivity[0]*(i.price))
    
    for s in M.sellers:
        for i in s.items:
            i.demands.append((exp(i.utility-M.price_sensitivity[0]*(i.price)))/(1+R))
    return M



