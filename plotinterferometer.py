'''
This file reads the sensitivity/upper bound/observation of commonly discussed
interferometers. A function plot_all_interferometers() combines all such plots 
along with the labels.
'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import os

# Get the current working directory
current_dir = os.getcwd()

# Define the name of the folder containing the data
folder_name = 'Interferometer data'

def plot_LISA():
    # Construct the path to the data file inside the folder
    LISA_path = os.path.join(current_dir, folder_name, 'LISApoints.csv')
    
    # Read the data from the file
    LISA = np.genfromtxt(LISA_path, delimiter=',')
    fLISA = LISA[:, 0]
    OmegaLISA = LISA[:, 1]
    plt.loglog(fLISA, OmegaLISA, linestyle='--', color='blue', alpha=0.3, linewidth=1)
    # Find the maximum y value
    max_y = 10
    plt.text(4.3e-5, 5.5e-11, r'LISA', color='blue', fontsize=7, rotation=-64)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fLISA, OmegaLISA, max_y, color='skyblue', alpha=0.5)  # Fill area above the curve

def plot_BBO():
    # Construct the path to the data file inside the folder
    BBO_path = os.path.join(current_dir, folder_name, 'BBO.csv')
    
    # Read the data from the file
    BBO = np.genfromtxt(BBO_path, delimiter=',')
    fBBO = BBO[:, 0]
    OmegaBBO = BBO[:, 1]
    plt.loglog(fBBO, OmegaBBO, linestyle='--', color='darkgreen', alpha=0.3, linewidth=1)
    # Find the maximum y value
    max_y = 10
    plt.text(0.08, 15.5e-18, r'BBO', color='darkgreen', fontsize=7)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fBBO, OmegaBBO, max_y, color='limegreen', alpha=0.2)  # Fill area above the curve

def plot_DECIGO():
    # Construct the path to the data file inside the folder
    DECIGO_path = os.path.join(current_dir, folder_name, 'Decigo.csv')
    
    # Read the data from the file
    DECIGO = np.genfromtxt(DECIGO_path, delimiter=',')
    fDECIGO = DECIGO[:, 0]
    OmegaDECIGO = DECIGO[:, 1]
    plt.loglog(fDECIGO, OmegaDECIGO, linestyle='--', color='blue', alpha=0.3, linewidth=1)
    # Find the maximum y value
    max_y = 10
    plt.text(0.03, 12.5e-17, r'DECIGO', color='blue', fontsize=7)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fDECIGO, OmegaDECIGO, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_ET():
    # Construct the path to the data file inside the folder
    ET_path = os.path.join(current_dir, folder_name, 'ETlist.csv')
    plt.text(2.3, 12.5e-12, r'ET', color='darkgreen', fontsize=7, rotation=-75)
    # Read the data from the file
    ET = np.genfromtxt(ET_path, delimiter=',')
    fET = ET[:, 0]
    OmegaET = ET[:, 1]
    plt.loglog(fET, OmegaET, linestyle='--', color='darkgreen', alpha=0.7, linewidth=1)
    # Find the maximum y value
    max_y = 10
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fET, OmegaET, max_y, color='lightgreen', alpha=0.5)  # Fill area above the curve    

# NANOGrav 15 data is divided into bins, we will plot them separately and then combine
def plot_NGbin1():
    # Construct the path to the data file inside the folder
    NGbin1_path = os.path.join(current_dir, folder_name, 'NGbin1.csv')
    
    # Read the data from the file
    NGbin1 = np.genfromtxt(NGbin1_path, delimiter=',')
    fNGbin1 = NGbin1[:, 0]
    OmegaNGbin1 = NGbin1[:, 1]
    plt.loglog(fNGbin1, OmegaNGbin1, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin1)
    plt.text(2.3e-9, 1.5e-9, r'NG15', color='blue', fontsize=7, rotation=55)
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin1, OmegaNGbin1, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
 
def plot_NGbin2():
    # Construct the path to the data file inside the folder
    NGbin2_path = os.path.join(current_dir, folder_name, 'NGbin2.csv')
    
    # Read the data from the file
    NGbin2 = np.genfromtxt(NGbin2_path, delimiter=',')
    fNGbin2 = NGbin2[:, 0]
    OmegaNGbin2 = NGbin2[:, 1]
    plt.loglog(fNGbin2, OmegaNGbin2, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin2)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin2, OmegaNGbin2, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin3():
    # Construct the path to the data file inside the folder
    NGbin3_path = os.path.join(current_dir, folder_name, 'NGbin3.csv')
    
    # Read the data from the file
    NGbin3 = np.genfromtxt(NGbin3_path, delimiter=',')
    fNGbin3 = NGbin3[:, 0]
    OmegaNGbin3 = NGbin3[:, 1]
    plt.loglog(fNGbin3, OmegaNGbin3, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin3)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin3, OmegaNGbin3, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin4():
    # Construct the path to the data file inside the folder
    NGbin4_path = os.path.join(current_dir, folder_name, 'NGbin4.csv')
    
    # Read the data from the file
    NGbin4 = np.genfromtxt(NGbin4_path, delimiter=',')
    fNGbin4 = NGbin4[:, 0]
    OmegaNGbin4 = NGbin4[:, 1]
    plt.loglog(fNGbin4, OmegaNGbin4, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin4)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin4, OmegaNGbin4, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin5():
    # Construct the path to the data file inside the folder
    NGbin5_path = os.path.join(current_dir, folder_name, 'NGbin5.csv')
    
    # Read the data from the file
    NGbin5 = np.genfromtxt(NGbin5_path, delimiter=',')
    fNGbin5 = NGbin5[:, 0]
    OmegaNGbin5 = NGbin5[:, 1]
    plt.loglog(fNGbin5, OmegaNGbin5, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin5)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin5, OmegaNGbin5, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin6():
    # Construct the path to the data file inside the folder
    NGbin6_path = os.path.join(current_dir, folder_name, 'NGbin6.csv')
    
    # Read the data from the file
    NGbin6 = np.genfromtxt(NGbin6_path, delimiter=',')
    fNGbin6 = NGbin6[:, 0]
    OmegaNGbin6 = NGbin6[:, 1]
    plt.loglog(fNGbin6, OmegaNGbin6, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin6)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin6, OmegaNGbin6, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin7():
    # Construct the path to the data file inside the folder
    NGbin7_path = os.path.join(current_dir, folder_name, 'NGbin7.csv')
    
    # Read the data from the file
    NGbin7 = np.genfromtxt(NGbin7_path, delimiter=',')
    fNGbin7 = NGbin7[:, 0]
    OmegaNGbin7 = NGbin7[:, 1]
    plt.loglog(fNGbin7, OmegaNGbin7, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin7)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin7, OmegaNGbin7, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin8():
    # Construct the path to the data file inside the folder
    NGbin8_path = os.path.join(current_dir, folder_name, 'NGbin8.csv')
    
    # Read the data from the file
    NGbin8 = np.genfromtxt(NGbin8_path, delimiter=',')
    fNGbin8 = NGbin8[:, 0]
    OmegaNGbin8 = NGbin8[:, 1]
    plt.loglog(fNGbin8, OmegaNGbin8, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin8)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin8, OmegaNGbin8, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin9():
    # Construct the path to the data file inside the folder
    NGbin9_path = os.path.join(current_dir, folder_name, 'NGbin9.csv')
    
    # Read the data from the file
    NGbin9 = np.genfromtxt(NGbin9_path, delimiter=',')
    fNGbin9 = NGbin9[:, 0]
    OmegaNGbin9 = NGbin9[:, 1]
    plt.loglog(fNGbin9, OmegaNGbin9, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin9)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin9, OmegaNGbin9, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin10():
    # Construct the path to the data file inside the folder
    NGbin10_path = os.path.join(current_dir, folder_name, 'NGbin10.csv')
    
    # Read the data from the file
    NGbin10 = np.genfromtxt(NGbin10_path, delimiter=',')
    fNGbin10 = NGbin10[:, 0]
    OmegaNGbin10 = NGbin10[:, 1]
    plt.loglog(fNGbin10, OmegaNGbin10, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin10)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin10, OmegaNGbin10, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve    

def plot_NGbin11():
    # Construct the path to the data file inside the folder
    NGbin11_path = os.path.join(current_dir, folder_name, 'NGbin11.csv')
    
    # Read the data from the file
    NGbin11 = np.genfromtxt(NGbin11_path, delimiter=',')
    fNGbin11 = NGbin11[:, 0]
    OmegaNGbin11 = NGbin11[:, 1]
    plt.loglog(fNGbin11, OmegaNGbin11, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin11)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin11, OmegaNGbin11, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
    
def plot_NGbin12():
    # Construct the path to the data file inside the folder
    NGbin12_path = os.path.join(current_dir, folder_name, 'NGbin12.csv')
    
    # Read the data from the file
    NGbin12 = np.genfromtxt(NGbin12_path, delimiter=',')
    fNGbin12 = NGbin12[:, 0]
    OmegaNGbin12 = NGbin12[:, 1]
    plt.loglog(fNGbin12, OmegaNGbin12, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin12)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin12, OmegaNGbin12, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
    
def plot_NGbin13():
    # Construct the path to the data file inside the folder
    NGbin13_path = os.path.join(current_dir, folder_name, 'NGbin13.csv')
    
    # Read the data from the file
    NGbin13 = np.genfromtxt(NGbin13_path, delimiter=',')
    fNGbin13 = NGbin13[:, 0]
    OmegaNGbin13 = NGbin13[:, 1]
    plt.loglog(fNGbin13, OmegaNGbin13, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin13)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin13, OmegaNGbin13, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
    
def plot_NGbin14():
    # Construct the path to the data file inside the folder
    NGbin14_path = os.path.join(current_dir, folder_name, 'NGbin14.csv')
    
    # Read the data from the file
    NGbin14 = np.genfromtxt(NGbin14_path, delimiter=',')
    fNGbin14 = NGbin14[:, 0]
    OmegaNGbin14 = NGbin14[:, 1]
    plt.loglog(fNGbin14, OmegaNGbin14, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin14)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin14, OmegaNGbin14, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin15():
    # Construct the path to the data file inside the folder
    NGbin15_path = os.path.join(current_dir, folder_name, 'NGbin15.csv')
    
    # Read the data from the file
    NGbin15 = np.genfromtxt(NGbin15_path, delimiter=',')
    fNGbin15 = NGbin15[:, 0]
    OmegaNGbin15 = NGbin15[:, 1]
    plt.loglog(fNGbin15, OmegaNGbin15, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin15)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin15, OmegaNGbin15, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin16():
    # Construct the path to the data file inside the folder
    NGbin16_path = os.path.join(current_dir, folder_name, 'NGbin16.csv')
    
    # Read the data from the file
    NGbin16 = np.genfromtxt(NGbin16_path, delimiter=',')
    fNGbin16 = NGbin16[:, 0]
    OmegaNGbin16 = NGbin16[:, 1]
    plt.loglog(fNGbin16, OmegaNGbin16, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin16)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin16, OmegaNGbin16, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin17():
    # Construct the path to the data file inside the folder
    NGbin17_path = os.path.join(current_dir, folder_name, 'NGbin17.csv')
    
    # Read the data from the file
    NGbin17 = np.genfromtxt(NGbin17_path, delimiter=',')
    fNGbin17 = NGbin17[:, 0]
    OmegaNGbin17 = NGbin17[:, 1]
    plt.loglog(fNGbin17, OmegaNGbin17, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin17)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin17, OmegaNGbin17, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin18():
    # Construct the path to the data file inside the folder
    NGbin18_path = os.path.join(current_dir, folder_name, 'NGbin18.csv')
    
    # Read the data from the file
    NGbin18 = np.genfromtxt(NGbin18_path, delimiter=',')
    fNGbin18 = NGbin18[:, 0]
    OmegaNGbin18 = NGbin18[:, 1]
    plt.loglog(fNGbin18, OmegaNGbin18, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin18)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin18, OmegaNGbin18, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin19():
    # Construct the path to the data file inside the folder
    NGbin19_path = os.path.join(current_dir, folder_name, 'NGbin19.csv')
    
    # Read the data from the file
    NGbin19 = np.genfromtxt(NGbin19_path, delimiter=',')
    fNGbin19 = NGbin19[:, 0]
    OmegaNGbin19 = NGbin19[:, 1]
    plt.loglog(fNGbin19, OmegaNGbin19, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin19)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin19, OmegaNGbin19, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin20():
    # Construct the path to the data file inside the folder
    NGbin20_path = os.path.join(current_dir, folder_name, 'NGbin20.csv')
    
    # Read the data from the file
    NGbin20 = np.genfromtxt(NGbin20_path, delimiter=',')
    fNGbin20 = NGbin20[:, 0]
    OmegaNGbin20 = NGbin20[:, 1]
    plt.loglog(fNGbin20, OmegaNGbin20, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin20)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin20, OmegaNGbin20, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin21():
    # Construct the path to the data file inside the folder
    NGbin21_path = os.path.join(current_dir, folder_name, 'NGbin21.csv')
    
    # Read the data from the file
    NGbin21 = np.genfromtxt(NGbin21_path, delimiter=',')
    fNGbin21 = NGbin21[:, 0]
    OmegaNGbin21 = NGbin21[:, 1]
    plt.loglog(fNGbin21, OmegaNGbin21, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin21)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin21, OmegaNGbin21, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
    
def plot_NGbin22():
    # Construct the path to the data file inside the folder
    NGbin22_path = os.path.join(current_dir, folder_name, 'NGbin22.csv')
    
    # Read the data from the file
    NGbin22 = np.genfromtxt(NGbin22_path, delimiter=',')
    fNGbin22 = NGbin22[:, 0]
    OmegaNGbin22 = NGbin22[:, 1]
    plt.loglog(fNGbin22, OmegaNGbin22, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin22)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin22, OmegaNGbin22, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
    
def plot_NGbin23():
    # Construct the path to the data file inside the folder
    NGbin23_path = os.path.join(current_dir, folder_name, 'NGbin23.csv')
    
    # Read the data from the file
    NGbin23 = np.genfromtxt(NGbin23_path, delimiter=',')
    fNGbin23 = NGbin23[:, 0]
    OmegaNGbin23 = NGbin23[:, 1]
    plt.loglog(fNGbin23, OmegaNGbin23, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin23)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin23, OmegaNGbin23, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin24():
    # Construct the path to the data file inside the folder
    NGbin24_path = os.path.join(current_dir, folder_name, 'NGbin24.csv')
    
    # Read the data from the file
    NGbin24 = np.genfromtxt(NGbin24_path, delimiter=',')
    fNGbin24 = NGbin24[:, 0]
    OmegaNGbin24 = NGbin24[:, 1]
    plt.loglog(fNGbin24, OmegaNGbin24, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin24)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin24, OmegaNGbin24, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin25():
    # Construct the path to the data file inside the folder
    NGbin25_path = os.path.join(current_dir, folder_name, 'NGbin25.csv')
    
    # Read the data from the file
    NGbin25 = np.genfromtxt(NGbin25_path, delimiter=',')
    fNGbin25 = NGbin25[:, 0]
    OmegaNGbin25 = NGbin25[:, 1]
    plt.loglog(fNGbin25, OmegaNGbin25, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin25)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin25, OmegaNGbin25, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
    
def plot_NGbin26():
    # Construct the path to the data file inside the folder
    NGbin26_path = os.path.join(current_dir, folder_name, 'NGbin26.csv')
    
    # Read the data from the file
    NGbin26 = np.genfromtxt(NGbin26_path, delimiter=',')
    fNGbin26 = NGbin26[:, 0]
    OmegaNGbin26 = NGbin26[:, 1]
    plt.loglog(fNGbin26, OmegaNGbin26, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin26)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin26, OmegaNGbin26, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin27():
    # Construct the path to the data file inside the folder
    NGbin27_path = os.path.join(current_dir, folder_name, 'NGbin27.csv')
    
    # Read the data from the file
    NGbin27 = np.genfromtxt(NGbin27_path, delimiter=',')
    fNGbin27 = NGbin27[:, 0]
    OmegaNGbin27 = NGbin27[:, 1]
    plt.loglog(fNGbin27, OmegaNGbin27, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin27)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin27, OmegaNGbin27, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin28():
    # Construct the path to the data file inside the folder
    NGbin28_path = os.path.join(current_dir, folder_name, 'NGbin28.csv')
    
    # Read the data from the file
    NGbin28 = np.genfromtxt(NGbin28_path, delimiter=',')
    fNGbin28 = NGbin28[:, 0]
    OmegaNGbin28 = NGbin28[:, 1]
    plt.loglog(fNGbin28, OmegaNGbin28, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin28)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin28, OmegaNGbin28, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve
    
def plot_NGbin29():
    # Construct the path to the data file inside the folder
    NGbin29_path = os.path.join(current_dir, folder_name, 'NGbin29.csv')
    
    # Read the data from the file
    NGbin29 = np.genfromtxt(NGbin29_path, delimiter=',')
    fNGbin29 = NGbin29[:, 0]
    OmegaNGbin29 = NGbin29[:, 1]
    plt.loglog(fNGbin29, OmegaNGbin29, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin29)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin29, OmegaNGbin29, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_NGbin30():
    # Construct the path to the data file inside the folder
    NGbin30_path = os.path.join(current_dir, folder_name, 'NGbin30.csv')
    
    # Read the data from the file
    NGbin30 = np.genfromtxt(NGbin30_path, delimiter=',')
    fNGbin30 = NGbin30[:, 0]
    OmegaNGbin30 = NGbin30[:, 1]
    plt.loglog(fNGbin30, OmegaNGbin30, linestyle='-', color='blue', alpha=0.1)
    # Find the maximum y value
    max_y = max(OmegaNGbin30)
    
    # Create a polygon to fill the area above the curve
    plt.fill(fNGbin30, OmegaNGbin30, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

# combine NG15 plots
def plot_NANOGrav():
    plot_NGbin1()
    plot_NGbin2()
    plot_NGbin3()
    plot_NGbin2()
    plot_NGbin4()
    plot_NGbin5()
    plot_NGbin6()
    plot_NGbin7()
    plot_NGbin8()
    plot_NGbin9()
    plot_NGbin10()
    plot_NGbin11()
    plot_NGbin12()
    plot_NGbin13()
    plot_NGbin14()
    plot_NGbin15()
    plot_NGbin16()
    plot_NGbin17()
    plot_NGbin18()
    plot_NGbin19()
    plot_NGbin20()
    plot_NGbin21()
    plot_NGbin22()
    plot_NGbin23()
    plot_NGbin24()
    plot_NGbin25()
    plot_NGbin26()
    plot_NGbin27()
    plot_NGbin28()
    plot_NGbin29()
    plot_NGbin30()
    
def plot_SKA():
    # Construct the path to the data file inside the folder
    SKA_path = os.path.join(current_dir, folder_name, 'SKA.csv')
    
    # Read the data from the file
    SKA = np.genfromtxt(SKA_path, delimiter=',')
    fSKA = SKA[:, 0]
    OmegaSKA = SKA[:, 1]
    plt.loglog(fSKA, OmegaSKA, linestyle='--', color='darkgreen', alpha=0.5, linewidth=1)
    # Find the maximum y value
    max_y = 10
    plt.text(2.0e-9, 2.5e-15, r'SKA', color='darkgreen', fontsize=7, rotation=69)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fSKA, OmegaSKA, max_y, color='lightgreen', alpha=0.3)  # Fill area above the curve

# EPTA data is divided into bins. We will plot them separately and then combine.
def plot_EPTAbin00():
    # Construct the path to the data file inside the folder
    EPTAbin00_path = os.path.join(current_dir, folder_name, 'EPTAbin00.csv')
    
    # Read the data from the file
    EPTAbin00 = np.genfromtxt(EPTAbin00_path, delimiter=',')
    fEPTAbin00 = EPTAbin00[:, 0]
    OmegaEPTAbin00 = EPTAbin00[:, 1]
    plt.loglog(fEPTAbin00, OmegaEPTAbin00, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = OmegaEPTAbin00
    plt.text(3.3e-9, 1e-8, r'EPTA', color='darkorange', fontsize=7, rotation=55)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin00, OmegaEPTAbin00, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin0():
    # Construct the path to the data file inside the folder
    EPTAbin0_path = os.path.join(current_dir, folder_name, 'EPTAbin0.csv')
    
    # Read the data from the file
    EPTAbin0 = np.genfromtxt(EPTAbin0_path, delimiter=',')
    fEPTAbin0 = EPTAbin0[:, 0]
    OmegaEPTAbin0 = EPTAbin0[:, 1]
    plt.loglog(fEPTAbin0, OmegaEPTAbin0, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin0)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin0, OmegaEPTAbin0, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin1():
    # Construct the path to the data file inside the folder
    EPTAbin1_path = os.path.join(current_dir, folder_name, 'EPTAbin1.csv')
    
    # Read the data from the file
    EPTAbin1 = np.genfromtxt(EPTAbin1_path, delimiter=',')
    fEPTAbin1 = EPTAbin1[:, 0]
    OmegaEPTAbin1 = EPTAbin1[:, 1]
    plt.loglog(fEPTAbin1, OmegaEPTAbin1, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin1)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin1, OmegaEPTAbin1, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin2():
    # Construct the path to the data file inside the folder
    EPTAbin2_path = os.path.join(current_dir, folder_name, 'EPTAbin2.csv')
    
    # Read the data from the file
    EPTAbin2 = np.genfromtxt(EPTAbin2_path, delimiter=',')
    fEPTAbin2 = EPTAbin2[:, 0]
    OmegaEPTAbin2 = EPTAbin2[:, 1]
    plt.loglog(fEPTAbin2, OmegaEPTAbin2, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin2)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin2, OmegaEPTAbin2, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin3():
    # Construct the path to the data file inside the folder
    EPTAbin3_path = os.path.join(current_dir, folder_name, 'EPTAbin3.csv')
    
    # Read the data from the file
    EPTAbin3 = np.genfromtxt(EPTAbin3_path, delimiter=',')
    fEPTAbin3 = EPTAbin3[:, 0]
    OmegaEPTAbin3 = EPTAbin3[:, 1]
    plt.loglog(fEPTAbin3, OmegaEPTAbin3, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin3)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin3, OmegaEPTAbin3, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin4():
    # Construct the path to the data file inside the folder
    EPTAbin4_path = os.path.join(current_dir, folder_name, 'EPTAbin4.csv')
    
    # Read the data from the file
    EPTAbin4 = np.genfromtxt(EPTAbin4_path, delimiter=',')
    fEPTAbin4 = EPTAbin4[:, 0]
    OmegaEPTAbin4 = EPTAbin4[:, 1]
    plt.loglog(fEPTAbin4, OmegaEPTAbin4, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin4)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin4, OmegaEPTAbin4, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin5():
    # Construct the path to the data file inside the folder
    EPTAbin5_path = os.path.join(current_dir, folder_name, 'EPTAbin5.csv')
    
    # Read the data from the file
    EPTAbin5 = np.genfromtxt(EPTAbin5_path, delimiter=',')
    fEPTAbin5 = EPTAbin5[:, 0]
    OmegaEPTAbin5 = EPTAbin5[:, 1]
    plt.loglog(fEPTAbin5, OmegaEPTAbin5, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin5)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin5, OmegaEPTAbin5, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin6():
    # Construct the path to the data file inside the folder
    EPTAbin6_path = os.path.join(current_dir, folder_name, 'EPTAbin6.csv')
    
    # Read the data from the file
    EPTAbin6 = np.genfromtxt(EPTAbin6_path, delimiter=',')
    fEPTAbin6 = EPTAbin6[:, 0]
    OmegaEPTAbin6 = EPTAbin6[:, 1]
    plt.loglog(fEPTAbin6, OmegaEPTAbin6, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin6)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin6, OmegaEPTAbin6, max_y, color='orange', alpha=0.1)  # Fill area above the curve

def plot_EPTAbin7():
    # Construct the path to the data file inside the folder
    EPTAbin7_path = os.path.join(current_dir, folder_name, 'EPTAbin7.csv')
    
    # Read the data from the file
    EPTAbin7 = np.genfromtxt(EPTAbin7_path, delimiter=',')
    fEPTAbin7 = EPTAbin7[:, 0]
    OmegaEPTAbin7 = EPTAbin7[:, 1]
    plt.loglog(fEPTAbin7, OmegaEPTAbin7, linestyle='-', color='orange', alpha=0.2)
    # Find the maximum y value
    max_y = max(OmegaEPTAbin7)
    
    # Create a polygon to fill the area above the curve
    plt.fill_between(fEPTAbin7, OmegaEPTAbin7, max_y, color='orange', alpha=0.1)  # Fill area above the curve

# combine EPTA plots
def plot_EPTA():
    plot_EPTAbin00()
    plot_EPTAbin0()
    plot_EPTAbin1()
    plot_EPTAbin2()
    plot_EPTAbin3()
    plot_EPTAbin4()
    plot_EPTAbin5()
    plot_EPTAbin6()
    plot_EPTAbin7()

def plot_AION():
    # Construct the path to the data file inside the folder
    AION_path = os.path.join(current_dir, folder_name, 'AION.csv')
    
    # Read the data from the file
    AION = np.genfromtxt(AION_path, delimiter=',')
    fAION = AION[:, 0]
    OmegaAION = AION[:, 1]
    plt.loglog(fAION, OmegaAION, linestyle='--', color='blue', alpha=0.4, linewidth=1)
    # Find the maximum y value
    max_y = max(OmegaAION)
    plt.text(0.22, 1.0e-11, r'AION', color='blue', fontsize=7, rotation=68)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fAION, OmegaAION, max_y, color='lightblue', alpha=0.7)  # Fill area above the curve

def plot_AEDGE():
    # Construct the path to the data file inside the folder
    AEDGE_path = os.path.join(current_dir, folder_name, 'AEDGE.csv')
    
    # Read the data from the file
    AEDGE = np.genfromtxt(AEDGE_path, delimiter=',')
    fAEDGE = AEDGE[:, 0]
    OmegaAEDGE = AEDGE[:, 1]
    plt.loglog(fAEDGE, OmegaAEDGE, linestyle='--', color='green', alpha=0.8, linewidth=1)
    # Find the maximum y value
    max_y = max(OmegaAEDGE)
    plt.text(0.08, 1.0e-13, r'AEDGE', color='green', fontsize=7, rotation=58)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fAEDGE, OmegaAEDGE, max_y, color='lightgreen', alpha=0.5)  # Fill area above the curve

def plot_CE():
    # Construct the path to the data file inside the folder
    CE_path = os.path.join(current_dir, folder_name, 'CE.csv')
    
    # Read the data from the file
    CE = np.genfromtxt(CE_path, delimiter=',')
    fCE = CE[:, 0]
    OmegaCE = CE[:, 1]
    plt.loglog(fCE, OmegaCE, linestyle='--', color='blue', alpha=0.6, linewidth=1)
    # Find the maximum y value
    max_y = max(OmegaCE)
    plt.text(65, 19.5e-12, r'CE', color='blue', fontsize=7, rotation=65)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fCE, OmegaCE, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_MuARES():
    # Construct the path to the data file inside the folder
    MuARES_path = os.path.join(current_dir, folder_name, 'MuARES.csv')
    
    # Read the data from the file
    MuARES = np.genfromtxt(MuARES_path, delimiter=',')
    fMuARES = MuARES[:, 0]
    OmegaMuARES = MuARES[:, 1]
    plt.loglog(fMuARES, OmegaMuARES, linestyle='--', color='darkgreen', alpha=0.5, linewidth=1)
    # Find the maximum y value
    max_y = max(OmegaMuARES)
    plt.text(1e-4, 1.5e-16, r'$\mu$Ares', color='green', fontsize=7)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fMuARES, OmegaMuARES, max_y, color='lightgreen', alpha=0.2)  # Fill area above the curve

def plot_ALIGOVIRGO():
    # Construct the path to the data file inside the folder
    LIGOsensitivity_path = os.path.join(current_dir, folder_name, 'LIGOsensitivity.csv')
    
    # Read the data from the file
    LIGOsensitivity = np.genfromtxt(LIGOsensitivity_path, delimiter=',')
    fLIGOsensitivity = LIGOsensitivity[:, 0]
    OmegaLIGOsensitivity = LIGOsensitivity[:, 1]
    ALIGOVIRGO = interp1d(fLIGOsensitivity, OmegaLIGOsensitivity)
    OmegaLIGOsensitivityh2 = 0.7**2 * ALIGOVIRGO(fLIGOsensitivity)
    plt.loglog(fLIGOsensitivity, OmegaLIGOsensitivityh2, linestyle='-', color='gray', alpha=0.8, linewidth=1)
    # Find the maximum y value
    max_y = max(OmegaLIGOsensitivityh2)
    plt.text(25, 4.0e-8, r'LVK', color='black', fontsize=7)
    plt.text(25, 2.0e-8, r'(O3)', color='black', fontsize=7)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fLIGOsensitivity, OmegaLIGOsensitivityh2, max_y, color='gray', alpha=0.5)  # Fill area above the curve

def plot_Aplus():
    # Construct the path to the data file inside the folder
    Aplus_path = os.path.join(current_dir, folder_name, 'Aplusdesignsensitivity.csv')
    
    # Read the data from the file
    Aplus = np.genfromtxt(Aplus_path, delimiter=',')
    fAplus = Aplus[:, 0]
    OmegaAplus = Aplus[:, 1]
    ALIGOVIRGO = interp1d(fAplus, OmegaAplus)
    OmegaAplush2 = 0.7**2 * ALIGOVIRGO(fAplus)
    plt.loglog(fAplus, OmegaAplush2, linestyle='--', linewidth=1, color='blue', alpha=0.5)
    # Find the maximum y value
    max_y = max(OmegaAplush2)
    plt.text(18, 4.5e-10, r'A+', color='blue', fontsize=7)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fAplus, OmegaAplush2, max_y, color='lightblue', alpha=0.5)  # Fill area above the curve

def plot_LV():
    # Construct the path to the data file inside the folder
    LV_path = os.path.join(current_dir, folder_name, 'LIGOVIRGOdesignsensitivity.csv')
    
    # Read the data from the file
    LV = np.genfromtxt(LV_path, delimiter=',')
    fLV = LV[:, 0]
    OmegaLV = LV[:, 1]
    ALIGOVIRGO = interp1d(fLV, OmegaLV)
    OmegaLVh2 = 0.7**2 * ALIGOVIRGO(fLV)
    plt.loglog(fLV, OmegaLVh2, linestyle='--', linewidth=1, color='green', alpha=0.5)
    # Find the maximum y value
    max_y = max(OmegaLVh2)
    plt.text(15, 2.5e-9, r'HLV', color='darkgreen', fontsize=7)
    # Create a polygon to fill the area above the curve
    plt.fill_between(fLV, OmegaLVh2, max_y, color='lightgreen', alpha=0.5)  # Fill area above the curve


# combine all interferometer plots    
def plot_all_interferometers():
    plot_LISA()
    plot_BBO() 
    plot_DECIGO()
    plot_ET()
    plot_NGbin1()
    plot_NANOGrav()
    plot_SKA()
    plot_EPTA()
    plot_AION()
    plot_AEDGE()
    plot_CE()
    plot_MuARES()
    plot_ALIGOVIRGO()
    plot_Aplus()
    plot_LV()
