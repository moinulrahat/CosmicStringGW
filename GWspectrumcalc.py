"""
This script calculates the GW spectrum. This is intended to be used in a local
computer for testing out the result for summing over small k-modes. For 30 frequency
bins, it takes couple of minutes for kmax = 2.

If parallelization is expected, use GWscanner.py 

"""
import numpy as np
from dwboundedbycs import DWBoundedbyCS

defectGW = DWBoundedbyCS()

kmax = 2

flist = np.logspace(-9, 5, 30)
result = np.array([0.] * len(flist))
for i in range(len(result)):
    result[i] = sum([defectGW.OmegaGWcalcDWCS(1e13, 246, flist[i], k) for k in range(1, kmax)])

print(np.column_stack((flist, result)))