"""
This script computes Gijswijt's sequence. The commented out version is an O(n^3) algorithm, while the new version is faster, although it appears to have the same complexity.
"""
from time import perf_counter as pf
from math import ceil
import numpy as np
from matplotlib import pyplot as plt

num_terms = int(input("Terms to compute: "))

# Determine how much of the sequence has already been computed
try:
    with open("gijswijt.txt", "r") as file:
        sequence = [int(line.strip()) for line in file]
except:
    sequence = []

num_prec_terms = len(sequence)

# def rep_suffixes(seq):
#     """
#     Determines the greatest natural number k so that seq = y^k, where y is a string / sequence.
#     """
#     n = len(seq)

#     for k in reversed(range(1, len(seq) + 1)):
#         if not (n % k):  # k must divide n
#             # Creating a set containing the k substrings
#             strings = set(tuple(seq[(n // k) * i: (n // k) * (i + 1)]) for i in range(k))
#             if len(strings) == 1:
#                 return k

# def curling_number(seq):
#     """
#     Computes the curling number of `seq`, the greatest natural number k so that seq = xy^k, where x and y are strings / sequences. Iterates through all lengths of x and returns the largest value of k that rep_suffixes yields on the input sequence y^k.
#     """
#     # Looping through all possible lengths of x
#     return max([1] + [rep_suffixes(seq[i:]) for i in range(0, len(seq))])

def curling_number(seq):
    """
    Computes the curling number of `seq`, the greatest natural number k so that seq = xy^k, where x and y are strings / sequences. Iterates through all lengths of y.
    """
    # Iterate through all lengths of y
    back_seq = seq[::-1]
    max_k = 1
    n = len(seq)

    # Once n // len_y <= k, we can stop the algorithm, since `seq` cannot have more than len_y * k terms
    len_y = 1
    while n // len_y > max_k:
        # Determining the new maximum k
        curr_k = 1
        prefix = back_seq[0: len_y]
        i = 1
        while (i + 1) * len_y <= len(seq) and back_seq[i * len_y: (i + 1) * len_y] == prefix:
            curr_k += 1
            i += 1
        max_k = max(max_k, curr_k)
        len_y += 1
    
    return max_k


# Computing and saving the sequence
start_time = pf()
seq_len = num_prec_terms
compute_times = []
while seq_len < num_terms:
    start = pf()
    sequence.append(curling_number(sequence))
    compute_times.append(pf() - start)
    seq_len += 1

# Printing and saving the results
print(sequence[:num_terms])
print(f"Runtime: {pf() - start_time}")

if num_terms > num_prec_terms:
    with open("gijswijt.txt", "a") as file:
        for elt in sequence[num_prec_terms:]:
            file.write(str(elt) + "\n")

# Graphing the computation times
x = list(range(num_prec_terms, len(sequence)))
for elt in set(sequence[num_prec_terms:]):
    mask = [s == elt for s in sequence[num_prec_terms:]]
    plt.scatter(np.array(x)[mask], np.array(compute_times)[mask], label=str(elt))
plt.legend()
plt.xlabel("term n")
plt.ylabel("computation time")
plt.title("Computation Time of Terms and Their Values")
plt.show()
