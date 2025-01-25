#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:07:19 2025

@author: evana
"""
#%% Libraries
import numpy as np
import pandas as df

#%% Constant values
num_dice = 5  # Number of dice
num_sides = 6  # Number of sides on a six-sided die


#%%functions
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


def find_closest_set(target_set, list_of_sets):
    """
    Find the set in the list that has the most numbers in common with the target set.
    Returns the set, the number of matches, and the matching numbers.

    Args:
        target_set (set): The incoming set to compare.
        list_of_sets (list of sets): A list of sets to check against.

    Returns:
        tuple: The set with the most matches, the number of matches, and the matching numbers.
    """
    # Find the set with the largest intersection
    closest_set = max(list_of_sets, key=lambda s: len(target_set & s))
    matching_numbers = list(target_set & closest_set)
    match_count = len(matching_numbers)

    return closest_set, matching_numbers

def reroll(dice_roll, dice_to_keep):
    """
    Parameters
    ----------
    dice_roll : list/array
        Current roll.
    dice_to_keep : list
        list of dice you want to keep, must put each one you want 
        i.e. if you have 1,5,5,4,3 and want the 5's put [5,5].
    Returns
    -------
    New dice roll.
    """
    # Re-roll dice that are not in the keep values
    new_roll = []
    temp_keep_values = dice_to_keep[:]
    for value in dice_roll:
        if value in temp_keep_values:
            new_roll.append(value)  # Keep this die
            temp_keep_values.remove(value)  # Remove one instance of the value
        else:
            new_roll.append(np.random.randint(1, num_sides + 1))  # Re-roll this 
    return new_roll