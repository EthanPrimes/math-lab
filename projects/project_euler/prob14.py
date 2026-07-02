from collections import defaultdict

def collatz_step(n):
    if n % 2:
        return 3*n + 1
    return n // 2

collatz = defaultdict(int)
collatz[1] = 0

for n in range(2, 10**6):
    curr = n
    steps = 0
    while curr not in collatz.keys():
        curr = collatz_step(curr)
        steps += 1
    collatz[n] = collatz[curr] + steps



print(max(collatz, key=collatz.get))
