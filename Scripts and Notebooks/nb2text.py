# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:47:14 2023

@author: kelly
"""
import nbformat
import os

path = r"C:\Users\kelly\OneDrive - University of Toronto\GitHub\BrainStationCapstone\Scripts and Notebooks\Cleaning Scripts\NB2_2023-03-04 Journal Data Frame Cleaning.ipynb"

# Define the name of the output file
name = '_'.join([os.path.basename(path), 'nb2txt_out.txt'])

# Read the Jupyter notebook file as a dictionary
with open(path, 'r') as f:
    with open(name, 'a') as g:
        nb_dict = nbformat.read(f, as_version=4)
        cell_dic = nb_dict['cells']
        for i in range(len(cell_dic)):
            if cell_dic[i]['cell_type'] == 'markdown':
                g.write(cell_dic[i]['source'])
                g.write('\n')