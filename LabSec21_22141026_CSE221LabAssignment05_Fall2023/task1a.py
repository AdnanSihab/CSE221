#Task1a
input_file = open("Input1a.txt", "r")
input_data = input_file.readline().split(" ")
vertices = list(map(int, input_data))
input_lines = input_file.read().split("\n")
edges = []
courses = {}
vertices_list = []
for line in input_lines:
    line_data = line.split(" ")
    line_values = list(map(int, line_data))
    edges.append(line_values)
for i in range(1, vertices[0] + 1):
    vertices_list += [i]
for edge in edges:
    if edge[0] not in courses:
        courses[edge[0]] = [edge[1]]
    else:
        temp_list = []
        temp_list += courses[edge[0]]
        temp_list += [edge[1]]
        courses[edge[0]] = temp_list

def depth_first_search(graph, vertices, num):
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
            path.append(vertex)
    if None in path:
        return None
    else:
        path.reverse()
        return path

def find_paths(graph, index, path, visited, cycle):
    visited[index] = True
    if index in graph:
        for neighbor in graph[index]:
            if cycle[neighbor] == True:
                path.append(None)
            if visited[neighbor] == False:
                cycle[neighbor] = True
                find_paths(graph, neighbor, path, visited, cycle)
                cycle[neighbor] = False
                path.append(neighbor)
output = depth_first_search(courses, vertices_list, vertices[0])
output_text = ""
if output == None:
    output_text = "IMPOSSIBLE"
else:
    for value in output:
        output_text += f"{value} "

output_file = open("Output1a.txt", "w")
output_file.write(output_text)
output_file.close()
