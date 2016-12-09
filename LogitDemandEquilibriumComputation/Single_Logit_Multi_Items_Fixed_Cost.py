
from Single_Logit_Multi_Items import *

def ComputeCLambda(M):
    for s in M.sellers:
        s.clambda=f(s.fcost+1/M.price_sensitivity[0],s.R,M.price_sensitivity[0])

def Single_Logit_Multi_Items_Fixed_Cost(M):
    ComputeR(M)
    ComputeCLambda(M)
    sellers=sorted(M.sellers, key=lambda seller: seller.clambda)
    M.sellers=[]
    M.num_sellers=0
    for s in sellers:
        M.sellers.append(s)
        M.num_sellers=len(M.sellers)
 #       print ('calling fixpoint')
        fp=fixpoint(M)
  #      print ('midfx is ', fp)
        if fp < s.clambda:
            M.sellers.pop()
            M.num_sellers=len(M.sellers)
    Single_Logit_Multi_Items(M)
    return M


