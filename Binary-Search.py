def binary(array,target): 
  left,right=0,len(array)-1  #initial pointers
  while left<=right:         #Loop to search
    mid=(left+right)//2      #find mid index
    if array[mid]==target:   #Target found
       return mid
    elif array[mid]<target:  #Search right half
       left=mid+1
    else:                    #Search left half  
      right=mid-1
  return-1                   #Target Not found
  
  
array=[10,20,30,40.50]
target=30
result=binary(array,target)
print("target found at index:",{result})
