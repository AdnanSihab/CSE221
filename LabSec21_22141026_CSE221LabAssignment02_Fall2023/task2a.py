#Task 2 a
in2a=open("input2a.txt", "r")
temp=in2a.readline()
lst1=in2a.readline().split(" ")
lst1=list(map(int,lst1))
temp1=in2a.readline()
lst2 =in2a.readline().split(" ")
lst2=list(map(int,lst2))
lst1 = lst1 + lst2
lst1.sort()
out2a = ""
for i in lst1:
    out2a+=str(i)
    out2a+=" "
output2=(f"{out2a}")
res=open("output2a.txt", "w")
res.write(output2)
res.close()