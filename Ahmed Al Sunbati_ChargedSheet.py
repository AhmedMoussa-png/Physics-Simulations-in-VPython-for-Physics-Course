from vpython import *
#Web VPython 3.2
sf = 0.002
oofpez = 9e9 # Electric constant.
e0 = 1.0/(4*pi*oofpez) # Other electric constant.
Qtot = 1e-9 # Total charge.
R = 1.0 # Radius of disk.
N = 5000 # Number of point charges the disk will be made of.

A = pi*R**2 # Area of the disk.
da = A/N # Area occupied by a single point charge.
dx = sqrt(da) # Distance between neighboring point charges.
constant = Qtot/(A*2*e0) # Thing in front of exact E result.

# Create a list of point charges.
sources = [] 


x = 0
while (x <= R):
    y = 0
    ymax = sqrt(R**2-x**2)
    while (y <= ymax):
        sources.append( sphere( radius=0.1*dx, pos=vector(x,y,0),
                                q=Qtot/N, color=color.red ) )
        sources.append( sphere( radius=0.1*dx, pos=vector(-x,y,0),
                                q=Qtot/N, color=color.red ) )
        sources.append( sphere( radius=0.1*dx, pos=vector(x,-y,0),
                                q=Qtot/N, color=color.red ) )
        sources.append( sphere( radius=0.1*dx, pos=vector(-x,-y,0),
                                q=Qtot/N, color=color.red ) )
        y = y + dx
    x = x + dx


# Create a list of observation locations.
observations = [] 

power_min = -6
power_max = 1
n_obs = 100 

power = power_min
while (power <= power_max):
    zmin = 10**(power)*R 
    zmax = 10**(power+1)*R
    dz = (zmax-zmin)/n_obs
    z = zmin
    while (z <= zmax):
        observations.append(vector(0,0,z))
        z = z + dz
    power = power + 1





print(dx/dz)



graph(xtitle="distance from disk", ytitle="electric field magnitude",
         ymax=20000,ymin=10**-1,xmin=10**power_min,xmax=10**power_max,
         logx=True,logy=True)
         
E_graph = gcurve(color=color.black,label="calculation")
theoretical_graph = gcurve(color=color.red,label="theory")

for r_obs in observations:
    # Calculate E from each point charge.
    E_net = vector(0,0,0)
    for s in sources:
        r = r_obs - s.pos # Relative position vector.
        rhat = r/mag(r) # Unit vector.
        E = (oofpez * s.q / mag(r)**2) * rhat # Calculate E for this slice.
        E_net = E_net + E # Add this E to the total E.
        
    E_graph.plot(pos=(r_obs.z,mag(E_net)))
    theoretical_graph.plot(pos=(r_obs.z, constant * (1-r_obs.z/(R**2+r_obs.z**2)**0.5)))
