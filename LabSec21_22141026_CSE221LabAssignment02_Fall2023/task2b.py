#Task 2 b
in2a=open("input2b.txt", "r")
temp=in2a.readline()
lst1=in2a.readline().split(" ")
lst1=list(map(int,lst1))
temp1=in2a.readline()
lst2 =in2a.readline().split(" ")
lst2=list(map(int,lst2))

i,j = 0,0
out2b = ""
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        out2b+=str(lst1[i])
        i += 1
        out2b+=" "
    else:
        out2b+=str(lst2[j])
        j += 1
        out2b+=" "

while i < len(lst1):
    out2b += str(lst1[i])
    i += 1
    out2b += " "

while j < len(lst2):
    out2b += str(lst2[j])
    j += 1
    out2b += " "
    
res=open("output2b.txt", "w")
res.write(out2b)
res.close()