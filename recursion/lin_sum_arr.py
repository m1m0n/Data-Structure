def arr_sum(arr, n):
	if n == 0:
		return 0
	else:
		return arr_sum(arr, n-1) + arr[n-1]

if __name__ == '__main__':
	arr = [4,3,6,2,8,9,3,2,8,5,1,7,2]
	print (arr_sum(arr, 5))
