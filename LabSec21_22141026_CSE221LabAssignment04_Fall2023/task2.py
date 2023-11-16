# Task2
from collections import deque

input_file_2 = open("Input2.txt", "r")
input_data_2 = input_file_2.readline().split(" ")
lst_2 = list(map(int, input_data_2))
input_lines_2 = input_file_2.read().split("\n")
arr_2 = []

for line_2 in input_lines_2:
    lst1_2 = line_2.split(" ")
    arr_2.append([int(lst1_2[0]), int(lst1_2[1])])

c = lst_2[0]
r = lst_2[1]
dict2 = {}

for i_2 in arr_2:
    if i_2[0] in dict2:
        lst_2 = dict2[i_2[0]] + [i_2[1]]
        dict2[i_2[0]] = lst_2
    else:
        dict2[i_2[0]] = [i_2[1]]
    if i_2[1] in dict2:
        lst_2 = dict2[i_2[1]] + [i_2[0]]
        dict2[i_2[1]] = lst_2
    else:
        dict2[i_2[1]] = [i_2[0]]


def bfs(dic, ind):
    queue = deque([ind])
    path = []
    while queue:
        node = queue.popleft()
        if node not in path:
            path.append(node)
            for i_2 in dic[node]:
                if i_2 not in path:
                    queue.append(i_2)
    return path


path_2 = bfs(dict2, 1)
output_2 = ""
i_2 = 0
while i_2 < len(path_2):
    output_2 += f"{path_2[i_2]} "
    i_2 += 1

output_file_2 = open("Output2.txt", "w")
output_file_2.write(output_2)
output_file_2.close()
