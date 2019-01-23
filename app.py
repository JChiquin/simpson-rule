from __future__ import division
from math import e,pi

def standard(x,mean,standard_deviation):
    return (x-mean)/standard_deviation

def normal_distribution(x,mean,standard_deviation):
    Z = standard(x,mean,standard_deviation)
    result = (e**((-Z**2)/2))/(2*pi)**0.5
    return result

def simpson(mean, standard_deviation, n, b, a=float('-inf')):
    
    flagB= False
    flagA= False
    if a == float('-inf'):
        a = 0
        flagA = True
        if b < 0:
            b=-b
            flag = True

    h=(b-a)/n
    value = normal_distribution(a,mean,standard_deviation) #x0
    for i in range(2,n-1,2):
        x=a+i*h
        value += 2*normal_distribution(x,mean,standard_deviation)
    for i in range(1,n,2):
        x=a+i*h
        value += 4*normal_distribution(x,mean,standard_deviation)
    value += normal_distribution(b,mean,standard_deviation) #xn
    value *= (h/3)
    
    if flagA:
        if flagB:
            value = -value
        value += 0.5
        
    return value
    

if __name__ == '__main__':
    print "P(X<=5) simple: " + str(simpson(0,1,2,5))
    print "P(X<=5) compuesta: " + str(simpson(0,1,40,5))
    print "P(X<=-5) simple: " + str(simpson(0,1,2,-5))
    print "P(X<=-5) Compuesta: " + str(simpson(0,1,40,-5))
    print "P(2<=X<=7) simple: " + str(simpson(0,1,2,7,2))
    print "P(2<=X<=7) Compuesta: " + str(simpson(0,1,40,7,2))