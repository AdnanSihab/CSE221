#Task1b
from collections import deque
input_file = open("Input1b.txt", "r")
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

def bfs_topological_sort(graph, vertices, num):
    queue = deque()
    in_degree = [0] * (num + 1)
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1
    queue = deque([vertex for vertex in range(1, num + 1) if in_degree[vertex] == 0])
    path = []
    count = 0
    while queue:
        current_node = queue.popleft()
        path.append(current_node)
        if current_node in graph:
            for neighbor in graph[current_node]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        count += 1
    if count != num:
        return None
    else:
        return path

result = bfs_topological_sort(course_graph, vertices_list, num_vertices[0])
output_text = ""
if result is not None:
    for vertex in result:
        output_text += f"{vertex} "
else:
    output_text = "IMPOSSIBLE"

output_file = open("Output1b.txt", "w")
output_file.write(output_text)
output_file.close()
