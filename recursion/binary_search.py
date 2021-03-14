def bin_search(arr, target, l, h):
	c = 0
	if l > h:
		return False
	else:
		mid = (l + h) // 2
		if target == arr[mid]:
			return True
		elif target > arr[mid]:
			c += 1 
			return bin_search(arr, target, mid + 1, h-1)
		else:
			c += 1
			return bin_search(arr, target, l , mid - 1)

		print(c)



if __name__ == '__main__':
	arr = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
	print(bin_search(arr, 22, 0, len(arr) - 1))