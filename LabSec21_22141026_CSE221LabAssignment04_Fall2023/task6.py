# Task 6
from collections import deque

input_file_6 = open("Input6.txt", "r")
input_data_6 = input_file_6.readline().split(" ")
lst_6 = list(map(int, input_data_6))
input_lines_6 = input_file_6.read().split("\n")
arr_6 = []

for line_6 in input_lines_6:
    lst_6 = []
    for j_6 in line_6:
        lst_6 += [j_6]
    arr_6.append(lst_6)


def diamond_collect(arr):
    max_count = 0
    for i_6 in range(len(arr)):
        for j_6 in range(len(arr[0])):
            if arr_6[i_6][j_6] == ".":
                count = dfs(arr_6, i_6, j_6)
                if count >= max_count:
                    max_count = count
    return max_count


def dfs(arr, idx1, idx2):
    if idx1 < 0 or idx1 >= len(arr) or idx2 < 0 or idx2 >= len(arr[0]):
        return 0
    elif arr[idx1][idx2] == '#' or arr[idx1][idx2] == 'V':
        return 0
    elif arr[idx1][idx2] == "D":
        count = 1
    else:
        count = 0
    arr[idx1][idx2] = "V"
    count += dfs(arr, idx1 - 1, idx2)
    count += dfs(arr, idx1, idx2 - 1)
    count += dfs(arr, idx1 + 1, idx2)
    count += dfs(arr, idx1, idx2 + 1)
    return count


ans_6 = diamond_collect(arr_6)
output_6 = str(ans_6)
output_file_6 = open("Output6.txt", "w")
output_file_6.write(output_6)
output_file_6.close()
