#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:07:19 2025

@author: evana
"""
import numpy as np
import pandas as df

# Function to fill the first blank spot in a column, or append a new row if no blank spots
def dynamic_fill(df, column, value):
    # Check if there are any blank (NaN) spots in the column
    blank_spots = df[column].isna()
    
    if blank_spots.any():
        # Fill the first blank spot
        first_blank_index = blank_spots.idxmax()
        df.at[first_blank_index, column] = value
    else:
        # If no blank spots, append a new row with NaN for all other columns
        new_row = {col: (value if col == column else np.nan) for col in df.columns}
        df = df.append(new_row, ignore_index=True)
    
    return df
