# Task1A
input_file_1a = open("Input1a.txt", "r")
input_data_1a = input_file_1a.readline().split(" ")
dimensions_1a = list(map(int, input_data_1a))
input_lines_1a = input_file_1a.read().split("\n")
matrix_data_1a = []

for line_1a in input_lines_1a:
    line_values_1a = line_1a.split(" ")
    values_1a = list(map(int, line_values_1a))
    matrix_data_1a.append(values_1a)

n_1a = dimensions_1a[0]
matrix_1a = [[0] * (n_1a + 1) for i_1a in range(n_1a + 1)]
output_1a = ""
count_1a = 0

for entry_1a in matrix_data_1a:
    matrix_1a[entry_1a[0]][entry_1a[1]] = entry_1a[2]

for row_1a in matrix_1a:
    count_1a += 1
    for value_1a in row_1a:
        output_1a += f"{value_1a} "
    if count_1a != len(matrix_1a):
        output_1a += "\n"

output_file_1a = open("Output1a.txt", "w")
output_file_1a.write(output_1a)
output_file_1a.close()
