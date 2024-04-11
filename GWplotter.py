# -*- coding: utf-8 -*-
"""
This file plots the GW spectrum from pre-calculated data using GWscanner.py,
along with various interferometer sensitivities/upper bounds/observations.
"""

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import os
from plotinterferometer import plot_all_interferometers

# Get the current working directory
current_dir = os.getcwd()

# Define the name of the folder containing the data
folder_name = '2hdmGWdata'

# Now we load and plot the pre-calculated GW spectrum.

# GW spectrum for U(1) breaking at 10^{12} GeV, Z2 breaking at 246 GeV
def plot_Lambda12():
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_12.0_246.0.txt')
    data12 = np.loadtxt(file_path)
    
    # separate the columns
    freq = data12[:, 0]
    OmegaGW12 = data12[:, 1]
    
    # pure CS case
    file_path = os.path.join(current_dir, folder_name, 'CSGW_12.0.txt')
    dataCS12 = np.loadtxt(file_path)
    
    # separate the columns
    freqCS = dataCS12[:, 0]
    OmegaCSGW12 = dataCS12[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW12)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW12_nonzero = OmegaGW12[nonzero_indices]
    
    plt.loglog(freq_nonzero, OmegaGW12_nonzero, color='purple', linewidth=2.2)
    plt.loglog(freqCS, OmegaCSGW12, color='purple', linewidth=2.2, linestyle=':')

# GW spectrum for U(1) breaking at 10^{13} GeV, Z2 breaking at 246 GeV
def plot_Lambda13():
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_13.0_246.0.txt')
    data13 = np.loadtxt(file_path)
    
    # separate the columns
    freq = data13[:, 0]
    OmegaGW13 = data13[:, 1]
    
    # pure CS case
    file_path = os.path.join(current_dir, folder_name, 'CSGW_13.0.txt')
    dataCS13 = np.loadtxt(file_path)
    
    # separate the columns
    freqCS = dataCS13[:, 0]
    OmegaCSGW13 = dataCS13[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW13)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW13_nonzero = OmegaGW13[nonzero_indices]
    
    plt.loglog(freq_nonzero, OmegaGW13_nonzero, color='darkblue', linewidth=2.2)
    plt.loglog(freqCS, OmegaCSGW13, color='darkblue', linewidth=2.2, linestyle=':')

# GW spectrum for U(1) breaking at 10^{14} GeV, Z2 breaking at 246 GeV
def plot_Lambda14():
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_14.0_246.0.txt')
    data14 = np.loadtxt(file_path)
    
    # separate the columns
    freq = data14[:, 0]
    OmegaGW14 = data14[:, 1]
    
    # pure CS case
    file_path = os.path.join(current_dir, folder_name, 'CSGW_14.0.txt')
    dataCS14 = np.loadtxt(file_path)
    
    # separate the columns
    freqCS = dataCS14[:, 0]
    OmegaCSGW14 = dataCS14[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW14)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW14_nonzero = OmegaGW14[nonzero_indices]
    
    plt.loglog(freq_nonzero, OmegaGW14_nonzero, color='orange', linewidth=2.2)
    plt.loglog(freqCS, OmegaCSGW14, color='orange', linewidth=2.2, linestyle=':')

# GW spectrum for U(1) breaking at 10^{15} GeV, Z2 breaking at 246 GeV
def plot_Lambda15():
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_15.0_246.0.txt')
    data15 = np.loadtxt(file_path)
    
    # separate the columns
    freq = data15[:, 0]
    OmegaGW15 = data15[:, 1]
    
    # pure CS case
    file_path = os.path.join(current_dir, folder_name, 'CSGW_15.0.txt')
    dataCS15 = np.loadtxt(file_path)
    
    # separate the columns
    freqCS = dataCS15[:, 0]
    OmegaCSGW15 = dataCS15[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW15)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW15_nonzero = OmegaGW15[nonzero_indices]
    
    plt.loglog(freq_nonzero, OmegaGW15_nonzero, color='red', linewidth=2.2)  
    plt.loglog(freqCS, OmegaCSGW15, color='red', linewidth=2.2, linestyle=':')
    
    
# Set font family to Latin Modern Roman for LaTeX text
plt.rcParams['font.family'] = 'Latin Modern Roman'

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Latin Modern Roman"
})


# make the final plot   
 
fig, ax = plt.subplots(figsize=(4*1.67, 4), dpi=600)
# Adding ticks on all sides
plt.tick_params(axis='both', which='both', direction='in', bottom=True, top=True, left=True, right=True)
# set axis limits to be displayed
plt.xlim(1e-9, 1e4)
plt.ylim(1e-18, 1e-7)
# put labels on the axes
plt.xlabel(r'$f$ [Hz]')
plt.ylabel(r'$\Omega_{\mathrm{GW}}h^2$')

# Now we combine all the plots into one
plot_all_interferometers() # interferometer plots
plot_Lambda12() # GW spectrum for U(1) breaking at 10^{12} GeV, Z2 breaking at 246 GeV
plot_Lambda13() # GW spectrum for U(1) breaking at 10^{13} GeV, Z2 breaking at 246 GeV
plot_Lambda14() # GW spectrum for U(1) breaking at 10^{14} GeV, Z2 breaking at 246 GeV
plot_Lambda15() # GW spectrum for U(1) breaking at 10^{15} GeV, Z2 breaking at 246 GeV

# plot legend
line_blank = mlines.Line2D([], [], color='blue', linestyle=' ', linewidth=0.5, label=r'$v_{\mathrm{SM}} = 246$ GeV')
line_purple = mlines.Line2D([], [], color='purple', linestyle='-', linewidth=1.5, label=r'$v_M = 10^{12}\ {\rm GeV}$')
line_blue = mlines.Line2D([], [], color='darkblue', linestyle='-', linewidth=1.5, label=r'$v_M = 10^{13}\ {\rm GeV}$')
line_orange = mlines.Line2D([], [], color='orange', linestyle='-', linewidth=1.5, label=r'$v_M = 10^{{14}}\ {\rm GeV}$')
line_red = mlines.Line2D([], [], color='red', linestyle='-', linewidth=1.5, label=r'$v_M = 10^{15}\ {\rm GeV}$')
plt.legend(handles=[line_blank, line_purple, line_blue, line_orange, line_red], loc = (0.74,0.045), framealpha=0.2, fontsize=8, edgecolor='black') #best upper-right

# save the figure
plt.savefig('GWspectrum.png', dpi=600)

# show plot
plt.show()
