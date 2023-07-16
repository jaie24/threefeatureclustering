# IMPORT LIBRARIES
import sklearn
assert sklearn.__version__ >= "0.20"

import numpy as np
import os
import csv

# Using pandas to format datasets
import pandas as pd

# To make this notebook's output stable across runs
np.random.seed(42)

# Pretty figures
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

import math # For log and mean operations

# ------ FIRST DATASET : FLUID SHEAR STRESS -------
# OPEN FIRST DATASET 
# READ FIRST DATASET

# ------ SECOND DATASET : POSTPARTUM BREAST CANCER ------
# OPEN SECOND DATASET
# READ SECOND DATASET

# ------ THIRD DATASET : AMP CELLULAR RESPONSE ---------
# OPEN THIRD DATASET
# READ THIRD DATASET

# COMBINE ALL THREE DATASETS INTO ONE DATAFRAME
# SCALING THE DATA 


# ---------------------- K MEANS CLUSTERING --------------------

# PLOTTING
# DETERMINING NUMBER OF CLUSTERS