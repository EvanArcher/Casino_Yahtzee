#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 07:34:48 2025

@author: evana

This code is trying to loop through a simulation of yahtzee rolls until completion
completion is deemed to be a yahtzee or large straight then it will report the results
"""

#%&Libraries
import numpy as np
import pandas as pd
import Yahztee_Function_Library as yfl

#%% Setup variables and winning hands
num_simulations = 500 #number of games played to completion
num_dice = 5  # Number of dice
num_sides = 6  # Number of sides on a six-sided die
# straight sets
small_straight_sets = [
    {1, 2, 3, 4},
    {2, 3, 4, 5},
    {3, 4, 5, 6}
]
large_straight_sets = [
    {1, 2, 3, 4, 5},
    {2, 3, 4, 5, 6}
    ]
# Other winning Hands are
# 3 of a kind, 4 of a kind, Yahtzee(5 of a kind), full house 
# 3 of a kind = if len(set(hands = 3)), 4 is if len(set(hands)) = 2... so on

#dataframe to hold our information
column_names = ['3_of_a_kind', '4_of_a_kind', '5_of_a_kind', 'full_house', 'small_straight', 'large_straight']
df = pd.DataFrame(columns=column_names)

#%% Loop to simulate hands, will save results to dataframe
yahtzee_counter = 0
for i in range(0,num_simulations):
    roll_count = 0
    dice_roll = list((np.random.randint(1, num_sides + 1, num_dice)))
    # print(dice_roll)
    roll_count += 1
    # Logic to find what to pursue, straights or sets
    # basically if we have a pair, we will go down the straight path x% of the time
    # then go down the set path 1-x% of the time.
    # same logic needs to be done for full house, if at 3 of a kind then x% go
    # for 4 of a kind and yahtzee then 1-x% of the time go for full house
    # however while rolling a full house, a 4 of a kind and yahtzee are possible
    # so we should record those as well.
    # Note: ensure we only record each type of roll 1 time during a run
    
    # if set length is 5 we must have at least a small straight
    if len(set(dice_roll)) == 5:
        df = yfl.dynamic_fill(df,'small_straight', roll_count)
        lg_check = any(set(dice_roll) == lg_set for lg_set in large_straight_sets)
        if lg_check:
            df = yfl.dynamic_fill(df,'large_straight', roll_count)
            # print(set(dice_roll))
            continue
        else: 
            # find which straight we are targeting
            tar_set, dice_to_keep = yfl.find_closest_set(set(dice_roll), large_straight_sets)
            while lg_check == False:
                dice_roll = yfl.reroll(dice_roll, dice_to_keep)
                roll_count += 1
                # print(dice_roll, roll_count)
                lg_check = any(set(dice_roll) == lg_set for lg_set in large_straight_sets)
                tar_set, dice_to_keep = yfl.find_closest_set(set(dice_roll), large_straight_sets)
            # finally have large straight
            df = yfl.dynamic_fill(df,'large_straight', roll_count)
            continue
    
    # check if we pursue a straight since we have 3 in a row
    if yfl.has_nums_in_order(dice_roll, 3):
        sm_check = any(set(dice_roll) == sm_set for sm_set in small_straight_sets)
        lg_check = any(set(dice_roll) == lg_set for lg_set in large_straight_sets)
        if sm_check:
            df = yfl.dynamic_fill(df,'small_straight', roll_count)
            if lg_check:
              df = yfl.dynamic_fill(df,'large_straight', roll_count)  
            # print(set(dice_roll))
            continue
        else:
            # Now need to find what we need to reroll
            # find which straight we are targeting
            tar_set, dice_to_keep = yfl.find_closest_set(set(dice_roll), small_straight_sets)
            while sm_check == False:
                dice_roll = yfl.reroll(dice_roll, dice_to_keep)
                roll_count += 1
                # print(dice_roll, roll_count)
                sm_check = any(set(dice_roll) == sm_set for sm_set in small_straight_sets)
                tar_set, dice_to_keep = yfl.find_closest_set(set(dice_roll), small_straight_sets)
            # finally have small straight
            df = yfl.dynamic_fill(df,'small_straight', roll_count)
            # Now we need to continue until we get a large straight
            lg_check = any(set(dice_roll) == lg_set for lg_set in large_straight_sets)
            if lg_check:
                df = yfl.dynamic_fill(df,'large_straight', roll_count)
                # print(set(dice_roll))
                continue
            else: 
                # find which straight we are targeting
                tar_set, dice_to_keep = yfl.find_closest_set(set(dice_roll), large_straight_sets)
                while lg_check == False:
                    dice_roll = yfl.reroll(dice_roll, dice_to_keep)
                    roll_count += 1
                    # print(dice_roll, roll_count)
                    lg_check = any(set(dice_roll) == lg_set for lg_set in large_straight_sets)
                    tar_set, dice_to_keep = yfl.find_closest_set(set(dice_roll), large_straight_sets)
                # finally have large straight
                df = yfl.dynamic_fill(df,'large_straight', roll_count)
            continue
    
    #Now do set logic/chance to pursue a straight some percent of the time
    if len(yfl.find_number_pairs(dice_roll)) >=2:
        print(dice_roll)
        print(yfl.find_number_pairs(dice_roll))




