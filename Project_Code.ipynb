import cvxpy as cp

#factories 1,2,3 to walmart, payless, DSW, Amazon, Finish Line
a1 = cp.Variable((3,5), integer = True)

#factories 1,2,3 to walmart, payless, DSW, Amazon, Finish Line
a2 = cp.Variable((3,5), integer = True)

#factories 1,2,4 to walmart, payless, DSW, Amazon
d = cp.Variable((3,4), integer = True)

#factories 1,2,4 to walmart, payless, DSW, Amazon
l = cp.Variable((3,4), integer = True)

#factories 1,2,5 to walmart, payless, DSW, Amazon, Finish Line
o = cp.Variable((3,5), integer = True)



#fixed factory costs, profit from selling to retailers, shipping costs, material costs, and potentially labor costs
obj_func = (-113500 + 20*cp.sum(a1[:,:]) - 128500 + 21*cp.sum(a2[:,:]) - 149000 + 35*cp.sum(d[:,:]) - 93500 + 10*cp.sum(l[:,:])
            - 139500 + 30*cp.sum(o[:,:]) - 2.5 * (cp.sum(a1[:,0]) + cp.sum(a2[:,0]) + cp.sum(d[:,0]) + cp.sum(l[:,0]) 
            + cp.sum(o[:,0])) - 2.7 * (cp.sum(a1[:,1]) + cp.sum(a2[:,1]) + cp.sum(d[:,1]) + cp.sum(l[:,1]) 
            + cp.sum(o[:,1])) - 2.8 * (cp.sum(a1[:,2]) + cp.sum(a2[:,2]) + cp.sum(d[:,2]) + cp.sum(l[:,2]) 
            + cp.sum(o[:,2])) - 2.5 * ((cp.sum(a1[:,3]) + cp.sum(a2[:,3]) + cp.sum(d[:,3]) + cp.sum(l[:,3]) 
            + cp.sum(o[:,3]))) - 2.9 * ((cp.sum(a1[:,4]) + cp.sum(a2[:,4]) + cp.sum(o[:,4]))) - 5 * (cp.sum(a1[:,:]) 
            + 2*cp.sum(a2[:,:]) + 4*cp.sum(d[:,:]) + 2*cp.sum(l[:,:]) + 2*cp.sum(o[:,:])) - 1 * (2*cp.sum(a1[:,:]) 
            + 2*cp.sum(a2[:,:]) + 2*cp.sum(l[:,:])) - 2 * (2*cp.sum(a1[:,:]) + cp.sum(a2[:,:]) + cp.sum(o[:,:])) 
            - 2.2 * (cp.sum(a1[:,:]) + cp.sum(a2[:,:]) + cp.sum(l[:,:]) + cp.sum(o[:,:])) - 2 * (cp.sum(a1[:,:]) 
            + cp.sum(a2[:,:]) + 2*cp.sum(d[:,:]) + cp.sum(l[:,:]) + cp.sum(o[:,:])))
            

#constraints
constraints = []

#lower demand constraints
#Walmart
constraints.append(cp.sum(a1[:,0]) >= 25000)
constraints.append(cp.sum(a2[:,0]) >= 25000)
constraints.append(cp.sum(d[:,0]) >= 40000)
constraints.append(cp.sum(l[:,0]) >= 50000)
constraints.append(cp.sum(o[:,0]) >= 40000)

#Payless
constraints.append(cp.sum(a1[:,1]) >= 6000)
constraints.append(cp.sum(a2[:,1]) >= 6000)
constraints.append(cp.sum(d[:,1]) >= 40000)
constraints.append(cp.sum(l[:,1]) >= 24000)
constraints.append(cp.sum(o[:,1]) >= 12000)

#DSW
constraints.append(cp.sum(a1[:,2]) >= 12500)
constraints.append(cp.sum(a2[:,2]) >= 12500)
constraints.append(cp.sum(d[:,2]) >= 40000)
constraints.append(cp.sum(l[:,2]) >= 60000)
constraints.append(cp.sum(o[:,2]) >= 30000)

#Amazon
constraints.append(cp.sum(a1[:,3]) >= 25000)
constraints.append(cp.sum(a2[:,3]) >= 25000)
constraints.append(cp.sum(d[:,3]) >= 50000)
constraints.append(cp.sum(l[:,3]) >= 60000)
constraints.append(cp.sum(o[:,3]) >= 50000)

#Finish Line
constraints.append(cp.sum(a1[:,4]) >= 45000)
constraints.append(cp.sum(a2[:,4]) >= 45000)
constraints.append(cp.sum(o[:,4]) >= 10000)

#upper demand constraints
#Walmart
constraints.append(cp.sum(a1[:,0]) <= 27500)
constraints.append(cp.sum(a2[:,0]) <= 27500)
constraints.append(cp.sum(d[:,0]) <= 44000)
constraints.append(cp.sum(l[:,0]) <= 55000)
constraints.append(cp.sum(o[:,0]) <= 44000)

#Payless
constraints.append(cp.sum(a1[:,1]) <= 6600)
constraints.append(cp.sum(a2[:,1]) <= 6600)
constraints.append(cp.sum(d[:,1]) <= 44000)
constraints.append(cp.sum(l[:,1]) <= 26400)
constraints.append(cp.sum(o[:,1]) <= 13200)

#DSW
constraints.append(cp.sum(a1[:,2])  <= 13750)
constraints.append(cp.sum(a2[:,2]) <= 13750)
constraints.append(cp.sum(d[:,2]) <= 44000)
constraints.append(cp.sum(l[:,2]) <= 66000)
constraints.append(cp.sum(o[:,2]) <= 33000)

#Amazon
constraints.append(cp.sum(a1[:,3]) <= 27500)
constraints.append(cp.sum(a2[:,3])  <= 27500)
constraints.append(cp.sum(d[:,3])  <= 55000)
constraints.append(cp.sum(l[:,3])  <= 66000)
constraints.append(cp.sum(o[:,3])  <= 55000)

#Finish Line
constraints.append(cp.sum(a1[:,4]) <= 49500)
constraints.append(cp.sum(a2[:,4]) <= 49500)
constraints.append(cp.sum(o[:,4]) <= 11000)

#Supply Constraints
constraints.append(cp.sum(a1[0,:]) + cp.sum(a2[0,:])  + cp.sum(d[0,:]) + cp.sum(l[0,:]) + cp.sum(o[0,:]) <= 250000)
constraints.append(cp.sum(a1[1,:]) + cp.sum(a2[1,:])  + cp.sum(d[1,:]) + cp.sum(l[1,:]) + cp.sum(o[1,:]) <= 250000)
constraints.append(cp.sum(a1[2,:]) + cp.sum(a2[2,:]) <= 200000)
constraints.append(cp.sum(d[2,:]) + cp.sum(l[2,:]) <= 200000)
constraints.append(cp.sum(l[2,:]) <= 100000)

#Material Constraints
#Factory 1 Materials
#Leather
constraints.append(cp.sum(a1[0,:]) + 2*cp.sum(a2[0,:])  + 4*cp.sum(d[0,:]) + 2*cp.sum(l[0,:]) + 2*cp.sum(o[0,:]) <= 300000)
#Rubber                                                                                                  
constraints.append(cp.sum(a1[0,:]) + cp.sum(a2[0,:])  + 2*cp.sum(d[0,:]) + cp.sum(l[0,:]) + cp.sum(o[0,:]) <= 155000)
#Textile                                                                                                  
constraints.append(2*cp.sum(a1[0,:]) + 2*cp.sum(2*a2[0,:]) + 2*cp.sum(l[0,:]) <= 160000)
#Synthetic                                                                                              
constraints.append(2*cp.sum(a1[0,:]) + cp.sum(a2[0,:]) + cp.sum(o[0,:]) <= 125000)
#Foam                                                                                                 
constraints.append(cp.sum(a1[0,:]) + cp.sum(a2[0,:]) + cp.sum(l[0,:]) + cp.sum(o[0,:]) <= 130000)
                                                                         
#Factory 1 Materials
#Leather
constraints.append(cp.sum(a1[0,:]) + 2*cp.sum(a2[0,:])  + 4*cp.sum(d[0,:]) + 2*cp.sum(l[0,:]) + 2*cp.sum(o[0,:]) <= 300000)
#Rubber                                                                                                  
constraints.append(cp.sum(a1[0,:]) + cp.sum(a2[0,:])  + 2*cp.sum(d[0,:]) + cp.sum(l[0,:]) + cp.sum(o[0,:]) <= 155000)
#Textile                                                                                                  
constraints.append(2*cp.sum(a1[0,:]) + 2*cp.sum(2*a2[0,:]) + 2*cp.sum(l[0,:]) <= 160000)
#Synthetic                                                                                              
constraints.append(2*cp.sum(a1[0,:]) + cp.sum(a2[0,:]) + cp.sum(o[0,:]) <= 125000)
#Foam                                                                                                 
constraints.append(cp.sum(a1[0,:]) + cp.sum(a2[0,:]) + cp.sum(l[0,:]) + cp.sum(o[0,:]) <= 130000)
                                                                         

#Factory 3 Materials
#Leather
constraints.append(cp.sum(a1[0,:]) + 2*cp.sum(a2[0,:]) <= 150000)
#Rubber                                                                                                  
constraints.append(cp.sum(a1[0,:]) + cp.sum(a2[0,:]) <= 105000)
#Textile                                                                                                  
constraints.append(2*cp.sum(a1[0,:]) + 2*cp.sum(2*a2[0,:]) <= 210000)
#Synthetic                                                                                              
constraints.append(2*cp.sum(a1[0,:]) + cp.sum(a2[0,:]) <= 165000)
#Foam                                                                                                 
constraints.append(cp.sum(a1[0,:]) + cp.sum(a2[0,:]) <= 110000)

#Factory 4 Materials
#Leather
constraints.append(4*cp.sum(d[0,:]) + 2*cp.sum(l[0,:]) <= 300000)
#Rubber                                                                                                  
constraints.append(2*cp.sum(d[0,:]) + cp.sum(l[0,:]) <= 160000)
#Textile                                                                                                  
constraints.append(2*cp.sum(l[0,:]) <= 120000)
#Foam                                                                                                 
constraints.append(cp.sum(l[0,:]) <= 50000)

#Factory 5 Materials
#Leather
constraints.append(2*cp.sum(o[0,:]) <= 100000)
#Rubber                                                                                                  
constraints.append(cp.sum(o[0,:]) <= 55000)
#Synthetic                                                                                              
constraints.append(cp.sum(o[0,:]) <= 56500)
#Foam                                                                                                 
constraints.append(cp.sum(o[0,:]) <= 60000)

#non-negativity
for i in range(3): 
    for j in range(5):
        constraints.append(a1[i,j] >= 0)
        constraints.append(a2[i,j] >= 0)
        constraints.append(o[i,j] >= 0)
for i in range(3): 
    for j in range(4):
        constraints.append(d[i,j] >= 0)
        constraints.append(l[i,j] >= 0)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)

print("obj_func = ")
print(obj_func.value)
print("a1 =")
print(a1.value)
print("a2 =")
print(a2.value)
print("d =")
print(d.value)
print("l =")
print(l.value)
print("o =")
print(o.value)
