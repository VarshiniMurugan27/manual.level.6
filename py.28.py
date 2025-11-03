n = 5  # maximum width (center of the arrow)

# Top half
for i in range(1, n + 1):
    print("* " * i)

# Bottom half
for i in range(n - 1, 0, -1):
    print("* " * i)
