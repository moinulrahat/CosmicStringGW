# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:56:38 2024

@author: rahat
"""
import numpy as np
import multiprocessing
from dwboundedbycs import DWBoundedbyCS

defectGW = DWBoundedbyCS()
kmax = 10
Lambda_val = 1e13
v_val = 246.


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
    Lambda = 1e13  # Example value for 'a'
    v = 246.
    kmax = 10
    flist = np.logspace(-9, 5, 30)  # Example list for 'b'
    klist = range(1, kmax + 1)  # Example list for 'c'

    total_result = evaluate_parallel(Lambda, v, flist, klist)
    print("Total result:", total_result)

