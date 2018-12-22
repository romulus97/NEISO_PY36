# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:29:55 2018

@author: jkern
"""

############################################################################
#                               DATA SETUP

# This file selects a single year from the synthetic record and organizes the 
# data in a form that is accessible to the unit commitment/economic dispatch
# (UC/ED) simulation model. This script can be interfaced with a data mining
# scheme for selecting specific years to run.
############################################################################


############################################################################
#                         YEAR SELECTION

# Default is that a random year from the synthetic record is selected to be run
# through the UC/ED model. 

import pandas as pd
import numpy as np
year = 0



############################################################################
#                          UC/ED Data File Setup

import NEISO_data_setup
NEISO_data_setup.setup(year)



