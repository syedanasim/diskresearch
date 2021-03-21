#from datetime import datetime
import time
from numpy import pi,cos,sin,arctan2,arcsin
import numpy as np
from numpy import loadtxt
import math
from math import e
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
from scipy.interpolate import interp1d
import scipy.interpolate as interpol
import sys
import os
#%matplotlib inline

#########################################################
'''Constant Parameters'''

TQM = "TQM"
SG = "SG"

s_BH = "s_BH"
stellar = "stellar"
m_star = "m_star"
g_star = "g_star"
o_star = "o_star"
r_giant = "r_giant"

#setting unit conversion values for distances
pc=3.1*10**16 #[m] meter #pc in meters #(pc) parsec
Rg=1.5*10**11 #[m] meter #rg in meters (for a BH of mass 10^8 Msun) #(rg) gravitational radius
Rs=2*Rg #[m] meter #rs in meters (also simply 3*10**11) #(rs) schwarzschild radius


#setting values of fundamental constants
G=6.67*(10**-11) #[(m**3)/(kg*(s**2))] cubic meter per kilogram second squared #(G) gravitational constant
M=(10**8)*1.99*(10**30) #[kg] kilogram #(M) mass of SMBH
year=3.154*10**7 #[s] second #(year) seconds per year
Cd=1 #[unit ?] #(Cd)
cs=10**4 #[m/s] meter per second #(cs) speed of sound
degrees=180/pi #for converting between radians and degrees

#setting paramenters of orbiting object
def Astar(rstar): #m^2 #area
    A=4*pi*(rstar**2)
    return A
def volstar(rstar): #m^3 #volume
    vol=(4/3)*pi*(rstar**3)
    return vol
def densitystar(mstar,rstar): #density
    den=mstar/volstar(rstar)
    return den

msun=1.989*(10**30) #[kg] kilogram #(msun) mass of our sun
rsun=6.957*(10**8) #[m] meter #(rsun) radius of our sun
densitysun=densitystar(msun,rsun)
#densitysun=1410 #[kg/m^3] kilogram per cubic meter #(densitysun) density of our sun
#Asun=4*pi*(rsun**2) #[m^2] meter squared #(Asun) area of our sun

mmstar=0.5*msun #[kg] kilogram #(mmstar) mass of m star
rmstar=0.4*rsun #[m] meter #(rmstar) radius of m star
densitymstar=densitystar(mmstar,rmstar)
#densitymstar=8806 #[kg/m^3] kilogram per cubic meter #(densitymstar) density of m star

mostar=50*msun #[kg] kilogram #(mostar) mass of o star
rostar=15*rsun #[m] meter #(rostar) radius of o star
densityostar=densitystar(mostar,rostar)
#densityostar=27.8 #[kg/m^3] kilogram per cubic meter #(densityostar) density of o star

mrgiant=1.5*msun #[kg] kilogram #(mrgiant) mass of red giant 
rrgiant=100* rsun #[m] meter #(rrgiant) radius of red giant
densityrgiant=densitystar(mrgiant,rrgiant)
#densityrgiant=2.81 #[kg/m^3] kilogram per cubic meter #(densityrgiant) density of red giant

m_sBH=10*msun #[kg] kilogram #(m_sBH) mass of stellar mass black hole

#########################################################
'''importing disk data for SG model'''

#importing data for logged (a,h/a)
hoverr_SG=loadtxt("diskdata/diskdataSG/hoverr.txt") #raw data

#(a) distance from SMBH
hars_SG=(10**hoverr_SG[:,0]) #[rs] schwarzschild radius #unlogged data #(a) distance from SMBH
ham_SG=Rs*hars_SG #[m] meter #for calculations #(a) distance from SMBH
harg_SG=ham_SG/Rg #[rg] gravitational radius #for plotting #(a) distance from SMBH

#(h/a) ratio of distances
hovera_SG=10**hoverr_SG[:,1] #[unitless] #unlogged #(h/a) ratio of distances

#(h) disk thickness
h_SG=ham_SG*hovera_SG #[m] meter #calculating thickness #(h) disk thickness
h_SG_interpolated = interpol.interp1d(ham_SG,h_SG)

#importing data for logged (a,surfacedensity)
surfacedensity_SG=loadtxt("diskdata/diskdataSG/SurfaceDensity.txt") #raw data

#(a) distance from SMBH
surfacedensityars_SG=(10**surfacedensity_SG[:,0]) #[rs] schwarzschild radius #unlogged data #(a) distance from SMBH
surfacedensityam_SG=Rs*surfacedensityars_SG #[m] meter #for calculations #(a) distance from SMBH
surfacedensityarg_SG=surfacedensityam_SG/Rg #[rg] gravitational radius #for plotting #(a) distance from SMBH

#(surfacedensity) disk surface density
surfacedensity_SG=10**surfacedensity_SG[:,1] #[g/(cm^2)] gram per centimeter squared #unlogged data #(surfacedensity) disk surface density
surfacedensity_SG_interpolated = interpol.interp1d(surfacedensityam_SG,surfacedensity_SG)

#(a) distance from SMBH
arslog_SG=loadtxt("diskdata/diskdataSG/a.txt") #raw data #compiled list of (a) values
ars_SG=(10**arslog_SG)#[rs] schwarzschild radius #unlogged data #(a) distance from SMBH
am_SG=Rs*ars_SG #[m] meter #for calculations #(a) distance from SMBH
arg_SG=am_SG/Rg #[rg] gravitational radius #for plotting #(a) distance from SMBH

#########################################################
'''importing disk data for TQM model'''

#importing data for logged (a,h/a)
hoverr_TQM=loadtxt("diskdata/diskdataTQM/hoverr.txt") #raw data

#(a) distance from SMBH
hapc_TQM=(10**hoverr_TQM[:,0]) #[pc] parsec #unlogged data #(a) distance from SMBH
ham_TQM=pc*hapc_TQM #[m] meter #for calculations #(a) distance from SMBH
harg_TQM=ham_TQM/Rg #[rg] gravitational radius #for plotting #(a) distance from SMBH

#(h/a) ratio of distances
hovera_TQM=10**hoverr_TQM[:,1] #[unitless] #unlogged data #(h/a) ratio of distances

#(h) disk thickness
h_TQM=ham_TQM*hovera_TQM #[m] meter #calculating thickness #(h) disk thickness
h_TQM_interpolated = interpol.interp1d(ham_TQM,h_TQM)

#importing data for logged (a,surfacedensity)
surfacedensity_TQM=loadtxt("diskdata/diskdataTQM/SurfaceDensity.txt") #raw data

#(a) distance from SMBH
surfacedensityapc_TQM=(10**surfacedensity_TQM[:,0]) #[pc] parsec #unlogged data #(a) distance from SMBH
surfacedensityam_TQM=pc*surfacedensityapc_TQM #[m] meter #for calculations #(a) distance from SMBH
surfacedensityarg_TQM=surfacedensityam_TQM/Rg #[rg] gravitational radius #for plotting #(a) distance from SMBH

#(surfacedensity) disk surface density
surfacedensity_TQM=10**surfacedensity_TQM[:,1] #[g/(cm^2)] gram per centimeter squared #unlogged data #(surfacedensity) disk surface density
surfacedensity_TQM_interpolated = interpol.interp1d(surfacedensityam_TQM,surfacedensity_TQM)

#(a) distance from SMBH
apclog_TQM=loadtxt("diskdata/diskdataTQM/a.txt") #raw data #compiled list of (a) values
apc_TQM=(10**apclog_TQM) #[pc] parsec #unlogged data #(a) distance from SMBH
am_TQM=pc*apc_TQM #[m] meter #for calculations #(a) distance from SMBH
arg_TQM=am_TQM/Rg #[rg] gravitational radius #for plotting #(a) distance from SMBH
#########################################################
am=[] #universal (within both models range)
for i in range(len(am_TQM[:50])):
    am.append(am_TQM[i])
for i in range(len(am_SG[12:])):
    am.append(am_SG[i+12])
am.sort()
#########################################################
'''funtion to help find the equation of a line on a log scale'''
def slope(dx, dy):
    return (dy / dx) if dx else None
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)
    def halfway(self, target):
        midx = (self.x + target.x) / 2
        midy = (self.y + target.y) / 2
        return Point(midx, midy)
    def distance(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        return (dx*dx + dy*dy) ** 0.5
    def reflect_x(self):
        return Point(-self.x,self.y)
    def reflect_y(self):
        return Point(self.x,-self.y)
    def reflect_x_y(self):
        return Point(-self.x, -self.y)
    def slope_from_origin(self):
        return slope(self.x, self.y)
    def slope(self, target):
        return slope(target.x - self.x, target.y - self.y)
    def y_int(self, target):       # <= here's the magic
        return self.y - self.slope(target)*self.x
    def line_equation(self, target):
        slope = self.slope(target)
        y_int = self.y_int(target)
        if y_int < 0:
            y_int = -y_int
            sign = '-'
        else:
            sign = '+'
        return '{}x {} {}'.format(slope, sign, y_int)
    def line_function(self, target):
        slope = self.slope(target)
        y_int = self.y_int(target)
        def fn(x):
            return slope*x + y_int
        return fn

'''interpolating h as a function of radius'''
#(h) interpolated disk thickness for TQM
def hint_TQM(am):
    a=am/Rg
    for i in range(len(harg_TQM)-1):
        j=i+1
        c = Point(harg_TQM[i],h_TQM[i])
        d = Point(harg_TQM[j],h_TQM[j])
        if ((a>=harg_TQM[i]) and (a<=harg_TQM[j])):
            y=(slope(harg_TQM[j]-harg_TQM[i],h_TQM[j]-h_TQM[i])*a)+(Point.y_int(c,d))
    return y
#(h) interpolated disk thickness for SG
def hint_SG(am):
    a=am/Rg
    for i in range(len(harg_SG)-1):
        j=i+1
        c = Point(harg_SG[i],h_SG[i])
        d = Point(harg_SG[j],h_SG[j])
        c_36 = Point(harg_SG[36],h_SG[36])
        d_37 = Point(harg_SG[37],h_SG[37])
        if ((a>=harg_SG[i]) and (a<=harg_SG[j])):
            y=(slope(harg_SG[j]-harg_SG[i],h_SG[j]-h_SG[i])*a)+(Point.y_int(c,d))
        if ((a>harg_SG[37]) and (a<=surfacedensityarg_SG[29])):
            y=(slope(harg_SG[37]-harg_SG[36],h_SG[37]-h_SG[36])*a)+(Point.y_int(c_36,d_37))
    return y
''' interpolating surfacedensity as a function of radius'''
#(surfacedensity) interpolated disk surface density for TQM
def surfacedensityint_TQM(am):
    a=am/Rg
    for i in range(len(surfacedensityarg_TQM)-1):
        j=i+1
        c = Point(surfacedensityarg_TQM[i],surfacedensity_TQM[i])
        d = Point(surfacedensityarg_TQM[j],surfacedensity_TQM[j])
        c_0 = Point(surfacedensityarg_TQM[0],surfacedensity_TQM[0])
        d_1 = Point(surfacedensityarg_TQM[1],surfacedensity_TQM[1])
        c_24 = Point(surfacedensityarg_TQM[24],surfacedensity_TQM[24])
        d_25 = Point(surfacedensityarg_TQM[25],surfacedensity_TQM[25])
        if ((a>=harg_TQM[0]) and (a<surfacedensityarg_TQM[0])):
            y=(slope(surfacedensityarg_TQM[1]-surfacedensityarg_TQM[0],surfacedensity_TQM[1]-surfacedensity_TQM[0])*a)+(Point.y_int(c_0,d_1))
        if ((a>=surfacedensityarg_TQM[i]) and (a<=surfacedensityarg_TQM[j])):
            y=(slope(surfacedensityarg_TQM[j]-surfacedensityarg_TQM[i],surfacedensity_TQM[j]-surfacedensity_TQM[i])*a)+(Point.y_int(c,d))
        if ((a>surfacedensityarg_TQM[25]) and (a<=harg_TQM[33])):
            y=(slope(surfacedensityarg_TQM[25]-surfacedensityarg_TQM[24],surfacedensity_TQM[25]-surfacedensity_TQM[24])*a)+(Point.y_int(c_24,d_25))
    return y
#(surfacedensity) interpolated disk surface density for SG
def surfacedensityint_SG(am):
    a=am/Rg
    for i in range(len(surfacedensityarg_SG)-1):
        j=i+1
        c = Point(surfacedensityarg_SG[i],surfacedensity_SG[i])
        d = Point(surfacedensityarg_SG[j],surfacedensity_SG[j])
        c_0 = Point(surfacedensityarg_SG[0],surfacedensity_SG[0])
        d_1 = Point(surfacedensityarg_SG[1],surfacedensity_SG[1])
        if ((a>=harg_SG[0]) and (a<surfacedensityarg_SG[0])):
            y=(slope(surfacedensityarg_SG[1]-surfacedensityarg_SG[0],surfacedensity_SG[1]-surfacedensity_SG[0])*a)+(Point.y_int(c_0,d_1))
        if ((a>=surfacedensityarg_SG[i]) and (a<=surfacedensityarg_SG[j])):
            y=(slope(surfacedensityarg_SG[j]-surfacedensityarg_SG[i],surfacedensity_SG[j]-surfacedensity_SG[i])*a)+(Point.y_int(c,d))
    return y
#########################################################
'''calculating density as a function of radius'''
#(density) calculated disk surface density
def density_SG(am): #creating a density function density with respect to radius
    #densitycal=surfacedensityint_SG(am)/(hint_SG(am)*100) #[g/(cm^3)] gram per cubic centimeter
    densitycal=surfacedensityint_SG(am)/hint_SG(am)*10 #[kg/(m^3)] kilogram per cubic meter 
    return densitycal
def density_TQM(am): #creating a density function density with respect to radius
    #densitycal=surfacedensityint_TQM(am)/(hint_TQM(am)*100) #[g/(cm^3)] gram per cubic centimeter
    densitycal=surfacedensityint_TQM(am)/hint_TQM(am)*10 #[kg/(m^3)] kilogram per cubic meter 
    return densitycal
#########################################################
'''Here things depend on both the position of the object, as well as the disk model'''

'''calculating arc length, or distance traveled in disk'''
def arc(i,am,hint): #creating function for arc length as function of i & radius
    s=2*am*arcsin(hint(am)/(2*am*sin(i)))
    return abs(s) #meters

'''calculating time traveled in disk'''
def Tdisk(i,am,hint): #creating function for time in disk Tdisk as function of i & a !!! CHECK THIS; i recall it being off by (an extra) factor of pi
    #tdisk=(2*hint(arg)*Torb(am))/circ(am) #currently assumes fixed inclination angle=pi/2 #needs to be a func of i
    t=(arc(i,am,hint)/circ(am))*Torb(am)
    return t #seconds

'''ratio of Time in disk vs Time of orbit'''
def Tratio(i,am,hint): #creating function for time ratio
    ratio=Tdisk(i,am,hint)/Torb(am)
    return ratio #unitless

'''setting limits on inclination, where object is considered within disk height'''
def imin(am,hint): #radians
    i_min=arcsin(hint(am)/(2*am))
    return i_min
def imax(am,hint): #radians
    i_max=pi-arcsin(hint(am)/(2*am))
    return i_max
def ivals(am,hint):
    #vals=np.linspace(imin(am,hint)+0.1,imax(am,hint),20)
    prograde=np.linspace(imin(am,hint),pi/2,1000)
    return prograde

#mutual a values: #within bounds of both SG & TQM #use only when necessary
arg=surfacedensityarg_SG[4:]
am=surfacedensityam_SG[4:]

#########################################################
'''The following parameters are independent of the disk model & depend only on the position of the orbiting object'''

def vel(am): #keplerian velocity v as function of radius #input a in meters
    speed=((2*G*M/am)**0.5) #m/s
    return speed

'''v rel components''' # keplarian velocity components wrt disk plane and orbit plane
def vktheta(i,am):#m/s
    kcomp=vel(am)*cos(i)
    return kcomp
def vkz(i,am):#m/s
    kcomp=vel(am)*sin(i)
    return kcomp
# relative velocity component-wise
def vrtheta(i,am):#m/s

    while (i < 0):
        i = i + 2*pi
    while (i > 2*pi):
        i = i - 2*pi

    if i<=pi/2:
        thetacomp=vel(am)-vktheta(i,am)
    if i>=pi/2:
        thetacomp=vktheta(i,am)-vel(am)
    return thetacomp
def vrz(i,am):#m/s
    rcomp=vkz(i,am)
    return rcomp
def vrel(i,am):#m/s
    rtot= ((vrtheta(i,am)**2)+(vkz(i,am)**2))**0.5
    return rtot

def circ(am): #creating function for circumference as a fuction of radius
    c=2*pi*am
    return c #meters

def Torb(am): #creating function for time of orbit Torb as function of radius #input radius in meters
    torb=(circ(am))/(vel(am)) 
    return torb #units of seconds
    
def rBH(i,am): #r bondi
    r=(2*G*m_sBH)/((vrz(i,am)**2)+(cs**2))
    return r
#r_sBH=rBH(pi/4,(10**4)*Rg)
#density_sBH=densitystar(m_sBH,r_sBH)

def omega(am):
    orbfreq = (G*M/(am**3))**(0.5)
    return orbfreq

def csound(am,hint):
    soundspeed = hint(am)*omega(am)
    return soundspeed

'''Here things depend on the position of the object, its other properties(ie mass, rad, etc.), as well as the model'''

# Energy of orbit Eorb
def Eorb(am,mstar): #creating function for energy of orbit Eorb as function of radius #input radius in meters
    eorb=(-G*M*mstar/(2*am))
    return eorb #units of joules

# Stokes Drag Force component-wise
def Ftheta_STO(i,am,rstar,density):#N (kgm/s^2)
    force=(Astar(rstar)*Cd/2)*density(am)*(vrtheta(i,am)**2)
    return force
def Fz_STO(i,am,rstar,density):#N (kgm/s^2)
    force=np.sign(i)*(Astar(rstar)*Cd/2)*density(am)*(vrz(i,am)**2)
    return force
def F_STO(i,am,rstar,density):#N (kgm/s^2)
    force=((Ftheta_STO(i,am,rstar,density)**2)+(Fz_STO(i,am,rstar,density)**2))**0.5
    return force

# Bondi-Hoyle-Littleton Drag Force component-wise
def Ftheta_BHL(i,am,rstar,density):#N (kgm/s^2)
    force=4*pi*(G**2)*(m_sBH**2)*density(am)*(vrtheta(i,am)**-2)
    return force
def Fz_BHL(i,am,rstar,density):#N (kgm/s^2)
    force=np.sign(i)*4*pi*(G**2)*(m_sBH**2)*density(am)*(vrz(i,am)**-2)
    return force
def F_BHL(i,am,rstar,density):#N (kgm/s^2)
    force=((Ftheta_BHL(i,am,rstar,density)**2)+(Fz_BHL(i,am,rstar,density)**2))**0.5
    return force

# Ostriker's Dynamical Drag Force component-wise
def Ftheta_DYN(i,am,rstar,density,hint):#N (kgm/s^2)
    force=4*pi*(G**2)*(m_sBH**2)*density(am)*(vrtheta(i,am)**-2)*np.log(arc(i,am,hint)/rBH(i,am))
    return force
def Fz_DYN(i,am,rstar,density,hint):#N (kgm/s^2)
    force=4*pi*(G**2)*(m_sBH**2)*density(am)*(vrz(i,am)**-2)*np.log(arc(i,am,hint)/rBH(i,am))
    return force
def F_DYN(i,am,rstar,density,hint):#N (kgm/s^2)
    force=((Ftheta_DYN(i,am,rstar,density,hint)**2)+(Fz_DYN(i,am,rstar,density,hint)**2))**0.5
    return force

#use mass of orbiters to set parameter!!!
#def Ftheta (name):
#    'STO'=1
#    'BHL'=2
#    if name=1
#        force=(Astar(rstar)*Cd/2)*density(am)*(vrtheta(i,am)**2)
#    if name=2    
#        force=4*pi*(G**2)*(m_sBH**2)*density(am)*(vrtheta(i,am)**-2)
#    return force
#def Fz (name):
#    'STO'=1
#    'BHL'=2
#    if name=1
#        force=(Astar(rstar)*Cd/2)*density(am)*(vrz(i,am)**2)
#    if name=2    
#        force=4*pi*(G**2)*(m_sBH**2)*density(am)*(vrz(i,am)**-2)
#    return force

#########################################################
'''Estimating Capture-Time: Tcap = n * Torb ''' #old 2017 formula

def n_STO(i,am,rstar,densitystar,hint,density): #num orbits assuming constant radius
    #n=((3*pi/4)*(density(am)/densitystar)*(am/rstar)*sin(i)*arcsin(hint(am)/(2*am*sin(i))))**(-1)
    n=(4*rstar*densitystar)/(3*pi*am*density(am)*sin(i)*arcsin(hint(am)/(2*am*sin(i))))
    return n
def n_BHL(i,am,hint,density): #num orbits assuming constant radius
    #n=(8*pi**2*(G**2)*m_sBH*density(am)*(am/(vel(am)**4*sin(i)**3))*arcsin(hint(am)/(2*am*sin(i))))**(-1)
    n=((vel(am)**4)*(sin(i)**3))/(8*(pi**2)*am*(G**2)*m_sBH*density(am)*arcsin(hint(am)/(2*am*sin(i))))
    return n

def n_DYN(i,am,hint,density): #num orbits assuming constant radius
    n=((vel(am)**4)*(sin(i)**3))/(8*pi*am*(G**2)*m_sBH*density(am)*arcsin(hint(am)/(2*am*sin(i)))*np.log(arc(i,am,hint)/rBH(i,am)))
    return n

def Tcap_estim_STO(i,am,rstar,densitystar,hint,density): #Tcap assuming constant radius
    t=n_STO(i,am,rstar,densitystar,hint,density)*Torb(am)
    years=t/year
    return years

def Tcap_estim_BHL(i,am,hint,density): #Tcap assuming constant radius
    t=n_BHL(i,am,hint,density)*Torb(am)
    years=t/year
    return years

def Tcap_estim_DYN(i,am,hint,density): #Tcap assuming constant radius
    t=n_DYN(i,am,hint,density)*Torb(am)
    years=t/year
    return years

#########################################################
'''WORK'''
def Wtheta_STO(i,am,rstar,density,hint):
    work=Ftheta_STO(i,am,rstar,density)*(arc(i,am,hint)*cos(i))
    return work
def Wz_STO(i,am,rstar,density,hint):
    work=Fz_STO(i,am,rstar,density)*(arc(i,am,hint)*sin(i))
    return work
def Worb_STO(i,am,rstar,density,hint):
    work=((Wtheta_STO(i,am,rstar,density,hint)**2)+(Wz_STO(i,am,rstar,density,hint)**2))**0.5
    return work

def Wtheta_BHL(i,am,rstar,density,hint):
    work=Ftheta_BHL(i,am,rstar,density)*(arc(i,am,hint)*cos(i))
    return work
def Wz_BHL(i,am,rstar,density,hint):
    work=Fz_BHL(i,am,rstar,density)*(arc(i,am,hint)*sin(i))
    return work
def Worb_BHL(i,am,rstar,density,hint):
    work=((Wtheta_BHL(i,am,rstar,density,hint)**2)+(Wz_BHL(i,am,rstar,density,hint)**2))**0.5
    return work

def Wtheta_DYN(i,am,rstar,density,hint):
    work=Ftheta_DYN(i,am,rstar,density,hint)*(arc(i,am,hint)*cos(i))
    return work
def Wz_DYN(i,am,rstar,density,hint):
    work=Fz_DYN(i,am,rstar,density,hint)*(arc(i,am,hint)*sin(i))
    return work
def Worb_DYN(i,am,rstar,density,hint):
    work=((Wtheta_DYN(i,am,rstar,density,hint)**2)+(Wz_DYN(i,am,rstar,density,hint)**2))**0.5
    return work

'''new Eorb'''
def newEorb_STO(i,am,mstar,rstar,density,hint): #function for new energy of orbit Eorb as function of radius #input radius in meters
    eorb=Eorb(am,mstar)-Worb_STO(i,am,rstar,density,hint)
    return eorb #units of joules

def newEorb_BHL(i,am,mstar,rstar,density,hint): #function for new energy of orbit Eorb as function of radius #input radius in meters
    eorb=Eorb(am,mstar)-Worb_BHL(i,am,rstar,density,hint)
    return eorb #units of joules

'''new a'''
def a_new_STO(i,am,mstar,rstar,density,hint):
    radius=(-G*M*mstar)/(2*newEorb_STO(i,am,mstar,rstar,density,hint)) #meters
    return radius

def a_new_BHL(i,am,mstar,rstar,density,hint):
    radius=(-G*M*mstar)/(2*newEorb_BHL(i,am,mstar,rstar,density,hint)) #meters
    return radius


def dvz_STO(i,am,rstar,mstar,density,hint): #m/s
    change=Fz_STO(i,am,rstar,density)*Tdisk(i,am,hint)/mstar
    return change
def dvtheta_STO(i,am,rstar,mstar,density,hint): #m/s
    change=Ftheta_STO(i,am,rstar,density)*Tdisk(i,am,hint)/mstar
    return change

def dvz_BHL(i,am,rstar,mstar,density,hint): #m/s
    change=Fz_BHL(i,am,rstar,density)*Tdisk(i,am,hint)/mstar
    return change
def dvtheta_BHL(i,am,rstar,mstar,density,hint): #m/s
    change=Ftheta_BHL(i,am,rstar,density)*Tdisk(i,am,hint)/mstar
    return change


def vktheta_new_STO(i_in,am_in,rstar,mstar,density,hint):
    new=vktheta(i_in,am_in)+dvtheta_STO(i_in,am_in,rstar,mstar,density,hint) #initial kep vel + del kep vel
    return new
def vkz_new_STO(i_in,am_in,rstar,mstar,density,hint):
    new=vkz(i_in,am_in)-dvz_STO(i_in,am_in,rstar,mstar,density,hint) #initial kep vel - del kep vel
    return new
def i_new_STO(i_in,am_in,mstar,rstar,density,hint):
    new=arctan2(vkz_new_STO(i_in,am_in,rstar,mstar,density,hint),vktheta_new_STO(i_in,am_in,rstar,mstar,density,hint))
    return new
def vk_new_STO(i_in,am_in,rstar,mstar,density,hint):
    new=(((vktheta_new_STO(i_in,am_in,rstar,mstar,density,hint))**2)+((vkz_new_STO(i_in,am_in,rstar,mstar,density,hint))**2))**0.5
    return new

def vktheta_new_BHL(i_in,am_in,rstar,mstar,density,hint):
    new=vktheta(i_in,am_in)+dvtheta_BHL(i_in,am_in,rstar,mstar,density,hint) #initial kep vel + del kep vel
    return new
def vkz_new_BHL(i_in,am_in,rstar,mstar,density,hint):
    new=vkz(i_in,am_in)-dvz_BHL(i_in,am_in,rstar,mstar,density,hint) #initial kep vel - del kep vel
    return new
def i_new_BHL(i_in,am_in,mstar,rstar,density,hint):
    new=arctan(vkz_new_BHL(i_in,am_in,rstar,mstar,density,hint)/vktheta_new_BHL(i_in,am_in,rstar,mstar,density,hint))
    #print(i_in)
    return new
def vk_new_BHL(i_in,am_in,rstar,mstar,density,hint):
    new=(((vktheta_new_BHL(i_in,am_in,rstar,mstar,density,hint))**2)+((vkz_new_BHL(i_in,am_in,rstar,mstar,density,hint))**2))**0.5
    return new

#########################################################
#Capture-Time assuming changing radius
def Tcapture(deg,radius,star,intermediate,disk,name): 
    start_time = time.time()
    i= deg/degrees
    am= radius*Rg
    if (disk in SG) == True:
        density = density_SG
        hint = hint_SG
        amin=surfacedensityam_SG[0]
    if (disk in TQM) == True:
        density = density_TQM
        hint = hint_TQM
        amin=surfacedensityam_TQM[0]
        
    if (star in s_BH) == True:
        mstar=m_sBH
        rstar=rBH(i,am)
    if (star in m_star) == True:
        mstar=mmstar
        rstar=rmstar
    if (star in g_star) == True:
        mstar=msun
        rstar=rsun
    if (star in o_star) == True:
        mstar=mostar
        rstar=rostar
    if (star in r_giant) == True:
        mstar=mrgiant
        rstar=rrgiant
    
    n=0
    t_sum=0
    initial_i=i
    initial_a=am
    min_i=imin(am,hint)
    new_i=i
    new_a=am
    data=[[],[],[],[]]
    data[0].append(initial_a)
    data[1].append(initial_i*degrees)
    data[2].append(0)
    data[3].append(0)
    condition1=True
    condition2=True
    condition3=True
    while condition1==True and condition2==True: #and condition3==True:
        n=n+1
        dt=Torb(new_a)/2
        t_sum=t_sum+dt
        if mstar==m_sBH:
            new_i=i_new_BHL(initial_i,initial_a,mstar,rstar,density,hint)
            new_a=a_new_BHL(initial_i,initial_a,mstar,rstar,density,hint)            
        else:
            new_i=i_new_STO(initial_i,initial_a,mstar,rstar,density,hint)
            new_a=a_new_STO(initial_i,initial_a,mstar,rstar,density,hint)
        min_i=imin(new_a,hint)
        initial_i=new_i
        initial_a=new_a
        if new_a<=amin: #6*Rg:
            condition1=False
        if (np.abs(new_i)<=np.abs(min_i)):
            condition2=False
        if (np.abs(new_i)<=np.abs(i)/e):
            condition3=False
            #print("n =",n,"t_sum =", t_sum/year,"years"," condition3 =",condition3)
        if n%intermediate==0:
            #print("n =",n,"t_sum =", t_sum/year, "years")
            #print("a =",new_a/Rg,"i =",new_i*degrees)
            data[0].append(new_a)
            data[1].append(new_i*degrees)
            data[2].append(n)
            data[3].append(t_sum/year)
        continue 
    else:
        print("condition1 =",condition1,"condition2 =",condition2,"condition3 =",condition3)
        print("final a =", new_a/Rg)
        print("final i =", new_i*degrees)
        print("number of passes through disk (n) =", n)
        print("grind time =",t_sum/year,"years")
        end_time=time.time()
        processingtime=(end_time - start_time)
        hours=processingtime//3600
        secsremaining=processingtime%3600
        minutes=secsremaining//60
        seconds=secsremaining%60        
        print("Processing time =", hours,'[hr] ',minutes,'[min] ',seconds,'[sec]')
        runtime=[hours,minutes,seconds]
        years=t_sum/year
        data[0].append(new_a)
        data[1].append(new_i*degrees)
        data[2].append(n)
        data[3].append(t_sum/year)
#
# the os package allows one to use unix commands in python. These line
# are testing if the directory exists, and if it does not, it creates it
#

        if not os.path.exists('capturedata/capturedata'+disk):
            os.makedirs('capturedata/capturedata'+disk)
        np.savetxt('./capturedata_'+name+'.txt', data, delimiter=' ')

        if not os.path.exists('capturedata/processingtime'):
            os.makedirs('capturedata/processingtime')
        np.savetxt('./processingtime_'+name+'.txt', runtime)

        #print(data)
        return years
#########################################################
