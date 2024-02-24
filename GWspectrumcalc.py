# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:06:01 2024

@author: rahat

GWspectrumcalc.py
"""
import numpy as np
from dwboundedbycs import DWBoundedbyCS

defectGW = DWBoundedbyCS()

kmax = 100

flist = np.logspace(-9, 5, 30)
result = np.array([0.] * len(flist))
for i in range(len(result)):
    result[i] = sum([defectGW.OmegaGWcalcDWCS(1e13, 246, flist[i], k) for k in range(1, kmax)])

print(np.vstack(flist, result))