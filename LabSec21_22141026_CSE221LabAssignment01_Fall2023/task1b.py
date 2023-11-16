with open("Input1b.txt","r") as f:
  line=int(f.readline())
  g=open("Output1b.txt","w")
  sum=0
  for i in range(line):
    a=f.readline()
    arr=a.split(" ")
    if arr[2]=="+":
      sum=int(arr[1])+int(arr[3])
    elif arr[2]=="-":
      sum=int(arr[1])-int(arr[3])  
    elif arr[2]=="*":
      sum=int(arr[1])*int(arr[3])
    elif arr[2]=="/": 
      sum=int(arr[1])/int(arr[3])
    g.write(f"The result of {str(arr[1])} {str(arr[2])} {str(arr[3])} is {str(sum)}\n")

