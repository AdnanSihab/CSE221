# Task 4
input_file_4 = open("Input4.txt", "r")
input_data_4 = input_file_4.readline().split(" ")
lst_4 = list(map(int, input_data_4))
input_lines_4 = input_file_4.read().split("\n")
arr_4 = []

for line_4 in input_lines_4:
    lst1_4 = line_4.split(" ")
    arr_4.append([int(lst1_4[0]), int(lst1_4[1])])

c = lst_4[0]
r = lst_4[1]
dict4 = {}

for i_4 in range(1, c + 1):
    dict4[i_4] = []

for i_4 in arr_4:
    lst_4 = dict4[i_4[0]] + [i_4[1]]
    dict4[i_4[0]] = lst_4


def cycle_check(dic, city):
    path = [False for i in range(city + 1)]
    lst = [False for i in range(city + 1)]

    for i in range(1, city + 1):
        if not path[i]:
            stack = [(i, iter(dic[i]))]

            while stack:
                current, neighbors = stack[-1]

                try:
                    next_neighbor = next(neighbors)
                    if not path[next_neighbor]:
                        stack.append((next_neighbor, iter(dic[next_neighbor])))
                        path[next_neighbor] = True
                        lst[next_neighbor] = True
                    elif lst[next_neighbor]:
                        return "Yes"
                except StopIteration:
                    stack.pop()
                    lst[current] = False

    return "No"


ans_4 = cycle_check(dict4, c)
output_4 = ans_4
output_file_4 = open("Output4.txt", "w")
output_file_4.write(output_4)
output_file_4.close()
