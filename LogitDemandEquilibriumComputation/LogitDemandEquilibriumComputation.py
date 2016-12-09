from Market import *

print (" 1) Multi Item Logit \n 2) Multi Item Logit with Fixed Costs \n 3) Mixed Logit (best response dynamic)")
print (" 4) Two dimensional Mixed Logit (Binary Search)")
select=int(input(" Select one (1-4): "))
#fileaddress=input(" Input file address: ")
fileaddress = "alg1_test_0.txt"
if (select==1):  
    M = Market()
    M.read(fileaddress)
    M.Single_Logit_Multi_Items_Equilibrium()
    M.print()
else:
    if(select==2):      
        M = Market()
        M.read_fcost(fileaddress) #("inputf.txt")
        M.Single_Logit_Multi_Items_Fixed_Cost_Equilibrium()
        M.print()
    else:
        if(select==3):
            M = Market()
            M.read(fileaddress)
            M.Mixed_Logit_Equilibrium_Best_Response_Dynamic()
            M.print()
        else:
            if(select==4):
                M = Market()
                M.read(fileaddress)
                M.Mixed_Logit_Equilibrium_Binary_Search()
                M.print()
            else:
                print(" Wrong input ")