# Task2
input_file = open("Input2.txt", "r")
input_data = input_file.readline().split(" ")
num_vertices = list(map(int, input_data))
input_lines = input_file.read().split("\n")
edges = []
course_graph = {}
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

def dfs_topological_sort(graph, vertices, num):
    path = []
    visited = [False] * (num + 1)
    cycle = [False] * (num + 1)
    visited[0] = True
    cycle[0] = True
    for vertex in vertices:
        if cycle[vertex] == True:
            path.append(None)
        if visited[vertex] == False:
            cycle[vertex] = True
            find_paths(graph, vertex, path, visited, cycle)
            cycle[vertex] = False
    if None in path:
        return None
    else:
        return path

def find_paths(graph, index, path, visited, cycle):
    path.append(index)
    visited[index] = True
    if index in graph:
        for neighbor in graph[index]:
            if cycle[neighbor] == True:
                path.append(None)
            if visited[neighbor] == False:
                cycle[neighbor] = True
                find_paths(graph, neighbor, path, visited, cycle)
                cycle[neighbor] = False
    return path

result = dfs_topological_sort(course_graph, vertices_list, num_vertices[0])
output_text = ""

if result is not None:
    for vertex in result:
        output_text += f"{vertex} "
else:
    output_text = "IMPOSSIBLE"

output_file = open("Output2.txt", "w")
output_file.write(output_text)
output_file.close()
