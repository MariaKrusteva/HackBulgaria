def sevens_in_a_row(arr,n):
	count=1
	for i in range(0,len(arr)-n):
		if arr[i]==7:
			for j in range(i+1,n+i):
				if arr[j]==7:
					count+=1
		if(count>=n):
			break
		else:
			count=1
	return count>=n
