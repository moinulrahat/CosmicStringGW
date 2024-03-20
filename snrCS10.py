import numpy as np
import warnings
import os
from snrgeneric import snr_LISA
from GWplotter import plot_all_interferometers
import matplotlib.pyplot as plt
# Suppress all warnings
warnings.filterwarnings("ignore") 

# Get the current working directory
current_dir = os.getcwd()

# Load and plot the pre-calculated GW spectrum.

# GW spectrum for U(1) breaking at 10^{15} GeV, Z2 breaking at 246 GeV
def get_CS_Lambda10():
    # Load the data from the text file
    file_path = os.path.join(current_dir, 'CSGW_10.0.txt')
    data = np.loadtxt(file_path)
    
    # separate the columns
    freq = data[:, 0]
    OmegaGW = data[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW_nonzero = OmegaGW[nonzero_indices]
    
    return freq_nonzero, OmegaGW_nonzero
    
f_list, Omega_list = get_CS_Lambda10()
print("SNR for $v = 10^{10}$ GeV \n", snr_LISA(f_list, Omega_list))

plt.loglog(f_list, Omega_list, color='purple', linewidth=2.2, linestyle='-')
plot_all_interferometers()
plt.show()