# Python code to demonstrate  
# how to update an element in array 
  
# importing array module 
import array 
  
# initializing array with array values 
# initializes array with signed integers 
arr = array.array('i', [1, 2, 3, 1, 2, 5])  
  
# printing original array 
print ("Array before updation : ", end ="") 
for i in range (0, 6): 
    print (arr[i], end =" ") 
  
print ("\r") 
  
# updating a element in a array 
arr[2] = 6
print("Array after updation : ", end ="") 
for i in range (0, 6): 
    print (arr[i], end =" ") 
print() 
  
# updating a element in a array 
arr[4] = 8
print("Array after updation : ", end ="") 
for i in range (0, 6): 
    print (arr[i], end =" ") 
