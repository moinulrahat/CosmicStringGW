"""
This script calculates the signal-to-noise ratio (SNR) for various interferometers.
The routines for calculating snr for any GW signal is in snrcalc.py script.
Here we import it to calculate snr for the 2hdm.
A script to convert these results into latex table is also included at the end.
"""
import numpy as np
import warnings
import os
from snrcalc import snr_all_interferometers
# Suppress all warnings
warnings.filterwarnings("ignore") 

# Get the current working directory
current_dir = os.getcwd()

# Load and plot the pre-calculated GW spectrum.

# GW spectrum for U(1) breaking at 10^{15} GeV, Z2 breaking at 246 GeV
def get_Lambda15():
    # Define the name of the folder containing the data
    folder_name = '2hdmGWdata'
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_15.0_246.0.txt')
    data = np.loadtxt(file_path)
    
    # separate the columns
    freq = data[:, 0]
    OmegaGW = data[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW_nonzero = OmegaGW[nonzero_indices]
    
    return freq_nonzero, OmegaGW_nonzero

# GW spectrum for U(1) breaking at 10^{14} GeV, Z2 breaking at 246 GeV
def get_Lambda14():
    # Define the name of the folder containing the data
    folder_name = '2hdmGWdata'
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_14.0_246.0.txt')
    data = np.loadtxt(file_path)
    
    # separate the columns
    freq = data[:, 0]
    OmegaGW = data[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW_nonzero = OmegaGW[nonzero_indices]
    
    return freq_nonzero, OmegaGW_nonzero

# GW spectrum for U(1) breaking at 10^{13} GeV, Z2 breaking at 246 GeV
def get_Lambda13():
    # Define the name of the folder containing the data
    folder_name = '2hdmGWdata'
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_13.0_246.0.txt')
    data = np.loadtxt(file_path)
    
    # separate the columns
    freq = data[:, 0]
    OmegaGW = data[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW_nonzero = OmegaGW[nonzero_indices]
    
    return freq_nonzero, OmegaGW_nonzero

# GW spectrum for U(1) breaking at 10^{12} GeV, Z2 breaking at 246 GeV
def get_Lambda12():
    # Define the name of the folder containing the data
    folder_name = '2hdmGWdata'
    # Load the data from the text file
    file_path = os.path.join(current_dir, folder_name, 'DWCSGW_12.0_246.0.txt')
    data = np.loadtxt(file_path)
    
    # separate the columns
    freq = data[:, 0]
    OmegaGW = data[:, 1]
    
    # get rid of the pairs where GW amplitude is zero
    nonzero_indices = np.nonzero(OmegaGW)
    freq_nonzero = freq[nonzero_indices]
    OmegaGW_nonzero = OmegaGW[nonzero_indices]
    
    return freq_nonzero, OmegaGW_nonzero
    

# Now calculate SNR     
f_list, Omega_list = get_Lambda12()
print("SNR for $v = 10^{12}$ GeV \n", snr_all_interferometers(f_list, Omega_list))

f_list, Omega_list = get_Lambda13()
print("SNR for $v = 10^{13}$ GeV \n", snr_all_interferometers(f_list, Omega_list))

f_list, Omega_list = get_Lambda14()
print("SNR for $v = 10^{14}$ GeV \n", snr_all_interferometers(f_list, Omega_list))
f_list, Omega_list = get_Lambda15()
print("SNR for $v = 10^{15}$ GeV \n", snr_all_interferometers(f_list, Omega_list))

f_list, Omega_list = get_Lambda15()
print("SNR for $v = 10^{15}$ GeV \n", snr_all_interferometers(f_list, Omega_list))


"""
The following script can make a latex table from the above results
"""
# single dictionary
def make_latex_table():
    def dict_to_latex_table(data):
        table = "\\begin{table}[htbp]\n"
        table += "\\centering\n"
        table += "\\begin{tabular}{|c|c|}\n"
        table += "\\hline\n"
        table += "Interferometer & SNR \\\\\n"
        table += "\\hline\n"
        for key, value in data.items():
            table += f"{key} & {value} \\\\\n"
        table += "\\hline\n"
        table += "\\end{tabular}\n"
        table += "\\caption{Your caption here}\n"
        table += "\\label{tab:my_table}\n"
        table += "\\end{table}"
        return table
    
    # Example dictionary
    f_list, Omega_list = get_Lambda14()
    my_dict = snr_all_interferometers(f_list, Omega_list)
    
    # Convert dictionary to LaTeX table
    latex_table = dict_to_latex_table(my_dict)
    
    # Print LaTeX table
    print(latex_table)

# combining multiple dictionaries
def dictionaries_to_latex_table(*dictionaries):
    keys = list(dictionaries[0].keys())
    num_dictionaries = len(dictionaries)

    table = "\\begin{table}[htbp]\n"
    table += "\\centering\n"
    table += "\\begin{tabular}{|c|" + "|".join(["c"] * num_dictionaries) + "|}\n"
    table += "\\hline\n"
    table += "Key & " + " & ".join([f"Dictionary {i+1}" for i in range(num_dictionaries)]) + " \\\\\n"
    table += "\\hline\n"
    
    for key in keys:
        values = [dictionary[key] for dictionary in dictionaries]
        row_values = " & ".join(map(str, values))
        table += f"{key} & {row_values} \\\\\n"
    
    table += "\\hline\n"
    table += "\\end{tabular}\n"
    table += "\\caption{Your caption here}\n"
    table += "\\label{tab:my_table}\n"
    table += "\\end{table}"

    return table

# Example dictionaries
f_list, Omega_list = get_Lambda12()
dict1 = snr_all_interferometers(f_list, Omega_list)
f_list, Omega_list = get_Lambda13()
dict2 = snr_all_interferometers(f_list, Omega_list)
f_list, Omega_list = get_Lambda14()
dict3 = snr_all_interferometers(f_list, Omega_list)
f_list, Omega_list = get_Lambda15()
dict4 = snr_all_interferometers(f_list, Omega_list)

# Convert dictionaries to LaTeX table
latex_table = dictionaries_to_latex_table(dict1, dict2, dict3, dict4)

# Print LaTeX table
print(latex_table)