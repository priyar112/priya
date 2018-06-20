def minimum(arr,n):
	min=arr[0]
	for i in range(1,n):
		if arr[i]<min:
			min=arr[i]
	return min
arr=[1,2,3]
n=len(arr)
ans=minimum(arr,n)
print(" minimum number in array is",ans)
