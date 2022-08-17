def preprocess(arr, n, lookup_min, lookup_max):
    for i in range(n):
        lookup_min[i][i] = i
        lookup_max[i][i] = i

    for i in range(n):
        for j in range(i + 1, n):
            # max fill-up
            if (arr[lookup_max[i][j - 1]] > arr[j]):
                lookup_max[i][j] = lookup_max[i][j - 1]
            else:
                lookup_max[i][j] = j

            # min fill-up
            if (arr[lookup_min[i][j - 1]] < arr[j]):
                lookup_min[i][j] = lookup_min[i][j - 1]
            else:
                lookup_min[i][j] = j


def calculate(arr, l, r, lookup_min, lookup_max, length):
    counter = 0
    while True:

        if l == 0 and r == length - 1:
            print(counter)
            break

        l_new = arr[lookup_min[l][r]]
        r_new = arr[lookup_max[l][r]]

        if l == r or (l == l_new - 1 and r == r_new - 1):
            print(-1)
            break

        l = l_new - 1
        r = r_new - 1

        counter += 1


def start_point():
    length, times = map(int, input().split())
    array = list(map(int, input().split()))

    lookup_min = [[0 for j in range(length)]
                  for i in range(length)]

    lookup_max = [[0 for k in range(length)]
                  for n in range(length)]

    preprocess(array, length, lookup_min, lookup_max)
    for t in range(times):
        l, r = map(int, input().split())
        calculate(array, l - 1, r - 1, lookup_min, lookup_max, length)

