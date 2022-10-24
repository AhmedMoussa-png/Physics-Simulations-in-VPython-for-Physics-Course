from vpython import *
#Web VPython 3.2
mz0fp = 1e-7
qe = 1.6e-19
mproton = 1.7e-27
B0 = vector(0,0.2,0)
bscale = 1

xmax = 0.4
dx = 0.1
yg = -0.1
x = -xmax
while x < xmax+dx:
    curve(pos=[vector(x,yg,-xmax),vector(x,yg,xmax)],color=vector(.7,.7,.7))
    x = x+dx
z = -xmax
while z < xmax+dx:
    curve(pos=[vector(-xmax,yg,z),vector(xmax,yg,z)],color=vector(.7,.7,.7))
    z = z+dx
x = -xmax
while x < xmax+dx:
    z = -xmax
    while z < xmax+dx:
        arrow(pos=vector(x,yg,z),axis=B0*bscale,color=vector(0,0.8,0.8))
        z = z + dx
    x = x + dx

# Create proton and set initial conditions.
rad = 1e-2
proton = sphere(pos=vector(0,0.15,0.0), radius=rad, color=color.red,
                  make_trail=True, trail_radius=rad/3, retain=2000,
                  velocity=vector(-2e6,0,0))
antiproton = sphere(pos=vector(0,0.15,0.0), radius=rad, color=color.green,
                  make_trail=True, trail_radius=rad/3, retain=2000,
                  velocity=vector(-2e6,0,0))
qproton = qe
dt = 5e-11

while (True):
    rate(500)
    force = qproton*cross(proton.velocity,B0)*
    proton.velocity = proton.velocity + force/mproton*dt
    proton.pos = proton.pos + proton.velocity*dt
    force = -2*qproton*cross(antiproton.velocity,B0)
    antiproton.velocity = antiproton.velocity + force/mproton*dt
    antiproton.pos = antiproton.pos + antiproton.velocity*dt