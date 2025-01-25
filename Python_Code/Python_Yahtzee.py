#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:54:40 2025

@authors: Chase Archer and Evan Archer 
This code plays yahtzee with you
"""

import numpy as np

def casino_yahtzee(num_trials):
    """
    CasinoYahtzee: Simulates rolling five six-sided dice multiple times.
    Allows selecting dice to keep by their numerical values and re-rolling the others up to two more times.
    Determines if the result is a win (three of a kind, full house, small straight, or large straight).

    Args:
        num_trials (int): Number of trials (games) to roll the dice.

    Returns:
        list: Boolean list where each entry is True if the trial is a win, False otherwise.
    """
    num_dice = 5  # Number of dice
    num_sides = 6  # Number of sides on a six-sided die

    # Winning condition helper sets
    small_straight_sets = [
        {1, 2, 3, 4},
        {2, 3, 4, 5},
        {3, 4, 5, 6}
    ]
    large_straight_sets = [
        {1, 2, 3, 4, 5},
        {2, 3, 4, 5, 6}
    ]

    # Initialize win list
    wins = [False] * num_trials

    for trial in range(num_trials):
        # Initial roll of all dice
        dice_rolls = np.random.randint(1, num_sides + 1, num_dice)
        print(f"Initial roll for trial {trial + 1}: {dice_rolls.tolist()}")

        # Allow up to two re-rolls
        for reroll in range(2):
            # Ask user for which dice values to keep
            keep_values = input("Enter the values of the dice you want to keep, separated by spaces (e.g., '3 5'): ")
            keep_values = [int(val) for val in keep_values.split()] if keep_values.strip() else []

            # Re-roll dice that are not in the keep values
            new_roll = []
            temp_keep_values = keep_values[:]
            for value in dice_rolls:
                if value in temp_keep_values:
                    new_roll.append(value)  # Keep this die
                    temp_keep_values.remove(value)  # Remove one instance of the value
                else:
                    new_roll.append(np.random.randint(1, num_sides + 1))  # Re-roll this die

            dice_rolls = np.array(new_roll)
            print(f"Roll after re-roll {reroll + 1}: {dice_rolls.tolist()}")

        # Sort the dice rolls for checking conditions
        roll = sorted(dice_rolls)

        # Count occurrences of each die face
        counts = [roll.count(i) for i in range(1, num_sides + 1)]

        # Check for three of a kind, four of a kind, full house, or Yahtzee
        has_three_of_a_kind = 3 in counts
        has_four_of_a_kind = 4 in counts
        has_yahtzee = 5 in counts
        has_pair = counts.count(2) == 1
        full_house = has_three_of_a_kind and has_pair

        # Check for small straight (four consecutive numbers)
        has_small_straight = any(set(range(start, start + 4)).issubset(set(roll)) for start in range(1, 4))

        # Check for large straight (five consecutive numbers)
        has_large_straight = any(set(range(start, start + 5)).issubset(set(roll)) for start in range(1, 3))

        # Determine win condition
        if full_house or has_three_of_a_kind or has_small_straight or has_large_straight or has_four_of_a_kind or has_yahtzee:
            wins[trial] = True
            print("Win")
        else:
            print("Lose")

    return wins
