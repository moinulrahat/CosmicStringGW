# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:44:13 2024

@author: rahat
"""

from scipy.interpolate import interp1d
import numpy as np
import sympy as sp
import scipy.integrate as spi
import scipy.optimize as spo
import scipy.special as sps
import os
# Get the directory of the current Python script
current_directory = os.path.dirname(os.path.abspath("__file__"))

# Set the current working directory to the directory of the Python script
os.chdir(current_directory)

# define parameters
cmitoGeV = 1.98e-14
HztoGeV = 6.58e-25
G = 6.70883e-39
h = 0.679
rhocrit = 1.053672e-5 * h**2 * cmitoGeV**3
t0 = 13.8e9 * 365.25 * 24 * 60 * 60 / HztoGeV
tF = 1e-22 / HztoGeV
zeq = 3360
teq = t0 / (1+zeq) ** (3./2)
CeffR = 5.7
CeffM = 0.5
Ceff = lambda t: CeffR if t < teq else CeffM
F = 0.1
alpha = 0.1
GammaS = 50
xi = 2
Mpl = 2.4e18
Cc = 1 / np.sqrt(8 * np.pi ** 3 * 106.75 / 90)

# import scale factor a as a function of time in GeV^-1
adata = np.loadtxt("a_evolution_in_Standard_cosmology.dat")
ax = adata[:, 0]
ay = adata[:, 1]
ascalef = interp1d(ax, ay, kind='linear')    

# define Gamma for the hybrid defect
x, q, r, s = sp.symbols('x q r s')
Gammainterp = sp.lambdify(x, q*x**2 + r*x + s)
Gammainterpdiff = sp.lambdify(x, sp.diff(Gammainterp(x), x))

eq1 = sp.Eq(Gammainterp(1.e-3), GammaS)
eq2 = sp.Eq(Gammainterpdiff(1.e-3), 0)
eq3 = sp.Eq(Gammainterp(100.), 3.7 * 100**2)

solution = sp.solve((eq1, eq2, eq3), (q, r, s))

Gammaint = lambda x: solution[q]*x**2 + solution[r]*x**2 + solution[s]

# function to calculate GW spectrum
def OmegaGWcalcDWCS(Lambda, v, freq, k):
    Rc = Lambda ** 2 / v ** 3
    tDW = Mpl * Cc / v ** 2
    tstar = max(Rc, tDW)
    Gmu = G * Lambda**2
    f = freq * HztoGeV

    # calculate the time when a loop was created
    def tiDWCS(tt):
        integrand = lambda lp: (1 + lp / (2*np.pi*Rc)) / Gammaint(lp / (2*np.pi*Rc))
        equation = lambda tik: spi.quad(integrand, (xi * k) / f * ascalef(tt) / ascalef(t0), alpha * tik)[0] - Gmu * (tt - tik)
        return spo.brentq(equation, (xi * k) / (alpha * f) * ascalef(tt) / ascalef(t0), tt, maxiter = 1000) \
                                            if (alpha * tt >= (xi * k) / f * ascalef(tt) / ascalef(t0)) \
                                            else 0
        # The loops being created at tt must have larger size than the loops \
        # already emitting GW at tt .
    #print(tiDWCS(t0 * 1e-10))

    zeta_value = sps.zeta(4./3)
    Pk = k ** (-4./3) / zeta_value
    prefactor = Gmu ** 2 / (G * rhocrit)

    def OmegaintegrandDWCS(tt):
        tk = tiDWCS(tt)
        print("This is tk = ", tk)
        Ogintegrand = (ascalef(tt) / ascalef(t0))**5 * F * Ceff(tk) / (alpha * tk**4.) * \
                      (ascalef(tk) / ascalef(tt))**3 * (Pk * xi * k / f) * \
                      (1. + xi * k / (2 * np.pi * Rc * f) * (ascalef(tt) / ascalef(t0))) * \
                      Gammaint(alpha * tk / (2 * np.pi * Rc)) / \
                      (Gammaint(alpha * tk / (2 * np.pi * Rc)) * Gmu + alpha * (1 + alpha * tk / (2 * np.pi * Rc))) \
                      if (tk != 0 and tstar > tk) else 0
        return Ogintegrand
    ttlist = np.linspace(np.log(tF), np.log(t0), num = 5)
    Omegalist = np.array([0.] * len(ttlist))
    for i in range(len(ttlist)):
        Omegalist[i] = (OmegaintegrandDWCS(np.exp(ttlist[i]))) 
        
    nonzero_indices = np.nonzero(Omegalist)[0]   
    Omegatable = np.log(np.array(Omegalist[nonzero_indices]))
    tttable = np.array(ttlist[nonzero_indices])
    
    if len(nonzero_indices) > 0:
        Omegainterp = interp1d(tttable, np.exp(Omegatable + tttable), kind='linear')
        def Omegainterpintegrand(x):
            return Omegainterp(x)
        result = prefactor * h**2 * spi.quad(Omegainterpintegrand, tttable[0], tttable[-1])[0]
        return result
    else:
        return 0

print(OmegaGWcalcDWCS(1e13, 246, 1, 1))
'''
run = 1
factor = 5
flist = np.logspace(-9, 5, num = 14)
klist = list(range((run - 1) * factor + 1, run * factor + 1))

results = np.array([0.] * len(flist))


if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
        for i in range(len(flist)):
            results[i] = sum(pool.starmap(OmegaGWcalcDWCS, [(1e12, 246, flist[i], k) for k in klist]))        
    pool.close()
    pool.join()            
print(results)


import matplotlib.pyplot as plt
plt.loglog(flist, results)
plt.xlabel('f [Hz]')
plt.ylabel('$\Omega_{GW}h^2$')
plt.show()
'''