# Task 6
in6 = open("input6.txt", "r")
in6_first_line = int(in6.readline())
elem = list(map(int, in6.readline().split()))
in6_second_line = int(in6.readline())
search = list(map(int, in6.read().split("\n")[:-1]))

def quick_select(arr, index, length, k):
    if index <= length:
        x = partition(arr, index, length)
        if k == x:
            return arr[k - 1]
        elif k > x:
            return quick_select(arr, x, length, k)
        else:
            return quick_select(arr, index, x - 1, k)
    return None
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def partition(arr, index, length):
    pivot = arr[length]
    for x in range(index, length):
        if arr[x] <= pivot:
            swap(arr, x, index)
            index += 1
    swap(arr, index, length)
    return index

results = []
for k in search:
    answer = quick_select(elem, 0, len(elem) - 1, k)
    if answer is not None:
        results.append(answer)

output = ""
for i in range(len(results)):
    output += str(results[i])
    if i != len(results) - 1:
        output += "\n"

out6 = open("output6.txt", "w")
out6.write(output)
out6.close()
