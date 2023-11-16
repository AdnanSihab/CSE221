with open("Input1a.txt","r") as f:
  s=int(f.readline())
  g=open("Output1a.txt","w")
  for i in range(s):
    a=int(f.readline())
    if a%2!=0:
      g.write(f"{str(a)} is an odd number\n")
    else:
      g.write(f"{str(a)} is an even number\n")
  g.close()

