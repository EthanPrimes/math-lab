from collections import defaultdict
import time
import turtle

import turtle2img

N = 20
# Finding all displacements of odd edges
odd_dict = {1: [1]}
for i in range(1, N + 1):
    val = 2*i + 1
    odd_dict[val] = list(k + v for k in odd_dict[val - 2] for v in [-val, val])

# Finding all displacements of even edges
even_dict = {2: [2]}
for i in range(1, N + 1):
    val = 2*i + 2
    even_dict[val] = list(k + v for k in even_dict[val - 2] for v in [-val, val])

odd_seqs = defaultdict(list)
even_seqs = defaultdict(list)

for i in range(N):
    zeros_in_odd = [i for i, val in enumerate(odd_dict[2*i+1]) if val == 0]
    for z in zeros_in_odd:
        res = bin(z)[2:]
        odd_seqs[2*i+1].append("1" + (i - len(res)) * "0" + res)
    zeros_in_even = [i for i, val in enumerate(even_dict[2*i+2]) if val == 0]
    for z in zeros_in_even:
        res = bin(z)[2:]
        even_seqs[2*i+2].append("1" + (i - len(res)) * "0" + res)

def move_turtle_in_sequence(seq, lens, scale=5):
    """Creates a turtle drawing.

    Turns in accordance to the items in seq and travels in lengths
    given by lens.
    """
    vert = True  # Tracks horizontal vs. vertical movement
    for i, dir in enumerate(seq):
        if dir == "1":
            if vert:
                turtle.setheading(90)
            else:
                turtle.setheading(0)
        else:
            if vert:
                turtle.setheading(270)
            else:
                turtle.setheading(180)

        turtle.forward(lens[i] * scale)
        vert = not vert

    # turtle.exitonclick()

# move_turtle_in_sequence("1100001100111100", list(range(1, 17)))

def build_direction_seqs(n, even_first=False):
    # n is the index of the first term we're looking at
    res = []
    for i in range(len(odd_seqs[n + even_first])):
        for j in range(len(even_seqs[n + 1 - even_first])):
            res.append("".join(val for a, b in zip(odd_seqs[n + even_first][i], even_seqs[n + 1 - even_first][j]) for val in [a, b]))

    return res

print(odd_seqs.keys())
print(even_seqs.keys())

M = 23
seqs = build_direction_seqs(M, even_first=False)
for index, seq in enumerate(seqs):
    turtle.title(f"{index} / {len(seqs)}")
    move_turtle_in_sequence(seq, list(range(1, M+2)))
    turtle.resetscreen()

# for index, seq in enumerate(build_direction_seqs(15)):
#     if index in [21, 24, 27]:
#         turtle.title(f"{index}")
#         move_turtle_in_sequence(seq, list(range(1, 17)))
#         ts = turtle.getscreen()
#         ts.getcanvas().postscript(file=f"projects/lines_forming_closed_shapes/turtle_{index}.eps")
#         turtle.resetscreen()
