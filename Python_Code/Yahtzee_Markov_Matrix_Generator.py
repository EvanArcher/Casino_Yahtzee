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

def find_s_matrix(num_sims):
    """
    Parameters
    -------
    num_sims: number of simulations to find s_matrix
    Returns
    -------
    s_matrix: our initial probability matrix
    """
    # Create an empty matrix (all zeros initially)
    markov_matrix = np.zeros((len(states), len(states)))
    s_matrix = np.zeros((1, len(states))) #matrix of initial rolls to get distribution
    # Create a DataFrame with the same names for both indices and columns
    s_df = pd.DataFrame(s_matrix, columns=states)
    markov_df = pd.DataFrame(markov_matrix, index=states, columns=states)

    # Display the matrix
    print(markov_df)
    
    for i in range(0,num_sims):
        dice_roll = list((np.random.randint(1, num_sides + 1, num_dice)))
        rolled_hands = yfl.hand_type(dice_roll)
        for hand in rolled_hands:
            markov_df.loc[hand,hand] += 1
    print(markov_df/num_sims)
    return markov_df/num_sims

def save_matrix(df,save_name):
    """
    Parameters
    -------
    df: dataframe to be saved
    save_name: path or name of df you would like to save
    -------
    Returns
    -------
    None
    """
    if save_name.endswith('.csv'):
        save_name = save_name
    else:
        save_name = save_name + '.csv'
        
    df.to_csv(save_name, index =True)
    
def find_trans_matrix():
    """
    Parameters
    -------
    num_sims: How many times we want to sim 
    -------
    Returns
    -------
    trans_matrix: (dataframe) matrix highlighting transistion probabilities
    """
    