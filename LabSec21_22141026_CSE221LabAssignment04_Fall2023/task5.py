# Task5
from collections import deque

input_file_5 = open("Input5.txt", "r")
input_data_5 = input_file_5.readline().split(" ")
lst_5 = list(map(int, input_data_5))
input_lines_5 = input_file_5.read().split("\n")
arr_5 = []

for line_5 in input_lines_5:
    lst1_5 = line_5.split(" ")
    arr_5.append([int(lst1_5[0]), int(lst1_5[1])])

c = lst_5[0]
r = lst_5[1]
destination_5 = lst_5[2]
dict5 = {}

for i_5 in arr_5:
    if i_5[0] in dict5:
        lst_5 = dict5[i_5[0]] + [i_5[1]]
        dict5[i_5[0]] = lst_5
    else:
        dict5[i_5[0]] = [i_5[1]]
    if i_5[1] in dict5:
        lst_5 = dict5[i_5[1]] + [i_5[0]]
        dict5[i_5[1]] = lst_5
    else:
        dict5[i_5[1]] = [i_5[0]]


def bfs(dic, ind, des):
    queue = deque([[ind, [ind]]])
    lst = []
    while queue:
        city, path = queue.popleft()
        lst.append(city)
        if city == des:
            return path, len(path) - 1
        for x in dic[city]:
            if x not in lst:
                queue.append([x, path + [x]])


path_5, time_5 = bfs(dict5, 1, destination_5)
output_5 = f"Time: {time_5}\nShortest Path: "
for i_5 in path_5:
    output_5 += f"{i_5} "

output_file_5 = open("Output5.txt", "w")
output_file_5.write(output_5)
output_file_5.close()
