tri_nums = set(n*(n+1)/2 for n in range(1, 2000))

nearest_dist = float("inf")
dists = {abs(t1*t2 - 2*10**6): (t1, t2) for t1 in tri_nums for t2 in tri_nums}

t1, t2 = dists[min(dists.keys())]
a, b = round(pow(2 * t1, 1/2)), round(pow(2 * t2, 1/2))
print(t1 * t2)
print(a * b)
print(a, b)
