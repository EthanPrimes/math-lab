N = 10**5
pent_list = [n*(3*n - 1) // 2 for n in range(1, N + 1)]
pent_set = set(pent_list)

min_diff = float("inf")
for i in range(N):
    for j in range(i + 1, N):
        plj = pent_list[j]
        pli = pent_list[i]
        if plj - pli in pent_set and plj + pli in pent_set:
            min_diff = min(min_diff, plj - pli)

print(min_diff)
