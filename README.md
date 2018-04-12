# Luria_Portfolio

Examples of previous work for David Luria

Contents:
----------------------------------------------------------
Beam_Critical_Load.py (Python)

Calculates the critical buckling load of a beam from a compressing force, given the beam's Young's modulus (E), moment of inertia (J), and length (L). Uses the finite differences method to estimate the differential operator of the beam deformation (y) as a matrix (A):

−E J y'' = P y

Then solves the system as an eigenvalue problem for the lowest eigenvalue using the reverse power method. The eigenvalue is used to calculate the critical buckling load.

-------------------------------------------------------------
Game_of_Chance.cpp (C++)

Simple dice game console application with a wager system. The user starts with $100 in the bank. They select a number 1-6 and a wager, then 3 dice are rolled. If one roll matches the user's number, the user wins. Otherwise, they lose. The game will continue until the user is out of money or chooses to quit. The user's wins and losses are tracked and reported after each turn.

--------------------------------------------------------------
Muon_Collection.py (Python)

Script that automates the collection of muons (cosmic rays) from a photomultiplier tube. The photomultiplier system detects cosmic ray particles striking it and saves the detections as plots on an oscilloscope. On the oscilloscope, a mask can be applied to the detections to separate detections with a muon signature. This script communicates with the oscilloscope to automate the process of collecting cosmic ray detections, applying the mask, and saving the muon detection plots to the computer for data analysis.
