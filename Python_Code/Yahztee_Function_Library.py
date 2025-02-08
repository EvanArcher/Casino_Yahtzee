#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:07:19 2025

@author: evana
"""
#%% Libraries
import numpy as np
import pandas as pd
from collections import Counter
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
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
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

def has_nums_in_order(numbers, nums_in_a_row):
    """
    Check if at least 3 numbers in the set are in consecutive ascending order.

    Args:
        numbers (set or list): A set or list of numbers.
        nums_in_a_row (int): Value saying how many numbers you need in a row

    Returns:
        bool: True if at least 3 numbers are in order, False otherwise.
    """
    sorted_numbers = sorted(set(numbers))  # Sort the numbers
    count = 1  # Count consecutive numbers

    # Iterate through the sorted numbers to check for consecutive order
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] == sorted_numbers[i - 1] + 1:  # Check if consecutive
            count += 1
            if count == nums_in_a_row:  # Found at least x in order
                return True
        else:
            count = 1  # Reset the count if not consecutive

    return False  # No x consecutive numbers found



def find_number_pairs(numbers):
    """
    Find all pairs (two identical numbers) from the list and return them.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: List of all pairs of numbers.
    """
    counts = Counter(numbers)
    
    # Build the list of pairs
    pairs = []
    for num, count in counts.items():
        if count >= 2:
            pairs.extend([num] * count)
    
    return pairs

def hand_type(hand):
    """
    Parameters
    ----------
    hand : (list) list of numbers in the hand

    Returns
    -------
    hand type as a string
    "Single",
    "Pair",
    "Two Pair",
    "Three of a Kind",
    "Full House",
    "Four of a Kind",
    "Yahtzee",
    "Small Straight",
    "Large Straight",
    """
    # Look at hands from biggest to smallest
    pairs = find_number_pairs(hand)
    hand_list = []
    if len(pairs) == 5 and len(set(pairs)) == 1:
        hand_list.append('Yahtzee')
        return hand_list
    if len(pairs) == 5 and len(set(pairs)) == 2:
        hand_list.append('Full House')
        return hand_list
    if len(pairs) == 4:
        hand_list.append('Four of a Kind')
        return hand_list
    if len(pairs) == 3:
        hand_list.append('Three of a Kind')
        return hand_list
    if len(pairs) == 2:
        hand_list.append('Two Pair')
    if len(pairs) == 1:
        hand_list.append('Single')
    if has_nums_in_order(hand,5):
        hand_list.append('Large Straight')
        return hand_list
    if has_nums_in_order(hand, 4):
        hand_list.append('Small Straight')
    return hand_list
        
    
    
    
    
    
    
    
    