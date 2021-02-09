#21.01.2021

import numpy
import matplotlib.pyplot as plt

G = 2.9591220828559e-4 # in terms of AU^3 d^-2  M_Sun^-1

def grav_force(m1,m2,r1,r2): #force on mass 2
    r = RY - RX #distance between masses
    rlen = ( (RY[1]-RX[1])**2 + (RY[0] - RX[0])**2 ) **0.5 #magnitude of the distance
    return (- G * m1 *m2* r) / rlen**3


def fullstep(dt, x, v): #function to find full step
    return x + v*dt

def halfstep(dt, x, v): #function to find half-step
    return x + v*dt/2

def UpdateVel(dt, v, a):
    return v + a*dt

#def a*dt olarak yaz fonksiyonları

data = open("data.txt","w")
def write_values(RX,Rsun): #function to write values into the file S24.dat
    
    data.write("{0:f} {1:f} {2:f} {3:f} \n".format(RX[0],RX[1], Rsun[0], Rsun[1]   )	 ) 


dt = 1#dt = 10^-2

tend = 365 #end time
step = 0
prst = 1 #printstep

#initial configuration
t = 0.0

m1 = 1 #mass of Sun in terms of Solar Mass
RX = numpy.array([0, 0])  #Sun is stationary at the origin
VX = numpy.array([0,0])


m2 = 3.00329789031573e-06 #mass of Earth in terms of Solar Mass
RY = numpy.array([0.98329, 0])
VY = numpy.array([0,0.0174939388]) # in terms of AU/day

write_values(RX, RY) #printing initial values

#Leapfrog Integration 

t += dt/2 #starting with half step

RX = halfstep(dt, RX, VX)  
RY = halfstep(dt, RY, VY)

while t < tend:
    step += 1
    t += dt
   
    ax = grav_force(m1,m2,RX,RY) /-m1
    ay = grav_force(m1,m2,RX,RY)/m2
	
    VX = UpdateVel(dt, VX, ax)
    VY = UpdateVel(dt, VY, ay)
    
    if (step%prst) == 0:
        RX = halfstep(dt, RX, VX)
        RY = halfstep(dt, RY, VY)
        write_values(RX, RY)
        RX = halfstep(dt, RX, VX)
        RY = halfstep(dt, RY, VY)
    else:
        RX = fullstep(dt, RX, VX)
        RY = fullstep(dt, RY, VY)
    
t += dt/2 
ax = grav_force(m1,m2,RX,RY) /-m1
ay = grav_force(m1,m2,RX,RY)/m2

VX += ax * dt/2
VY += ay * dt/2

write_values(RX, RY)

data.close() #we close the file after we we are done with writing

#Plotting Part
data = open("data.txt","r") #we read the file

Earthx = [] 
Earthy = []
Sunx = []
Suny = []

for i in data: #we read each line from the file
    s = i.split()
    Earthx.append(float(s[0])) #we add the first column to x list
    Earthy.append(float(s[1])) #we add the second column to y list
    Sunx.append(float(s[2])) 
    Suny.append(float(s[3]))

data.close()

plt.plot(Earthx, Earthy, "-ro")
plt.plot(Sunx, Suny, "-bo")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.show()
