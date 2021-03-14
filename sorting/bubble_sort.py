# Complextiy = n^2/2 = O(n^2)
# num of Swap : n^2/4  --> N = 6, swap = 9
# Num of comparisons = n^2/2 --> N = 6, comp = 18
# Space Complextiy = O(1)
#Applications: get the first small element from n = 1000 000
# to make bubble sort a little bit smart. we can use a bool flag see if there is a swap or not 
# stable 
# One extram temp variable

def bubble_sort(arr):
	flag = True
	swaps = 0
	for i in range(len(arr)): #i: 0,1,2,3,4,5
		min_index = len(arr)-i-1 # 5 4 3 2 1 0 
		for j in range(min_index):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1], arr[j]
				flag = False
				swaps += 1
		if flag == True:
			break

	return arr, swaps

if __name__ == "__main__":
	arr = [6,8,4,5,9,2]
	# arr = [1, 2, 3, 4, 5]
	print(arr)

	print(bubble_sort(arr))
