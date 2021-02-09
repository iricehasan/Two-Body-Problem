#31.10.2020

import numpy

G = 6.67408e-11 #in terms of m^3 kg^-1 s^-2


def a_m1(r1, r2): #acceleration of mass 1
    r = RY - RX #distance between masses
    rlen = ( (RY[1]-RX[1])**2 + (RY[0] - RX[0])**2 ) **0.5 #magnitude of the distance
    return (G * m2 * r) / rlen**3


def a_m2(r1, r2): #acceleration of mass 2
    r = RY - RX #distance between masses
    rlen = ( (RY[1]-RX[1])**2 + (RY[0] - RX[0])**2 ) **0.5 #magnitude of the distance
    return (- G * m1 * r) / rlen**3

def fullstep(dt, x, v): #function to find full step
    return x + v*dt

def halfstep(dt, x, v): #function to find half-step
    return x + v*dt/2

def UpdateVel(dt, v, a):
    return v + a*dt

def print_values(RX, RY):
    print(RX[0],RX[1], end = ' ')
    print(RY[0],RY[1], end = ' ')
    print()


dt = 24*3600 #dt = 10^-2

tend = 365*24*3600 #end time
step = 0
prst = 1 #printstep

#initial configuration
t = 0.0

m1 = 1.9891e30  #mass of Sun in terms of kg
RX = numpy.array([0, 0])  #Sun is stationary at the origin
VX = numpy.array([0,0])


m2 =  5.972e24 #mass of Earth in terms of kg
RY = numpy.array([1.4710e11, 0])
VY = numpy.array([0,3.0287e4]) #in terms of m/s

print_values(RX, RY) #printing initial values


#Leapfrog Integration 

t += dt/2

RX = halfstep(dt, RX, VX)  
RY = halfstep(dt, RY, VY)

while t < tend:
    step += 1
    t += dt
   
    ax = a_m1(RX,RY)
    ay = a_m2(RX,RY)
	
    VX = UpdateVel(dt, VX, ax)
    VY = UpdateVel(dt, VY, ay)
    
    if (step%prst) == 0:
        RX = halfstep(dt, RX, VX)
        RY = halfstep(dt, RY, VY)
        print_values(RX, RY)
        RX = halfstep(dt, RX, VX)
        RY = halfstep(dt, RY, VY)
    else:
        RX = fullstep(dt, RX, VX)
        RY = fullstep(dt, RY, VY)
    
t += dt/2 
ax = a_m1(RX,RY)
ay = a_m2(RX,RY)

VX += ax * dt/2
VY += ay * dt/2

print_values(RX, RY) 
