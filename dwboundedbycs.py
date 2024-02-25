# -*- coding: utf-8 -*-
"""
This script defines the essential functions for calculating GW spectrum for the
hybrid defect called domain walls bounded by cosmic strings. The parameter values
and the formula are taken from section VII of the following reference:
    
\bibitem{Dunsky:2021tih}
D.~I.~Dunsky, A.~Ghoshal, H.~Murayama, Y.~Sakakihara and G.~White,
%``GUTs, hybrid topological defects, and gravitational waves,''
Phys. Rev. D \textbf{106}, no.7, 075030 (2022)
doi:10.1103/PhysRevD.106.075030
[arXiv:2111.08750 [hep-ph]].

"""

from scipy.interpolate import interp1d
import numpy as np
import sympy as sp
import scipy.integrate as spi
import scipy.optimize as spo
import scipy.special as sps

class DWBoundedbyCS:
    def __init__(self):
        # first we initialize the constants
        self.cmitoGeV = 1.98e-14 # converts 1/cm to GeV
        self.HztoGeV = 6.58e-25 # converts 1/s to GeV
        self.G = 6.70883e-39 # Newton's constant
        self.h = 0.679 
        self.rhocrit = 1.053672e-5 * self.h**2 * self.cmitoGeV**3 # critical energy density
        self.t0 = 13.8e9 * 365.25 * 24 * 60 * 60 / self.HztoGeV # present time
        self.tF = 1e-22 / self.HztoGeV # initial string formation time
        self.zeq = 3360 # z at matter-radiation equality
        self.teq = self.t0 / (1+self.zeq) ** (3./2) # time at matter-radiation equality
        self.CeffR = 5.7 # Ceff at radiation-dominated era
        self.CeffM = 0.5 # Ceff at matter-dominated era
        self.F = 0.1
        self.alpha = 0.1
        self.GammaS = 50
        self.xi = 2
        self.Mpl = 2.4e18
        self.zeta_value = sps.zeta(4./3)
        self.Cc = 1 / np.sqrt(8 * np.pi ** 3 * 106.75 / 90)
        # import scale factor a as a function of time in GeV^-1
        self.adata = np.loadtxt("a_evolution_in_Standard_cosmology.dat")
        self.ax = self.adata[:, 0]
        self.ay = self.adata[:, 1]
        self.ascalef = interp1d(self.ax, self.ay, kind='linear') # interpolation of scale factor
        self.q, self.r, self.s = self.Gamma_interp()
    
    def Ceff(self, t):
        return self.CeffR if t < self.teq else self.CeffM
    
    # define Gamma_s for the hybrid defect fitting the curve of Fig. 14
    # of the above reference
    def Gamma_interp(self):
        x, q, r, s = sp.symbols('x q r s')
        Gammainterp = sp.lambdify(x, q*x**2 + r*x + s)
        Gammainterpdiff = sp.lambdify(x, sp.diff(Gammainterp(x), x))
        eq1 = sp.Eq(Gammainterp(1.e-3), self.GammaS)
        eq2 = sp.Eq(Gammainterpdiff(1.e-3), 0)
        eq3 = sp.Eq(Gammainterp(100.), 3.7 * 100**2)
        solution = sp.solve((eq1, eq2, eq3), (q, r, s))        
        return float(solution[q]), float(solution[r]), float(solution[s])
    
    def Gamma_s(self, r_over_rc):
        return self.q * r_over_rc**2 + self.r * r_over_rc + self.s
    
    # calculate the time when a loop emitting GW at time tt was created
    def tiDWCS(self, Gmu, tt, Rc, k, f):
        integrand = lambda lp: (1 + lp / (2*np.pi*Rc)) / self.Gamma_s(lp / (2*np.pi*Rc))
        equation = lambda tik: spi.quad(integrand, (self.xi * k) / f * \
                        self.ascalef(tt) / self.ascalef(self.t0), self.alpha * tik, limit=100)[0] - \
                        Gmu * (tt - tik)
        return spo.brentq(equation, (self.xi * k) / (self.alpha * f) * \
                          self.ascalef(tt) / self.ascalef(self.t0), tt, maxiter = 1000) \
                          if (self.alpha * tt >= (self.xi * k) / f * \
                              self.ascalef(tt) / self.ascalef(self.t0)) \
                                            else 0
        # The loops being created at tt must have larger size than the loops \
        # already emitting GW at tt .
    
    # calculate the integrand
    def OmegaintegrandDWCS(self, Gmu, tt, tstar, Rc, k, f):
        tk = self.tiDWCS(Gmu, tt, Rc, k, f)
        Pk = k ** (-4./3) / self.zeta_value
        Ogintegrand = (self.ascalef(tt) / self.ascalef(self.t0))**5 * self.F * self.Ceff(tk) / (self.alpha * tk**4.) * \
                      (self.ascalef(tk) / self.ascalef(tt))**3 * (Pk * self.xi * k / f) * \
                      (1. + self.xi * k / (2 * np.pi * Rc * f) * (self.ascalef(tt) / self.ascalef(self.t0))) * \
                      self.Gamma_s(self.alpha * tk / (2 * np.pi * Rc)) / \
                      (self.Gamma_s(self.alpha * tk / (2 * np.pi * Rc)) * Gmu + self.alpha * (1 + self.alpha * tk / (2 * np.pi * Rc))) \
                      if (tk != 0 and tstar > tk) else 0
        return Ogintegrand
    
    # perform the integration to calculate the GW amplitude
    def OmegaGWcalcDWCS(self, Lambda, v, freq, k):
        Rc = Lambda ** 2 / v ** 3
        tDW = self.Mpl * self.Cc / v ** 2
        tstar = max(Rc, tDW)
        Gmu = self.G * Lambda**2
        f = freq * self.HztoGeV
        
        prefactor = Gmu ** 2 / (self.G * self.rhocrit)
        
        # integrand
        ttlist = np.linspace(np.log(self.tF), np.log(self.t0), num = 300)
        Omegalist = np.array([0.] * len(ttlist))
        for i in range(len(ttlist)):
            Omegalist[i] = (self.OmegaintegrandDWCS(Gmu, np.exp(ttlist[i]), tstar, Rc, k, f)) 
           
        nonzero_indices = np.nonzero(Omegalist)[0]   
        Omegatable = np.log(np.array(Omegalist[nonzero_indices]))
        tttable = np.array(ttlist[nonzero_indices])
        
        # integration in log-log space
        if len(nonzero_indices) > 0:
            Omegainterp = interp1d(tttable, np.exp(Omegatable + tttable), kind='linear')
            def Omegainterpintegrand(x):
                return Omegainterp(x)
            result = prefactor * self.h**2 * spi.quad(Omegainterpintegrand, tttable[0], tttable[-1])[0]
            return result
        else:
            return 0
    
    

    

