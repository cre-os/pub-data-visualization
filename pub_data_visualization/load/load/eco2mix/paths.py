
"""
    Folders where the raw auctions data provided by eCO2mix
    and the transformed dataframes are saved.
    
"""

import os
#
from .... import global_var

fpath_load_tmp = os.path.join(global_var.path_transformed,
                              'eCO2mix',
                              'load_{0}_{1}.csv',
                              )
