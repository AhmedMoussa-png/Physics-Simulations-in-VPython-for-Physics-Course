from vpython import *
#Web VPython 3.2
sf = 0.0002 
oofpez = 9e9 
Qtot = 1e-9 
R_ring = 0.1 
N = 50 
dtheta = 2*pi/N # 


slices = [] 
i = 0
while i < N:

    a = sphere(pos=vector(R_ring*cos(i*dtheta),R_ring*sin(i*dtheta),0), 
                          radius=R_ring/10.0, color=color.red, q=Qtot/N)
    slices.append(a)
    i = i + 1 
    
    

observations = [] 

yobs_list = [-0.1,-0.075,-0.05,-0.025,0.00,0.025,0.05,0.075,0.1] 
for yobs in yobs_list:
    R_obs = 0.15 
    dtheta = pi/6.0 
    theta = 0
    while (theta < 2.0*pi):
        a = vector(R_obs*cos(theta), yobs, R_obs*sin(theta))
        observations.append(a)
        theta = theta + dtheta


for r_obs in observations:
    E_net = vector(0,0,0)
    for s in slices:
        r = r_obs - s.pos 
        rhat = r/mag(r) 
        E = (oofpez * s.q / mag(r)**2) * rhat 
        E_net = E_net + E 
        
    arrow(pos=r_obs, axis=sf*E_net)
    
print(E_net)