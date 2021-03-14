def plusMinus(arr):
    
    p_r = n_r = d = 0
    for i in arr:
        if i < 0 :
            n_r += 1
        elif i > 0:
            p_r += 1
        else:
        	d += 1
    out=str(format(p_r/len(arr), ".6f")) + "\n" + str(format(n_r/len(arr), ".6f")) + "\n" + str(format(d/len(arr), ".6f"))
    return out

if __name__ == '__main__':

	x = [-4 ,3 ,-9 ,0 ,4 ,1]
	print(plusMinus(x))

