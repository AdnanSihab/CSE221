infile=open("Input4.txt","r")
outfile=open("Output4.txt","w")

N=int(infile.readline().strip())
train_info={}
temp_str=''
for i in range(N):
    temp=str(infile.readline().strip())
    temp_list=temp.split(' ')

    for j in temp_list:
        if temp_list[0] not in train_info:
            train_info[temp_list[0]]=[[temp_list[4], temp_list[-1]]]
        else:
            train_info[temp_list[0]].append([temp_list[4], temp_list[-1]])
        break

train_name=[]
for k in train_info:
    train_name.append(k)

def sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sort(train_name)

for k in train_info:
    for i in range(len(train_info[k])):
        for j in range(len(train_info[k])-i-1):
            if train_info[k][j][1] < train_info[k][j+1][1]:
                train_info[k][j], train_info[k][j+1]=train_info[k][j+1], train_info[k][j]
    
for z in train_name:
    for y in range(len(train_info[z])):
        outfile.write(f'{z} will departure for {train_info[z][y][0]} is {train_info[z][y][1]}\n')

outfile.close()