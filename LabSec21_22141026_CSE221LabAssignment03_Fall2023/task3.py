#Task 3
in3 = open("Input3.txt", "r")
in3_first_line = in3.readline()
lst = in3.read().split(" ")
alien_heights = list(map(int, lst))

def merge_and_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inversions_left = merge_and_count_inversions(arr[:mid])
    right, inversions_right = merge_and_count_inversions(arr[mid:])
    merged, inversions = merge_and_count_split_inversions(left, right)
    return merged, (inversions + inversions_left + inversions_right)
def merge_and_count_split_inversions(left, right):
    merged = []
    i,j,inversions = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions
sorted_heights, inversions = merge_and_count_inversions(alien_heights)
result = str(inversions)
out3 = open("output3.txt", "w")
out3.write(result)
out3.close()
