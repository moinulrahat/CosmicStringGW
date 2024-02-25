# -*- coding: utf-8 -*-
"""
This script is designed to run in a cluster for parallelizing the computation
over many k modes. If parallelization is not desired, use GWspectrumcalc.py
instead.

"""
import numpy as np
import multiprocessing
from dwboundedbycs import DWBoundedbyCS

defectGW = DWBoundedbyCS()

# specify the user parameters ----------------------
kmax = 10000 # how many k-modes to sum up to
Lambda_val = 1e12 # U(1) symmetry breaking scale
v_val = 246. # Intermediate Z2 breaking scale
# --------------------------------------------------

# evaluate GW spectrum for the frequency list flist, summing the k-modes
# from k = 1 up to k = kmax
def evaluate_parallel(Lambda, v, flist, klist):
    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        results = []
        # Apply the function to each element of blist in parallel
        for freq in flist:
            result_f = sum(pool.starmap(defectGW.OmegaGWcalcDWCS, [(Lambda, v, freq, kval) for kval in klist]))
            results.append(result_f)

    return results

if __name__ == "__main__":
    Lambda = Lambda_val
    v = v_val
    flist = np.logspace(-9, 5, 30)  # frequency in the observable range
    klist = range(1, kmax + 1)  # all k-modes

    omega_gw_spectrum = evaluate_parallel(Lambda, v, flist, klist)
    
    final_result = np.column_stack((flist,omega_gw_spectrum))

    print("GW spectrum vs frequency:", final_result)
    
    # save results in a text file
    np.savetxt(f'DWCSGW_{np.log10(Lambda_val)}_{v_val}.txt', final_result)
    
