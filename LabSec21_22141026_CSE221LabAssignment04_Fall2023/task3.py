# Task3
from collections import deque

input_file_3 = open("Input3.txt", "r")
input_data_3 = input_file_3.readline().split(" ")
lst_3 = list(map(int, input_data_3))
input_lines_3 = input_file_3.read().split("\n")
arr_3 = []

for line_3 in input_lines_3:
    lst1_3 = line_3.split(" ")
    arr_3.append([int(lst1_3[0]), int(lst1_3[1])])

c = lst_3[0]
r = lst_3[1]
dict3 = {}

for i_3 in arr_3:
    if i_3[0] in dict3:
        lst_3 = dict3[i_3[0]] + [i_3[1]]
        dict3[i_3[0]] = lst_3
    else:
        dict3[i_3[0]] = [i_3[1]]
    if i_3[1] in dict3:
        lst_3 = dict3[i_3[1]] + [i_3[0]]
        dict3[i_3[1]] = lst_3
    else:
        dict3[i_3[1]] = [i_3[0]]


def dfs(dic, ind):
    stack = [ind]
    path = []

    while stack:
        node = stack.pop()
        if node not in path:
            path.append(node)
            stack.extend(reversed(dic[node]))

    return path


ans_3 = dfs(dict3, 1)
output_3 = ""
i_3 = 0
while i_3 < len(ans_3):
    output_3 += f"{ans_3[i_3]} "
    i_3 += 1

output_file_3 = open("Output3.txt", "w")
output_file_3.write(output_3)
output_file_3.close()