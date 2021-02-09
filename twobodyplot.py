from matplotlib import pyplot as plt
import numpy



sunx = numpy.loadtxt("results.txt", usecols= 0)
suny =  numpy.loadtxt("results.txt", usecols= 1)


earthx = numpy.loadtxt("results.txt", usecols= 2)
earthy = numpy.loadtxt("results.txt", usecols= 3)



plt.plot(sunx, suny, "rs")
plt.plot(earthx, earthy)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.legend(("The Sun", "The Earth"))
plt.show()
