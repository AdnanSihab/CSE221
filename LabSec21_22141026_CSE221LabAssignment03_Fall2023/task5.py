#Task 5
in5 = open("input5.txt", "r")
in5_first_line = int(in5.readline())
elements = list(map(int, in5.read().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left, equal, right = [], [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            right.append(x)
    return quick_sort(left) + equal + quick_sort(right)
sorted_elements = quick_sort(elements)
output = ""
for i in range(len(sorted_elements)):
    if i == len(sorted_elements) - 1:
        output += str(sorted_elements[i])
    else:
        output += str(sorted_elements[i]) + " "

output_file = open("output5.txt", "w")
output_file.write(output)
output_file.close()
