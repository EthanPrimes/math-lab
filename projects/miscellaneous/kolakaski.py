"""
Computes terms of the Kolakaski sequence. Goals include determining the frequency of 1's and 2's.
"""
import argparse
from time import perf_counter as pf

# Initialize parser
parser = argparse.ArgumentParser(description="A script that computes terms of the Kolakaski sequence and examines frequencies of the terms.")

# Required arguments
parser.add_argument("terms", type=int, help="The number of terms to compute")

# Optional arguments
parser.add_argument("-f", "--frequency", action="store_true", help="Return the frequency of 1's and 2's.")
parser.add_argument("-p", "--print", action="store_true", help="Print the resulting sequence.")
parser.add_argument("-t", "--timing", action="store_true", help="Time the computation.")

# Parsing inputs
args = parser.parse_args()

# Computing the given terms
start_time = pf()
sequence = [1, 2, 2]
index = 2
term = 1

while len(sequence) < args.terms:
    sequence.extend([term] * sequence[index])
    term = 3 - term
    index += 1

total_time = pf() - start_time

# Returning the results
if args.print:
    print(sequence[:args.terms])

if args.frequency:
    print(f"Frequency of 1: {sequence[:args.terms].count(1) / args.terms}")
    print(f"Frequency of 2: {sequence[:args.terms].count(2) / args.terms}")

if args.timing:
    print(f"Computation time: {total_time}")