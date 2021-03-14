def swap(arr, l, h):
	if l < h:
		arr[l], arr[h] = arr[h], arr[l]
		return swap(arr, l+1, h-1)
	return arr

if __name__ == '__main__':
	arr = [4,3,6,2,7,8,9,5]
	print(swap(arr, 0, len(arr)-1))