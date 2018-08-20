'''
copyright CSE450@asu 




'''

import os, platform
import numpy as np 
import pandas as pd


this_dir = os.getcwd()

test_dir = os.path.join(this_dir, 'test_files')

#run tests for each test_file

for m_file in os.listdir(test_dir):
    if m_file.endswith('.csv'):
        print(m_file)


