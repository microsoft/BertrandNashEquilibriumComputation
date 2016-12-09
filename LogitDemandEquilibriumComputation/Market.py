from math import exp
from random import random
import Single_Logit_Multi_Items
import Single_Logit_Multi_Items_Fixed_Cost
import Mixed_Logit_Best_Response_Dynamic
import Two_Dimension_Logit_Binary_Search
import config

class Item:
    def __init__(self):
        self.id=''
        self.price=0
        self.demands=[]
        self.mcost=0
        self.utility=0
    def print(self):
            print("item id: ", self.id, " utility: ", self.utility, " mcost: ",self.mcost)
            print("price: ", self.price)
            print("demands: ")
            for d in self.demands:
                print(d)

class Seller:
    def __init__(self):
        self.id=''
        self.alpha=0 # Marginal Profit
        self.items=[]
        self.R=0 
        self.num_items=0
        self.rev=0
        self.fcost=0
    def print(self):
        print("Seller: ", self.id)
        print("Number of items: ", self.num_items)
        self.rev=0
        for i in self.items:
            for d in i.demands:
                self.rev+=(i.price-i.mcost)*d
        print("Revenue: ",self.rev, " Fixed costs: ", self.fcost)
        for j in range(0,self.num_items):
            self.items[j].print()

class Market:
    def __init__(self):
        self.sellers=[]
        self.price_sensitivity=[] 
        self.num_sellers=0
        self.logit_dim=0
        config.set_config()
        return super().__init__()

    def print(self):
        print("##############MARKET##################")
        print("Logit dimensions : ", self.logit_dim)
        print("Price sensitivity parameters: ")
        for i in range(0,self.logit_dim):
            print( self.price_sensitivity[i] )
        print("number of sellers : ",self.num_sellers)
        for i in range(0,self.num_sellers):     
            self.sellers[i].print()
        print("##############END OF MARKET############")

    def read(self,fileaddress):
        file=open(fileaddress , 'r' )
        data=file.read()
        data=data.split()
        self.logit_dim=(int(data.pop(0)))
        for i in range(0,self.logit_dim):
            self.price_sensitivity.append(float(data.pop(0)))
        self.num_sellers=(int(data.pop(0)))
        for j in range(0,self.num_sellers):
            s=Seller()
            s.id=(data.pop(0))
            s.num_items=int(data.pop(0))
            for i in range(0,s.num_items):
                good=Item()
                good.id=(data.pop(0))
                good.utility=(float(data.pop(0)))
                good.mcost=(float(data.pop(0)))
                s.items.append(good)
            self.sellers.append(s)

    def read_fcost(self,fileaddress):
        file=open(fileaddress , 'r' )
        data=file.read()
        data=data.split()
        self.logit_dim=(int(data.pop(0)))
        for i in range(0,self.logit_dim):
            self.price_sensitivity.append(float(data.pop(0)))
        self.num_sellers=(int(data.pop(0)))
        for j in range(0,self.num_sellers):
            s=Seller()
            s.id=(data.pop(0))
            s.fcost=float(data.pop(0))
            s.num_items=int(data.pop(0))
            for i in range(0,s.num_items):
                good=Item()
                good.id=(data.pop(0))
                good.utility=(float(data.pop(0)))
                good.mcost=(float(data.pop(0)))
                s.items.append(good)
            self.sellers.append(s)

    def Single_Logit_Multi_Items_Equilibrium(self):
        self = Single_Logit_Multi_Items.Single_Logit_Multi_Items(self)

    def Single_Logit_Multi_Items_Fixed_Cost_Equilibrium(self):
        self = Single_Logit_Multi_Items_Fixed_Cost.Single_Logit_Multi_Items_Fixed_Cost(self)

    def Mixed_Logit_Equilibrium_Best_Response_Dynamic(self):
        self = Mixed_Logit_Best_Response_Dynamic.Mixed_Logit_Best_Response_Dynamic(self)

    def Mixed_Logit_Equilibrium_Binary_Search(self):
        if(self.logit_dim != 2):
            print("ERROR: Binary search algorithm works only for two dimensional logit market")
        else:
            self = Two_Dimension_Logit_Binary_Search.Two_Dimension_Logit_Binary_Search(self)        