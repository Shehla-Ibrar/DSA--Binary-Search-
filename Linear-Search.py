def Linearsearch(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
  
  
array=[1,2,3,4,5]
target=3
result=Linearsearch(array,target)
print("target found at index:",{result})
