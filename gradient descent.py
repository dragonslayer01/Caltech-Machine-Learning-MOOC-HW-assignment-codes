import math
v = 0.0
u =v
u,v = 1,1
E_inst = 3.9303972318771003
eta = 0.1

while(E_inst>math.pow(10,-14)):
    multi = v*u
    
    delta_E_u = 2*(int(math.exp(v))+2*v*int(math.exp(-u)))*(u*int(math.exp(v))-2*v*int(math.exp(-u))    
    delta_E_v = 2*(v*u*int(math.exp(v))-2*int(math.exp(-u)))*(u*int(math.exp(v))-2*v*int(math.exp(-u))
    u = u + eta*delta_E_u
    v = v + eta*delta_E_v
    E_inst = math.pow((u*math.exp(v)-2*v*math.exp(-u)),2)
print(u+" "+v)
        

