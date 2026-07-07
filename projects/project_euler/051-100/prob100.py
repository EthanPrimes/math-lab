M0 = 3
M1 = 20
N0 = 2
N1 = 14
while M1 < 10**12:
    M0, N0, M1, N1, = M1, N1, 6*M1 - M0 + 2, 6*N1 - N0 + 2

print(M1)
print(N1)
