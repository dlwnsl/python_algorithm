nums = []
for _ in range(9):
    nums.append(int(input()))

max = max(nums)
max_index = nums.index(max) + 1 

print(max) 
print(max_index) 