"""
This script calculates the signal-to-noise ratio (SNR) for various interferometers.
"""
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
import warnings
import os
# Suppress all warnings
warnings.filterwarnings("ignore")


# Get the current working directory
current_dir = os.getcwd()

def snr_calculator(f_list, Omega_list, Interf):
    # Interpolate the interferometer data 
    f_interf = Interf[:, 0]
    Omega_interf = Interf[:, 1]  
    log_interp = interp1d(np.log10(f_interf), np.log10(Omega_interf))
    def Omega_interf_int(freq):
        return 10**log_interp(np.log10(freq))
    
    # new grid
    f_new_list = np.logspace(np.log10(1.00001*f_interf[0]), np.log10(0.9999*f_interf[-1]), 100)
        
    Omega_interf_new_list = np.array([float(Omega_interf_int(freq)) for freq in f_new_list])
       
    # interpolate the GW signal data
    Omega_interp = interp1d(np.log10(f_list), np.log10(Omega_list))
    def Omega_signal(freq):
        if freq < f_list[0] or freq > f_list[-1]:
            return 0
        else:
            return 10**Omega_interp(np.log10(freq))
    Omega_signal_new_list = np.array([float(Omega_signal(freq)) for freq in f_new_list])
    
    # calculate snr
    log_snr_integrand = interp1d(np.log10(f_new_list), np.log10((Omega_signal_new_list / Omega_interf_new_list)**2))
    def snr_integrand(freq):
        return 10**log_snr_integrand(np.log10(freq))
    
    integral, error = quad(snr_integrand, f_new_list[0], f_new_list[-1], limit=100)

    snr = np.sqrt(4 * integral)
    
    return snr

def snr_LISA(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'LISApoints.csv')
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)
    

def snr_BBO(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'BBO.csv')
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)

def snr_DECIGO(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'Decigo.csv')     
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)

def snr_ET(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'ETlist.csv')     
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)

def snr_AION(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'AION.csv')     
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)

def snr_AEDGE(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'AEDGE.csv')     
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)

def snr_CE(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'CE.csv')     
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)

def snr_MuARES(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'MuARES.csv')
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    return snr_calculator(f_list, Omega_list, Interf)

def snr_Aplus(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'Aplusdesignsensitivity.csv')
    
     
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    f_interf = Interf[:, 0]
    Omega_interf = 0.7**2 *Interf[:, 1]
    Omega_interp = interp1d(f_list, Omega_list)
    def Omega_int(freq):
        if freq < f_list[0] or freq > f_list[-1]:
            return 0
        else:
            return Omega_interp(freq)
    Omega_interp_list = [Omega_int(freq) for freq in f_interf]
    
    snr = np.sqrt(4 * sum((Omega_interp_list / Omega_interf)**2))
    
    return snr

def snr_LV(f_list, Omega_list):
    # Define the name of the folder containing the data
    folder_name = 'Interferometer data'
    # Construct the path to the data file inside the folder
    Interf_path = os.path.join(current_dir, folder_name, 'LIGOVIRGOdesignsensitivity.csv')
    
     
    Interf = np.genfromtxt(Interf_path, delimiter=',')
    f_interf = Interf[:, 0]
    Omega_interf = 0.7**2 *Interf[:, 1]
    Omega_interp = interp1d(f_list, Omega_list)
    def Omega_int(freq):
        if freq < f_list[0] or freq > f_list[-1]:
            return 0
        else:
            return Omega_interp(freq)
    Omega_interp_list = [Omega_int(freq) for freq in f_interf]
    
    snr = np.sqrt(4 * sum((Omega_interp_list / Omega_interf)**2))
    
    return snr

def snr_all_interferometers(f_list, Omega_list):
    snr_dict = {'snr_MuARES': round(snr_MuARES(f_list, Omega_list), 2),
                'snr_LISA': round(snr_LISA(f_list, Omega_list), 2),
                'snr_BBO': round(snr_BBO(f_list, Omega_list), 2),
                'snr_DECIGO': round(snr_DECIGO(f_list, Omega_list), 2),
                'snr_AION': round(snr_AION(f_list, Omega_list), 2),
                'snr_AEDGE': round(snr_AEDGE(f_list, Omega_list), 2),
                'snr_ET': round(snr_ET(f_list, Omega_list), 2),
                'snr_CE': round(snr_CE(f_list, Omega_list), 2),
                'snr_Aplus': round(snr_Aplus(f_list, Omega_list), 2),
                'snr_HLV': round(snr_LV(f_list, Omega_list), 2)
                }
    return snr_dict