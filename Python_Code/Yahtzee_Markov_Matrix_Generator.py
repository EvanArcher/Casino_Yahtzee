#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:27:44 2025

@author: evana

This code will simulate many runs finding the initial set up matrix odds, S
and then find the transition matrix odds

hands are
Single
Pair
2 pair
3 of a kind
4 of a kind
yahtzee
small straight
large straight


"""
#%%Libraries
import numpy as np
import pandas as pd
import Yahztee_Function_Library as yfl

#%% Constants
num_dice = 5  # Number of dice
num_sides = 6  # Number of sides on a six-sided die

#%% Define the states
states = [
    "Single",
    "Pair",
    "Two Pair",
    "Three of a Kind",
    "Full House",
    "Four of a Kind",
    "Yahtzee",
    "Small Straight",
    "Large Straight",
]

# Create an empty matrix (all zeros initially)
markov_matrix = np.zeros((len(states), len(states)))
s_matrix = np.zeros((1, len(states))) #matrix of initial rolls to get distribution
# Create a DataFrame with the same names for both indices and columns
s_df = pd.DataFrame(s_matrix, columns=states)
markov_df = pd.DataFrame(markov_matrix, index=states, columns=states)

# Display the matrix
print(markov_df)

def find_s_matrix():
    print(num_dice)