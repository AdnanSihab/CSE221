with open("Input3.txt","r") as f:
  output = open("Output3.txt","w")
  line = int(f.readline())
  id = f.readline().split(" ")
  marks = f.readline().split(" ")
  marks_id_list = []
  for i in range(line) :
    j = [int(marks[i]),int(id[i])]
    marks_id_list.append(j)
  for i in range(len(marks_id_list)) :
    max_idx = i
    for j in range(i+1,len(marks_id_list)) :
      if marks_id_list[max_idx][0] == marks_id_list[j][0] :
        if marks_id_list[max_idx][1] > marks_id_list[j][1] :
          max_idx = j
      if marks_id_list[max_idx][0] < marks_id_list[j][0] :
        max_idx = j
    marks_id_list[i],marks_id_list[max_idx] = marks_id_list[max_idx],marks_id_list[i]


for i in range(line):
  output.write(f"ID: {str(marks_id_list[i][1])} Mark: {str(marks_id_list[i][0])}\n")

