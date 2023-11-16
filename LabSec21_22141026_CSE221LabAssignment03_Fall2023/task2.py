#Task 2
in2 = open("Input2.txt", "r")
input_data = in2.readline()
lst = in2.read().split(" ")
lst = list(map(int, lst))
lenght = len(lst)
def findMax(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    max_left = findMax(arr, left, mid)
    max_right = findMax(arr, mid + 1, right)
    return max(max_left, max_right)

max_value = findMax(lst, 0, lenght - 1)
result = str(max_value)
out2 = open("output2.txt", "w")
out2.write(result)
out2.close()
