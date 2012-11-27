# Provides the merge sort algorithm with the following set of performance 
# characteristics
#     best    -- O(n log n) 
#     average -- O(n log n) 
#     worst   -- O(n log n) 
# This implementation sorts in place (). 
# 
# We might also want to consider using the .sort function in Python which
# to the best of my understanding it is base on Timsort.
# Performance characteristics for Timsort are clearly described at :
#    https://secure.wikimedia.org/wikipedia/en/wiki/Timsort
# 

def sort(array,s=0,e=-1):
	if e == -1:
	  e = len(array)
	  
	if e-s>1:                     
	  mid = s+((e-s)/2)
	  sort(array,s,mid)
	  sort(array,mid,e)
	  merge(array,s,mid,mid,e)
	return array

def merge(array,s1,e1,s2,e2):
	''' Minimizes copies.  Not truly inplace '''
	start = s1
	result = []
	while (e1-s1>0) and (e2-s2>0):
	 if (array[s1] <= array[s2]):
	   result.append(array[s1])        
	   s1 += 1
	 else:
	   result.append(array[s2])
	   s2 += 1

	result += array[s1:e1] + array[s2:e2]            
	array[start:e2]=result
	return array
