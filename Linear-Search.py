def Linearsearch(array,target):
    for i in range(len(array)):    #Loop through each index of array
        if array[i]==target:       #Check if current element matches the target

            return i               #return the index if Target found
    return -1                      #Target Not found
  
  
array=[1,2,3,4,5]
target=3
result=Linearsearch(array,target)
print("target found at index:",{result})
