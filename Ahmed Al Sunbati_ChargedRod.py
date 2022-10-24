from vpython import *
#Web VPython 3.2
sf = 0.002 
oofpez = 9e9 
Qtot = 1e-9 
L = 1.0 
N = 10.0
dy = L/N 


slices = []
i = 0
y0 = -L/2 + dy/2
while i < N:
    a = sphere(pos=vector(0,y0+i*dy,0), radius=dy/2.0, color=color.red, q=Qtot/N)
    slices.append(a)
    i = i + 1 
    
observations = []

yobs_list = [-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75] 
for yobs in yobs_list:
    R = 0.15
    dtheta = pi/6.0
    theta = 0
    while (theta < 2.0*pi):
        a = vector(R*cos(theta), yobs, R*sin(theta))
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
