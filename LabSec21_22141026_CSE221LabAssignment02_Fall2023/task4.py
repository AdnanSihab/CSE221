# Task 4
in4 = open("input4.txt","r")
out4 = open("output4.txt","w")
temp = in4.readline()
temp = temp.split()
lst = temp[1].split("\n")
temp1 = int(lst[0])
lst = in4.read().split("\n")
lst1 = []
for i in range(len(lst)):
  x = lst[i].split()
  lst1.append([int(x[0]),int(x[1])])
i = 0
while i < len(lst1) - 1:
    j = 0
    while j < len(lst1) - i - 1:
        if lst1[j][0] < lst1[j + 1][0]:
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
        j += 1
    i += 1
i = 1
j = 0
k = 1
count = 0
length = len(lst1)
while k <= temp1:
  if k == temp1 and length-count == 1:
    count += 1
  if lst1[i] != None:
    if lst1[j] != None:
      if lst1[i][1] <= lst1[j][0]:
        lst1[j] = None
        count += 1
        j = i
    else:
      j += 1
  if i == len(lst1)-1:
    if lst1[j] != None:
      count += 1
    lst1[j] = None
    j = 0
    i = 0
    k += 1
  i += 1
out4a = f"{count}"
out4.write(out4a)
out4.close()