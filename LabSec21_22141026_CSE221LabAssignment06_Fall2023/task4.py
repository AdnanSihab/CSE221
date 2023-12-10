#Task4
input_file=open("Input4.txt","r")
input_data=input_file.readline().split(" ")
lst=list(map(int,input_data))
input_lines=input_file.read().split("\n")
edges=[]
for line in input_lines:
  lst1=line.split(" ")
  lst2=list(map(int,lst1))
  connection=[lst2[0],lst2[1]]
  edges.append([lst2[2],connection])
edges.sort()
roots=[x for x in range(lst[1]+1)]
def find_root(node):
  if node==roots[node]:
    return node
  else:
    roots[node]=find_root(roots[node])
    return roots[node]
min_cost=0
for edge in edges:
  node1=find_root(edge[1][0])
  node2=find_root(edge[1][1])
  if node1!=node2:
    roots[node2]=node1
    min_cost+=edge[0]
output=f"{min_cost}"
output_file=open("Output4.txt","w")
output_file.write(output)
output_file.close()
