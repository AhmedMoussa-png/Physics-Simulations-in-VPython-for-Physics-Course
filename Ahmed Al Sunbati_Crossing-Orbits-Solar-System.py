from vpython import *
#Web VPython 3.2
def gforce(p1,p2):
  
    G = 1
    r_vec = p1.pos-p2.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    force_mag = G*p1.mass*p2.mass/r_mag**2
    force_vec = -force_mag*r_hat
    
    return force_vec
    
star = sphere( pos=vector(0,0,0), radius=0.5, color=color.yellow,
               mass = 1000, momentum=vector(0,0,0), make_trail=True )
       
planet1 = sphere( pos=vector(5,0,0), radius=0.2, color=color.blue,
                  mass = 1, momentum=vector(0,15,0), make_trail=True )

planet2 = sphere( pos=vector(0,7,0), radius=0.3, color=color.red,
                  mass = 2, momentum=vector(-15,0,0), make_trail=True )
#planet1 = sphere( pos=vector(5,0,0), radius=0.1, color=color.blue,
#                  mass = 1, momentum=vector(0,15,0), make_trail=True )
#angle = 17*pi/180
#planet2 = sphere( pos=vector(0,7,0), radius=0.15, color=color.red,
#                  mass = 2, momentum=vector(-15*cos(angle),0,-15*sin(angle)), make_trail=True )
                  


dt = 0.0001
t = 0
while (True):
    rate(5000)
    star.force = gforce(star,planet1)+gforce(star,planet2)
    planet1.force = gforce(planet1,star)+gforce(planet1,planet2)
    planet2.force = gforce(planet2,star)+gforce(planet2,planet1)
    star.momentum = star.momentum + star.force*dt
    planet1.momentum = planet1.momentum + planet1.force*dt
    planet2.momentum = planet2.momentum + planet2.force*dt
    star.pos = star.pos + star.momentum/star.mass*dt
    planet1.pos = planet1.pos + planet1.momentum/planet1.mass*dt
    planet2.pos = planet2.pos + planet2.momentum/planet2.mass*dt
    t = t + dt