#Task1
input_file=open("Input1.txt","r")
input_data=input_file.readline().split(" ")
lst=list(map(int,input_data))
input_lines=input_file.read().split("\n")
arr=[]
source=None
index = 0
while index < len(input_lines):
    line = input_lines[index]
    lst1 = line.split(" ")
    lst2 = list(map(int, lst1))
    if len(arr) == lst[1]:
        source = lst2[0]
    else:
        arr.append(lst2)
    index += 1
graph=[[] for i in range(lst[0]+1)]
for i in arr:
  graph[i[0]].append((i[1],i[2]))
def dijkstra(graph,source,num):
  distance=[999]*(num+1)
  distance[source]=0
  temp=[(source,0)]
  while len(temp)!=0:
    node,dis=temp.pop(0)
    for node1,dis1 in graph[node]:
      dis2=dis1+dis
      if dis2<distance[node1]:
        distance[node1]=dis2
        temp.append((node1,dis2))
  for i in range(len(distance)):
    if distance[i]==999:
      distance[i]=-1
  return distance
ans=dijkstra(graph,source,lst[0])
output=""
for i in range(1,len(ans)):
  output+=f"{ans[i]} "
output_file=open("Output1.txt","w")
output_file.write(output)
output_file.close()
