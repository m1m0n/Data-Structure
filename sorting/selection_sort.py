# Complextiy : O(n^2)
# num of Swap : n --> N = 6 , swap = 6
# num of comaprisons = n^2 --> N = 6, comp = 36
# Space Complextiy : O(1) -> no need for extra space
# Applications: Get smallest three numbers 
# stable 
# One extram temp variable

arr = [4,5,9,2, 15, 0, 65, -9]
swaps = 0
# Ascending
for i in range(0, len(arr)):
	min_index = i
	for j in range(i+1, len(arr)):
		if arr[j] < arr[min_index]:
			min_index = j
	arr[i], arr[min_index] = arr[min_index], arr[i]
	swaps += 1

print(arr, swaps)