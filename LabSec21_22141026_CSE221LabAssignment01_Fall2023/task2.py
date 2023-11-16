f = open("Input2.txt","r")
output = open("Output2.txt","w")

iterator= int(f.readline())
g= f.readline()
arr = g.split(" ")
for i in range(iterator):
  arr[i]=int(arr[i])
bool = False 
i = 0 
while i < iterator-1 :
  if arr[i] < arr[i+1] :
    i+= 1
  else :
    bool = True
    break  
if bool :
  for i in range(len(arr)) :
    for j in range(len(arr)-i-1) :
      if int(arr[j]) > int(arr[j+1]) :
        arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr,file = output)
output.close()


'''
1. The given bubble sort code has a time complexity of θ(n^2) due to nested loops, with the first loop taking n time and the second loop also taking n time, resulting in a total of n^2 time.
2. In the best-case scenario where the input is already sorted, achieving θ(n) complexity is possible.
3. To accomplish this, a flag can be used to check if the input is sorted before applying the bubble sort algorithm.
4. If the input is already sorted, the flag becomes True, and the input can be printed directly without going through the nested loop of the bubble sort algorithm.
'''