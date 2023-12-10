#Task2
input_file=open("Input2.txt","r")
input_data=input_file.readline().split()
lst=list(map(int,input_data))
input_lines=input_file.read().split("\n")
arr=[]
source1=None
source2=None
for line in input_lines:
  lst1=line.split(" ")
  lst2=list(map(int,lst1))
  if len(arr)==lst[1]:
    source1=lst2[0]
    source2=lst2[1]
  else:
    arr.append(lst2)
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
  return distance
dis1=dijkstra(graph,source1,lst[0])
dis2=dijkstra(graph,source2,lst[0])
ans=[]
for i in range(len(dis1)):
  if dis1[i]>dis2[i]:
    ans+=[dis1[i]]
  else:
    ans+=[dis2[i]]
node=None
time=999
for i in range(1,len(ans)):
  if node==None or time>ans[i]:
    node=i
    time=ans[i]
if time==999:
  output="Impossible"
else:
  output=f"Time {time}\nNode {node}"
output_file=open("Output2.txt","w")
output_file.write(output)
output_file.close()
