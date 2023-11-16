# Task1B
input_file_1b = open("Input1b.txt", "r")
input_data_1b = input_file_1b.readline().split(" ")
lst_1b = list(map(int, input_data_1b))
input_lines_1b = input_file_1b.read().split("\n")
arr_1b = []

for line_1b in input_lines_1b:
    lst1_1b = line_1b.split(" ")
    lst2_1b = list(map(int, lst1_1b))
    arr_1b.append(lst2_1b)

n_1b = lst_1b[0]
ans_1b = [[i] for i in range(n_1b + 1)]
output_1b = ""

i_1b = 0
while i_1b < len(ans_1b):
    j_1b = 0
    while j_1b < len(arr_1b):
        if ans_1b[i_1b][0] == arr_1b[j_1b][0]:
            ans_1b[i_1b].append((arr_1b[j_1b][1], arr_1b[j_1b][2]))
        j_1b += 1
    i_1b += 1


for i_1b in range(len(ans_1b)):
    output_1b += f"{i_1b}: "
    if len(ans_1b[i_1b]) != 1:
        for j_2_1b in range(1, len(ans_1b[i_1b])):
            output_1b += f"{ans_1b[i_1b][j_2_1b]} "
    if i_1b != len(ans_1b) - 1:
        output_1b += f"\n"

output_file_1b = open("Output1b.txt", "w")
output_file_1b.write(output_1b)
output_file_1b.close()
