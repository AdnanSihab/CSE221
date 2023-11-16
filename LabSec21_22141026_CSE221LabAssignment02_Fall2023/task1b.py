#Task 1 b
in1b = open("input1b.txt", "r")
out1b = open("output1b.txt", "w")
temp1, val = map(int, in1b.readline().split())
nums = list(map(int, in1b.readline().split()))
left = 0
right = temp1 - 1
res = "IMPOSSIBLE"

while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == val:
        res = (left + 1, right + 1)
        break
    elif current_sum < val:
        left += 1
    else:
        right -= 1
if res == "IMPOSSIBLE":
    out1b.write("IMPOSSIBLE")
else:
    out1b.write(f"{res[0]} {res[1]}")

in1b.close()
out1b.close()
