#Try this
input3 = open("Input3.txt", "r")
input_data = input3.readline().split()
N, K = map(int, input_data)
friendships = []
for i in range(K):
    friendship = list(map(int, input3.readline().split()))
    friendships.append(friendship)
input3.close()

def calculate_friend_circle_size(N, friendships):
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    def find_set(x):
        if parent[x] != x:
            parent[x] = find_set(parent[x])
        return parent[x]
    def union_sets(a, b):
        root_a = find_set(a)
        root_b = find_set(b)
        if root_a != root_b:
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
    result = []
    for friendship in friendships:
        a, b = friendship
        union_sets(a, b)
        result.append(size[find_set(a)])
    return result

output = calculate_friend_circle_size(N, friendships)
output2 = open("Output3.txt", "w")
for item in output:
    output2.write(str(item) + "\n")
output2.close()
