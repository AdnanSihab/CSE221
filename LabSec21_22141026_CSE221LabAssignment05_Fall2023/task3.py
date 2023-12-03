# Task3
input_file = open("Input3.txt", "r")
input_data = input_file.readline().split(" ")
num_vertices = list(map(int, input_data))
input_lines = input_file.read().split("\n")
edges = []
course_graph = {}
reverse_graph = {}
vertices_list = []
for line in input_lines:
    line_data = line.split(" ")
    line_values = list(map(int, line_data))
    edges.append(line_values)
for edge in edges:
    if edge[0] not in course_graph:
        course_graph[edge[0]] = [edge[1]]
        vertices_list += [edge[0]]
    else:
        temp_list = course_graph[edge[0]]
        temp_list += [edge[1]]
        course_graph[edge[0]] = temp_list
for edge in edges:
    if edge[1] not in reverse_graph:
        reverse_graph[edge[1]] = [edge[0]]
    else:
        temp_list = reverse_graph[edge[1]]
        temp_list += [edge[0]]
        reverse_graph[edge[1]] = temp_list

def dfs_first_pass(graph, vertices, num):
    path = []
    visited = [False] * (num + 1)
    visited[0] = True
    for vertex in vertices:
        if visited[vertex] == False:
            paths(graph, vertex, path, visited)

    if num != len(path):
        for i in range(1, num + 1):
            if i not in path:
                path.append(i)

    return path
def dfs_second_pass(graph, stack, num):
    result = []
    ans = ""
    visited = [False] * (num + 1)
    visited[0] = True
    for vertex in stack:
        if visited[vertex] == False:
            temp = paths(graph, vertex, [], visited)
            for i in temp:
                if i not in result:
                    ans += f"{i} "
            ans += "\n"
            result += temp
    return ans

def paths(graph, index, path, visited):
    path.append(index)
    visited[index] = True
    if index in graph:
        for neighbor in graph[index]:
            if visited[neighbor] == False:
                temp = paths(graph, neighbor, path, visited)
    return path

stack_result = dfs_first_pass(course_graph, vertices_list, num_vertices[0])
output_result = dfs_second_pass(reverse_graph, stack_result, num_vertices[0])
output_lines = output_result.split("\n")
output_text = ""

for i in range(len(output_lines)):
    if i == len(output_lines) - 2:
        output_text += f"{output_lines[i]}"
    if i < len(output_lines) - 2:
        output_text += f"{output_lines[i]}\n"

output_file = open("Output3.txt", "w")
output_file.write(output_text)
output_file.close()
