#Task 1 a
in1a = open("input1a.txt", "r")
out1a = open("output1a.txt", "w")

temp1 = in1a.readline().split(" ")
desired_output = temp1[1]
temp2 = in1a.readline().split(" ")
count = 0
index_num = "Impossible"

for i in range(int(temp1[0]) - 1):
    for j in range(i + 1, int(temp1[0])):
        if int(temp2[i]) + int(temp2[j]) == int(desired_output):
            index_num = str(i + 1) + " " + str(j + 1)
            count += 1
            break

if count == 0:
    out1a.write("Impossible")
else:
    out1a.write(index_num)

in1a.close()
out1a.close()
