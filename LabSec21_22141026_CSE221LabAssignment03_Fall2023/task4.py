#Task 4
in4 = open("Input4.txt", "r")
in4_first_line = in4.readline()
data = in4.read().split(" ")
lst = list(map(int, data))

def find_max_and_merge(left, right):
    i,j,index = 0,0,0
    merged_lst = []
    max_val = None
    while index < len(right):
        if max_val is None or max_val < left[-1] + (right[index] ** 2):
            max_val = left[-1] + (right[index] ** 2)
        index += 1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_lst.append(left[i])
            i = i + 1
        else:
            merged_lst.append(right[j])
            j = j + 1
    if i < len(left):
        merged_lst += left[i:]
    if j < len(right):
        merged_lst += right[j:]
    return merged_lst, max_val

def merge_sort_with_max(lst):
    if len(lst) == 1:
        return lst, 0
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left, left_max = merge_sort_with_max(left)
    right, right_max = merge_sort_with_max(right)
    merged_lst, maximum = find_max_and_merge(left, right)
    return merged_lst, max(maximum, left_max, right_max)

result = merge_sort_with_max(lst)
output = str(result[1])
out4 = open("output4.txt", "w")
out4.write(output)
out4.close()
