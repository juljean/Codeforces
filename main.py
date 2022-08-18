from math import log2, ceil


def query(arr: list, L: int, R: int, par, lookup) -> int:

    # Find the biggest block of size 2^p that fits in the range (left) ... (right).
    # For [2,10], j = 3
    j = int(log2(R - L + 1))

    # For [2,10], we compare
    # arr[lookup[0][3]] and
    # arr[lookup[3][3]],
    if par == "min":
        if (arr[lookup[L][j]] <=
                arr[lookup[R - (1 << j) + 1][j]]):
            return arr[lookup[L][j]]
        else:
            return arr[lookup[R - (1 << j) + 1][j]]
    else:
        if (arr[lookup[L][j]] >=
                arr[lookup[R - (1 << j) + 1][j]]):
            return arr[lookup[L][j]]
        else:
            return arr[lookup[R - (1 << j) + 1][j]]


def preprocess(arr, n, lookup_min, lookup_max):
    # Diagonal fill-up
    for i in range(n):
        lookup_min[i][0] = i
        lookup_max[i][0] = i

    j = 1
    while (1 << j) <= n:

        # Compute minimum value for
        # all intervals with size 2^j
        i = 0
        while i + (1 << j) - 1 < n:
            # min

            # For arr[2][10], we compare
            # arr[lookup[0][3]] and
            # arr[lookup[3][3]]
            if arr[lookup_min[i][j - 1]] < arr[lookup_min[i + (1 << (j - 1))][j - 1]]:
                lookup_min[i][j] = lookup_min[i][j - 1]
            else:
                lookup_min[i][j] = lookup_min[i + (1 << (j - 1))][j - 1]

            # max
            if arr[lookup_max[i][j - 1]] > arr[lookup_max[i + (1 << (j - 1))][j - 1]]:
                lookup_max[i][j] = lookup_max[i][j - 1]
            else:
                lookup_max[i][j] = lookup_max[i + (1 << (j - 1))][j - 1]

            i += 1
        j += 1


def calculate(arr, l, r, lookup_min, lookup_max, length):
    counter = 0
    while True:
        if l == 0 and r == length - 1:
            print(counter)
            break

        l_new = query(arr, l, r, "min", lookup_min)
        r_new = query(arr, l, r, "max", lookup_max)

        if l == r or (l == l_new - 1 and r == r_new - 1):
            print(-1)
            break

        l = l_new - 1
        r = r_new - 1

        counter += 1


def start_point():
    length, times = map(int, input().split())
    array = list(map(int, input().split()))

    sparse_matrix_length = ceil(log2(len(array))) + 1
    lookup_min = [[0 for j in range(sparse_matrix_length)]
                  for i in range(length)]

    lookup_max = [[0 for k in range(sparse_matrix_length)]
                  for n in range(length)]

    preprocess(array, length, lookup_min, lookup_max)
    for t in range(times):
        l, r = map(int, input().split())
        calculate(array, l - 1, r - 1, lookup_min, lookup_max, length)

start_point()