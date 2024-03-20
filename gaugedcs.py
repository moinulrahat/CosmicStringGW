# -*- coding: utf-8 -*-
"""
This script defines the essential functions for calculating GW spectrum from 
gauged cosmic strings. The parameter values and the formula are taken from 
section VII of the following reference:
    
\bibitem{Dunsky:2021tih}
D.~I.~Dunsky, A.~Ghoshal, H.~Murayama, Y.~Sakakihara and G.~White,
%``GUTs, hybrid topological defects, and gravitational waves,''
Phys. Rev. D \textbf{106}, no.7, 075030 (2022)
doi:10.1103/PhysRevD.106.075030
[arXiv:2111.08750 [hep-ph]].

"""

from scipy.interpolate import interp1d
import numpy as np
import scipy.integrate as spi
import scipy.special as sps

class CosmicString:
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
    
    def Ceff(self, t):
        return self.CeffR if t < self.teq else self.CeffM
    
    
    def Gamma_s(self):
        return self.GammaS
    
    # calculate the time when a loop emitting GW at time tt was created
    def tiCS(self, Gmu, tt, k, f):
        return 1 / (self.alpha + self.GammaS*Gmu) * (2*k/f * self.ascalef(tt) / self.ascalef(self.t0) + self.GammaS * Gmu * tt) \
                          if (self.alpha * tt >= (self.xi * k) / f * \
                              self.ascalef(tt) / self.ascalef(self.t0)) \
                                            else 0
        # The loops being created at tt must have larger size than the loops \
        # already emitting GW at tt .
    
    # calculate the integrand
    def OmegaintegrandCS(self, Gmu, tt, k, f):
        tk = self.tiCS(Gmu, tt, k, f)
        Pk = k ** (-4./3) / self.zeta_value
        Ogintegrand = (self.ascalef(tt) / self.ascalef(self.t0))**5 * self.F * self.Ceff(tk) / (self.alpha * tk**4.) * \
                      (self.ascalef(tk) / self.ascalef(tt))**3 * (Pk * self.xi * k / f) * \
                      self.GammaS / (self.alpha + self.GammaS* Gmu) \
                      if (tk != 0) else 0
        return Ogintegrand
    
    # perform the integration to calculate the GW amplitude
    def OmegaGWcalcCS(self, Lambda, freq, k):
        Gmu = self.G * Lambda**2
        f = freq * self.HztoGeV
        
        prefactor = Gmu ** 2 / (self.G * self.rhocrit)
        
        # integrand
        ttlist = np.linspace(np.log(self.tF), np.log(self.t0), num = 300)
        Omegalist = np.array([0.] * len(ttlist))
        for i in range(len(ttlist)):
            Omegalist[i] = (self.OmegaintegrandCS(Gmu, np.exp(ttlist[i]), k, f)) 
           
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
    
    

    

