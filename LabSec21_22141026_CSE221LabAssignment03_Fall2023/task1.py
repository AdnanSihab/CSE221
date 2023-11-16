#Task 1
in1 = open("Input1.txt", "r")
input_data = in1.readline()
lst = in1.read().split(" ")
lst = list(map(int, lst))
def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

sorted_numbers = mergeSort(lst)
output = ""
for num in sorted_numbers:
    output += str(num) + " "

out1 = open("output1.txt", "w")
out1.write(output)
out1.close()
