def calculate_probabilities_dynamic(n, m, c):
    probabilities = [[1 / m] + [0] * (n - 1) for _ in range(m)]
    mid = (m - 1) // 2

    for i in range(1, n):
        large = sum(probabilities[k][i - 1] for k in range(mid, m))
        small = sum(probabilities[k][i - 1] for k in range(mid))

        for k in range(m):
            smaller_than_k = sum(probabilities[m][i - 1] for m in range(k))
            larger_than_k = sum(probabilities[m][i - 1] for m in range(k + 1, m))

            if k < mid:
                probabilities[k][i] = (smaller_than_k + large) / (m - 1)
            elif k == mid:
                probabilities[k][i] = (smaller_than_k + large) / (m - 1)
                probabilities[k][i] -= probabilities[k][i - 1] / (m - 1)
            elif k > mid:
                probabilities[k][i] = (larger_than_k + small) / (m - 1)

    column_sums = [sum(col) for col in zip(*probabilities)]
    column_sums_times_c = [sum * c[i] for i, sum in enumerate(column_sums)]

    return probabilities, column_sums, column_sums_times_c

# Example with numbers from 1 to 5 and vector c (0, 10, 100, 1000)
m = 5
n = 4
c = [0, 10, 100, 1000]

probabilities, column_sums, column_sums_times_c = calculate_probabilities_dynamic(n, m, c)

print("Probabilities:")
for row in probabilities:
    print(row)

print("\nColumn Sums:")
print(column_sums)

print("\nColumn Sums Times c:")
print(column_sums_times_c)
