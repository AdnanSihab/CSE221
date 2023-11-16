#Task 3
in3 = open("input3.txt","r")
out3 = open("output3.txt","w")
temp = in3.readline()
lst = in3.read().split("\n")
lst1 = []
for i in range(len(lst)):
  x=lst[i].split()
  lst1.append([int(x[0]),int(x[1])])
n = len(lst1)
i = 0
while i < n - 1:
    j = 0
    while j < n - i - 1:
        if lst1[j][1] > lst1[j + 1][1]:
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
        j += 1
    i += 1
temp1 = [lst1[0]]
j = 0
count = 1
for i in range(1,len(lst1)):
  if lst1[i][0] >= lst1[j][1]:
    count += 1
    temp1.append(lst1[i])
    j = i
res = f"{count}\n"
for i in range(len(temp1)):
  if i == len(temp1)-1:
    res += (f"{temp1[i][0]} {temp1[i][1]}")
  else:
    res += (f"{temp1[i][0]} {temp1[i][1]}\n")
out3.write(res)
out3.close()